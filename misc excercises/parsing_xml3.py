# XML Parsing 2

from xml.etree import ElementTree as et
import requests

# retrieve an xml doc from a web server
xml = requests.get("http://www.w3schools.com/xml/cd_catalog.xml")

with open("test.xml","wb") as code:
    code.write(xml.content)


doc = et.parse("test.xml")

# outputs the album, artist and year of each CD to the screen
for e in doc.findall("CD"):
    print "Album: ", e.find("TITLE").text
    print "Artist: ", e.find("ARTIST").text
    print "Year: ", e.find("YEAR").text, "\n"
