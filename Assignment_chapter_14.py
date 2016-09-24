import urllib
import sys
import re
from xml.etree import ElementTree

numbers = []

open("Assignment_chapter_14.txt", "w").close()

url = "http://python-data.dr-chuck.net/comments_306448.xml"
content = urllib.urlopen(url).read()
with open("Assignment_chapter_14.txt","a") as myfile:
    myfile.write(content)

fileh = open("Assignment_chapter_14.txt")
for line in fileh:
    line = line.rstrip()
    if not line.endswith("</count>"):
        #print line
        continue
    else:
        numbers.extend(re.findall('[0-9]+', line))

print numbers        
print sum(map(int, numbers))

   
