import json,requests

url = "http://maps.googleapis.com/maps/api/directions/json?"

origin ="origin=Central+Park"
destination = '&destination=Times+Square'
sensor='&sensor=false'
mode='&mode=walking'

url = url+origin+destination+sensor+mode

data = requests.get(url)

binary = data.content

output = json.loads(binary)


print output['status']
print '\n'
print json.dumps(output, indent=4, sort_keys=True)

for route in output['routes']:
    for leg in route['legs']:
        for step in leg['steps']:
            print step['html_instructions']




