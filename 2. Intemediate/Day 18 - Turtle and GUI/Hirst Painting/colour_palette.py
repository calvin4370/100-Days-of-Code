import colorgram

# Extract all used colours from the stupid Hirst painting as a list in order of proportion of image
# the 1st is beige for the back ground and 2nd is black transparency
# there are 33 colours other than the beige background and black transparency, i used 35 to get all of the colours, but 50 for example, can also be used
print("Using colorgram to extract colours from the stupid Hirst painting...")
hirst_colours = colorgram.extract("antipyrylazo_iii.jpg", 35)
print("Colour extraction complete. Beige background and 33 spot colours identified.\n")

bg_colour = (hirst_colours[0].rgb.r, hirst_colours[0].rgb.g, hirst_colours[0].rgb.b)
hirst_colours = hirst_colours[2:]

spot_colours = []

for Color_ in hirst_colours:
    rgb_tuple = (Color_.rgb.r, Color_.rgb.g, Color_.rgb.b)
    spot_colours.append(rgb_tuple)
    

# NOTE All these colours are Rgb objects with r, g, b values, access them with colour.r etc.
"""
bg_color is a rgb tuple representing the beige background colour used by the stupid Hirst painting
spot_colours is a list of rgb tuples of the spot colours used
"""