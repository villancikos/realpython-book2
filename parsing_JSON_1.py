# JSON Parsing 1

import json

# decodes the json file
output = json.load(open('cars.json'))

# display output screen
print output
print " "
print json.dumps(output, indent=4, sort_keys=True)

