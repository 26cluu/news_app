import feedparser
from pygooglenews import GoogleNews
import json

gn = GoogleNews()
test = gn.geo_headlines('bay area')
entries = test['entries']
count = 0
for entry in entries:
    count += 1
    print(entry['title'])
print(count)
