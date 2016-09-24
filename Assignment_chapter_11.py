import urllib
import sys
import re

numbers = []
open("Assignment_chapter_11.txt", "w").close() # empty the file to clear previous content

url = "http://python-data.dr-chuck.net/regex_sum_306446.txt"
url_h = urllib.urlopen(url).read()
with open("Assignment_chapter_11.txt","a") as myfile:
    myfile.write(url_h)

fileh = open("Assignment_chapter_11.txt")
for line in fileh:
    line = line.rstrip()
    numbers.extend(re.findall('[0-9]+', line)) # the method extend() appends the contents of lists.
#print numbers
print sum(map(int, numbers))

