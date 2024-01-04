# program that parses the JSON data and calculates the molecular weigh

import jsonFileHandler

# Retrieve the the JSON data and store it in a data variable.

data = jsonFileHandler.readJsonFile('insulin.json')
# Test if the returned data is not empty and obtain the insulin data.

if data != "" :
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
else:
    print("Error. Exiting program")