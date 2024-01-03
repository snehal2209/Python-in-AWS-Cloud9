#A composite data type is any data type that comprises primitive data types. If you like food, you can visualize a composite data type as a turducken, which is a dish that consists of a chicken that is stuffed into a duck, which is stuffed into a turkey. In this lab, you will create a data type that consists of a string that is in a dictionary, which is in a list.

#First, import the modules that you will use:

import csv
import copy

#Next, define a dictionary that will serve as your composite type for reading the tabular data:
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#You will use a for loop to iterate over the initial keys and values of the dictionary.

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

#Note: The items() function belongs to the dictionary data type. The items() function tells the for loop to traverse the collection owned by the dictionary data type.

#Define an empty list to hold the car inventory that you will read:

myInventoryList = []





#Copying the CSV file into memory
#You will read in the data from disk (hard drive) and make an in-memory (random access memory, or RAM) copy. In a computer, a hard drive stores data long term, including when the power is turned off. RAM refers to temporary memory that is faster, but it is erased when the computer's power is turned off.

#You will be introduced to the with open syntax statement, which keeps a file open while you read data. It will automatically close the CSV file when the code inside the with block is finished running.

#You will also use a new way of formatting a string. Instead of using double quotation marks and .format to pass in the variables, you can use a single quotation mark and write in the variables between the "{}" symbols.

#Finally, csv.reader() is a function that you are using from the csv library that you imported with the import csv statement.

#Most of the rest of the code should be familiar.

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')

#Though this code seems like a large amount of code to process, it mostly comprises statements that you saw in earlier labs. You have a for loop with an if-else statement followed by a print() statement at the end.

#However, the following line needs further explanation:
currentVehicle = copy.deepcopy(myVehicle)
#By default, Python does a shallow copy of complex data types. A shallow copy refers, or points, to the storage location of the myVehicle dictionary variable. Without this line, you would have only one storage box, and only the last item in the list would be copied into memory. This line makes sure that new storage boxes are created in memory to store the new tabular data that is being read.


#Printing the car inventory
##You will finish the Python script by printing the car inventory from the myInventoryList variable.

for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")
