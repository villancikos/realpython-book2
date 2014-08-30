from bs4 import BeautifulSoup
from urllib2 import urlopen
URL = 'http://web2py.com'
htmlPage = urlopen(URL)
htmlText = htmlPage.read()
mySoup = BeautifulSoup(htmlText)

for link in mySoup.find_all('a'):
    print link["href"]
