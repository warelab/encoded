import urllib, json
import os

url = os.environ['URL_PREF']+"/_indexer"
response = urllib.urlopen(url)
data = json.loads(response.read())

print data["status"]