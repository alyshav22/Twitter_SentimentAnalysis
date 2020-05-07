import requests
from requests_oauthlib import OAuth1
import jsonlines

api_key = "0JxAh5bjGidMWFKokzJOrm3oX"
api_secret = "WO5SNh9nmYCaGGO3vVvPivxrtPpMw7iezKOSzl9mLWGQxLQF9Y"
access_token_key = "2648886764-WZ5ETxoxuxcL2juUJMoxeyb2Io4pNo2RsELGFlw"
access_token_secret = "6SV65SXNRZh4pyAoOfCuNnvuXK43leJjLP7KPaZfcvedT"

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(api_key, api_secret, access_token_key, access_token_secret)

r = requests.get(url, auth=auth)
print(r.status_code)

url = 'https://stream.twitter.com/1.1/statuses/sample.json'
r = requests.get(url, auth=auth, stream=True)
if r.encoding is None:
    r.encoding = 'utf-8'

with jsonlines.open('output.json', mode='w') as writer:    
    try:
        for line in r.iter_lines(decode_unicode=True):
            if line:
                writer.write(line)
    except KeyboardInterrupt:
        pass
