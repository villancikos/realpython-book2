# XML Parsing 2

from xml.etree import ElementTree as et

doc = et.parse("cars.xml")

# outputs the make, model and cost of each car to the screen
for e in doc.findall("CAR"):
    print (e.find("MAKE").text + " " + e.find("MODEL").text + ", $" + e.find("COST").text)

