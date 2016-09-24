#could not do it with BeautifulSoup

import sys
import re
import urllib
numbers = []

open("Assignment_1_chapter_13.txt", "w").close() # empty the file to remove previous content
url = "http://python-data.dr-chuck.net/comments_306451.html"

html = urllib.urlopen(url).read()
with open("Assignment_1_chapter_13.txt","a") as myfile:
    myfile.write(html)

fileh = open("Assignment_1_chapter_13.txt")
for line in fileh:
    if not line.startswith("<tr>"):
        continue
    else:
        line = line.rstrip()
        numbers.extend(re.findall('[0-9]+', line))
print numbers
print sum(map(int, numbers))

