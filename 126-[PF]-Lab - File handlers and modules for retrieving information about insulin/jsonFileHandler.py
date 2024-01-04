# Creating the JSON file handler module
# In this task, you create a module that reads the JSON file and returns the JSON document.

import json

# For the body of the function, open the json file using the open function, and parse the file using json.load.
def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file",IOError)
    return data
data = readJsonFile('insulin.json')
