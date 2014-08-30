import requests

url = 'http://text-processing.com/api/sentiment/'
data = {'text':'great'}
    r = requests.post(url,data=data)
print r.content
