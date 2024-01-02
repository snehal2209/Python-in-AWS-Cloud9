# Exercise 1: Introducing the list data type
# Defining a list
# In this activity, you will edit a Python script to hold a collection of fruit names, or a list of fruit.

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))



# Accessing a list by position
# You can access the contents of a list by position. In this activity, you will print out each item in our list by their position:

# In programming languages, the list position starts at zero (0). The brackets tell Python which position in the list you want. To access the apple string, enter the following code:
print(myFruitList[0])

# To access the banana string, enter the following:
print(myFruitList[1])

# To access the cherry string, enter the following code:
print(myFruitList[2])




# Changing the values in a list
# The values of a list can be changed. In this activity, you will change cherry to orange.
# In Python, list position starts at zero (0), so you must use the numeral 2 to access the third position. Enter the following code:
myFruitList[2] = "orange"

# Print the updated list:
print(myFruitList)

# Confirm that the script runs correctly and that the output displays as you expect it to.
  # ['apple', 'banana', 'cherry']                                
  # <class 'list'>                                               
  # apple                                                        
  # banana                                                       
  # cherry                                                       
  # ['apple', 'banana', 'orange'] 




# Exercise 2: Introducing the tuple data type
# Defining a tuple
# The tuple is like a list, but it can't be changed. A data type that can't be changed after it's created is said to be immutable. To define a tuple, you use parentheses instead of brackets ([]).

# Create a tuple by entering the following code:

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))




# Accessing a tuple by position
# Like a list, the items of a tuple can also be accessed by position:
# To access the apple string, enter the following code:
print(myFinalAnswerTuple[0])

# To access the banana string, enter the following code:
print(myFinalAnswerTuple[1])

# To access the pineapple string, enter the following code:
print(myFinalAnswerTuple[2])


# Confirm that the script runs correctly and that the output displays as you expect it to.
  # ['apple', 'banana', 'cherry']                                
  # <class 'list'>                                               
  # apple                                                        
  # banana                                                       
  # cherry                                                       
  # ['apple', 'banana', 'orange']                                
  # ('apple', 'banana', 'pineapple')                             
  # <class 'tuple'>                                              
  # apple                                                        
  # banana                                                       
  # pineapple
  
  
# Exercise 3: Introducing the dictionary data type
# Defining a dictionary
# A dictionary is a list with named positions (keys). Imagine that your list shows people’s favorite fruit.

myFavoriteFruitDictionary = {
  "Manu" : "apple",
  "Madhu" : "banana",
  "Shubu" : "pineapple"
}


# Use the print() function to write the dictionary to the shell:
print(myFavoriteFruitDictionary)

# Use the type() function to write the data type to the shell:
print(type(myFavoriteFruitDictionary))
# Save and run the file.




# Accessing a dictionary by name
# In this activity, you will use the name of the individuals to get their favorite fruit, instead of numbers.

# To access Manu's favorite fruit, enter the following code:
print("Manu's Favourite Fruit is : "+myFavoriteFruitDictionary["Manu"])

# To access Madhu's favorite fruit, enter the following code:
print("Madhu's Favourite Fruit is : "+myFavoriteFruitDictionary["Madhu"])

# To access Shubu's favorite fruit, enter the following code:
print("Shubhu's Favourite Fruit is : "+myFavoriteFruitDictionary["Shubu"])

# Save and run the file.
# Confirm that the script runs correctly and that the output displays as you expect it to.

  # ['apple', 'banana', 'cherry']
  # <class 'list'>
  # apple
  # banana
  # cherry
  # ['apple', 'banana', 'orange']
  # ('apple', 'banana', 'pineapple')
  # <class 'tuple'>
  # apple
  # banana
  # pineapple
  # {'Manu': 'apple', 'Madhu': 'banana', 'Shubu': 'pineapple'}
  # <class 'dict'>
  # Manu's Favourite Fruit is : apple
  # Madhu's Favourite Fruit is : banana
  # Shubhu's Favourite Fruit is : pineapple                                             

# Congratulations! You have worked with the list, tuple, and dictionary data types in Python.