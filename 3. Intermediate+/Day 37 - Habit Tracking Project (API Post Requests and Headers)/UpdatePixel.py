import requests
import sys
from datetime import datetime
from pixela_user_info import TOKEN, USERNAME, VAL_GRAPH_ID, pixela_endpoint, graph_endpoint, val_graph_endpoint

def update_pixel(value='0', date=datetime.now().strftime('%Y%m%d')):
    val_post_params = {
        'date': date, # yyyyMMdd format
        'quantity': str(value),
    }
    return requests.post(url=val_graph_endpoint, json=val_post_params, headers={'X-USER-TOKEN': TOKEN})

if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) > 2 or len(args) == 0:
        raise ValueError(f'Invalid number of arguments: {len(args)}; Provide value, date (optional, default today)')
    elif len(args) == 1:
        response = update_pixel(value=args[0])
    elif len(args) == 2:
        response = update_pixel(value=args[0], date=args[1])
    
    print(response.text)
 