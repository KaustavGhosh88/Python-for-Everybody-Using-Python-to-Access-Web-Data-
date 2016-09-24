import urllib
import json

numbers = []

url = "http://python-data.dr-chuck.net/comments_306452.json"
url_h = urllib.urlopen(url).read()

info = json.loads(url_h)
counts = info['comments']

for item in counts:
    numbers.append(item['count'])

print "Count:", len(numbers)
print "Sum:", sum(numbers)
