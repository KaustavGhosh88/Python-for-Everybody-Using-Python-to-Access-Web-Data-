# help taken from GitHub

import urllib2
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/known_by_Unity.html"
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))

names = []

while count > 0:
    print format(url)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    anchors = soup('a')
    name = anchors[position-1].string
    names.append(name)
    url = anchors[position-1]['href']
    count -= 1

print names[-1]