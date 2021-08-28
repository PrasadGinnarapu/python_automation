"""imported the requests library"""
import requests

DATA_URL = "https://simple.wikipedia.org/wiki/Rose"

# URL of the image to be downloaded is defined as image_url
OBJECT= requests.get(DATA_URL)  # create HTTP response object



# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("webcontent.txt", 'wb') as f:
    # Saving received content as a png file in
    # binary format

    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(OBJECT.content)
