#Exercise 1: Creating a mixed-type list
#You can mix data types in a Python list. In other languages, this capability is not a feature of lists. In this exercise, you will explore this capability.

#Define a list with different types, like the following example:

myMixedTypeList = [22, 290578, 1.02, True, "My dog is on the bed.", "45"]

#Use a for loop statement to traverse the list and print the data type for each item in the list:
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))

#Confirm that the script runs correctly and that the output displays as you expect it to.

    #22 is of the data type <class 'int'>                             
    #290578 is of the data type <class 'int'>
    #1.02 is of the data type <class 'float'>
    #True is of the data type <class 'bool'>
    #My dog is on the bed. is of the data type <class 'str'>
    #45 is of the data type <class 'str'>
