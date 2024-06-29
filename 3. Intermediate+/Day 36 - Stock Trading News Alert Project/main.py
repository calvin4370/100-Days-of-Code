'''
To be ran every market opening 4.30am (EST)
'''
import requests
import os
import datetime

from twilio.rest import Client
from stocks_to_watch import stocks

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

ALPHAVANTAGE_API_KEY = os.environ['ALPHAVANTAGE_API_KEY']
NEWSAPI_KEY = os.environ['NEWSAPI_KEY']

stocks_with_big_change = {} # stock_ticker: (stock_name, percentage_change)

# Check when STOCK price increase/decreases by 5% between opening stock price and closing stock price
datetime_now = datetime.datetime.now()
yst_date_time = datetime_now - datetime.timedelta(days=1)
two_days_ago_date_time = datetime_now - datetime.timedelta(days=2)
tdy_date = datetime_now.strftime('%Y-%m-%d')
yst_date = yst_date_time.strftime('%Y-%m-%d')
two_days_ago_date = two_days_ago_date_time.strftime('%Y-%m-%d')

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': '(INSERT TICKER HERE)',
    'apikey': ALPHAVANTAGE_API_KEY,
}
for ticker, name in stocks.items():
    stock_params['symbol'] = ticker
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    data = response.json()

    with open('data.json', 'w') as file:
        print(f'Updated data.json with {data}')
        import json
        json.dump(data, file)
    
    tdy_data = data['Time Series (Daily)'][yst_date]
    yst_data = data['Time Series (Daily)'][yst_date]

    tdy_closing_price = float(tdy_data['4. close'])
    yst_closing_price = float(yst_data['4. close'])
    percentage_change = round((tdy_closing_price - yst_closing_price) / yst_closing_price * 100, 2)

    if abs(percentage_change) >= 5:
        stocks_with_big_change[ticker] = (name, percentage_change)


# For each stock with notable price changes, grab the top 3 headlines relating to the stock within the past 24hrs
news_params = {
    'apiKey': NEWSAPI_KEY,
    'q': f'(TICKER) OR (NAME)',
    'searchIn': 'title',
    'from': yst_date,
    'to': tdy_date,
    'language': 'en',
    'sortBy': 'popularity',
}
for ticker, attributes in stocks_with_big_change.items():
    name, percentage_change = attributes
    headlines = []
    news_params['q'] = f'{ticker} OR {name}' # Update the query for the specific stock

    response = requests.get(NEWS_ENDPOINT, params=news_params)
    data = response.json()
    articles = data['articles'][:3] # Get up to 3 headlines

    # Update each entry to ticker: (name, percentage_change, list_of_articles)
    stocks_with_big_change[ticker] = (name, percentage_change, articles)


# Send a seperate message with the percentage change and each article's title and description to your phone number. 
# Twilio API
# With environment variables
account_sid = os.environ["TWILIO_WHATSAPP_SID"] # For WhatsApp only
auth_token = os.environ["TWILIO_WHATSAPP_AUTH_TOKEN"] # For WhatsApp only
my_phone_number = os.environ["PERSONAL_PHONE_NUMBER"]

client = Client(account_sid, auth_token)

for ticker, attributes in stocks_with_big_change.items():
    name, percentage_change, articles = attributes
    body = f""""""
    # Message Title
    if percentage_change > 0:
        body += f'{ticker} ({name}): 🔼{percentage_change}%\n'
    else:
        body += f'{ticker} ({name}): 🔻-{percentage_change}%\n'
    
    # Link to articles
    for article in articles:
        body += f"""\n*{article['source']['name']}: {article['title']}*\n
        {article['description']}\n
        {article['url']}\n\n"""

    message = client.messages.create(
        body=body.rstrip(),
        from_="whatsapp:+14155238886",
        to=f'whatsapp:{my_phone_number}',
    )

    print(f'DEBUG: Sent {len(articles)} articles on {ticker} to your WhatsApp')


#Optional: Format the SMS message like this: 
""":
TSLA: 🔺🔼2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻-5% ⏫🔽⏬
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

if __name__ == '__main__':
    try:
        pass
    except:
        print('FAILED TO RUN')