# A text file containing a logical sequence of commands is a script.
myString = "This is a string."

print(myString)

# Confirm that the script runs correctly and that the output displays as you expect it to.
# This is a string.

# Extend the Python script by using the built-in function type() to get the data type of the variable. Enter the following code:
print(type(myString))

# To convert the return value of type into a string, use the str() built-in function:
print(myString + " is of the data type " + str(type(myString)))


# Exercise 2: Working with string concatenation
# String concatenation is the process of combining two strings into one string. You have actually been doing string concatenation since lab 1, but you didn’t call this process by that term. The plus sign (+) is used to concatenate strings. When the plus sign (+) is used with strings, it behaves differently than when you use it for numbers. In lab 1, you used the plus sign (+) to add numbers. Now, you will use the plus sign (+) to combine, or concatenate, strings.

# Create two strings and then concatenate them by entering the following code:
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)


# Confirm that the script runs correctly and that the output displays as you expect it to.
#   This is a string.                                            
#   <class 'str'>                                                
#   This is a string. is of the data type <class 'str'>
#   waterfall




# Exercise 3: Working with input strings
# In coding, information that a user enters is known as input. You will use a built-in function named input() to get information from the user. The input() function will pause the code until a user enters a string and presses ENTER. Return to the Python script:

name = input("What is your name? ")

# Use the print() function to write the value of the variable to the shell:
print(name)

# Confirm that the script runs correctly and that the output displays as you expect it to.
#   This is a string.                                            
#   <class 'str'>                                                
#   This is a string. is of the data type <class 'str'>              
#   waterfall                                                    
#   What is your name? Snehal                                     
#   Snehal   


# Exercise 4: Formatting output strings
# When your script wants to communicate information back to the user, it is called output. You have been using the print() function to write output to the shell. You will create a survey and output the information that it collects back to the user.

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

# You have been using the print() function with only one variable, but you can also use it with multiple variables to format a string. Enter the following code:
print("{}, you like a {} {}!".format(name,color,animal))

# The Python shell has stopped and is waiting for your input.
# Enter a name and press ENTER.
# Next, you are asked for your favorite color. Enter a color and press ENTER.
# Next, you are asked for your favorite animal. Enter an animal and press ENTER.
# Finally, the script prints a formatted string to the user by using the three pieces of information that you provided. Confirm that the output in the shell looks like the following output.
#   This is a string.                                            
#   <class 'str'>                                                
#   This is a string. is of the data type <class 'str'>              
#   waterfall                                                    
#   What is your name? Snehal                                     
#   Snehal                                    
#   What is your favorite color?  Ponk                           
#   What is your favorite animal?  Cat                           
#   Snehal, you like a Pink Cat!