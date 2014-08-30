# JSON Parsing 1

import json

# decodes the json file
output = json.load(open('cars.json'))

# display output screen
#print output[0]["CAR"][0]["MODEL"]
print output["CARS"][0]["MODEL"]
