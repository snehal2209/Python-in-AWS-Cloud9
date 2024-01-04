# implementing a Caesar cipher in Python
# Function getDoubleAlphabet that takes a string argument and concatenates, or combines, the given string with itself
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    
# this function request a message to encrypt from the user
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
    

# The cipher key is how far you will shift the letters. By using two alphabets, you can have a cipher key that is any integer from 1 to 25. Don’t count the key at index 26 because that key would shift you back to the original message.

def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount
    
    

# Encrypting a message
# algorithm for encryption as follows:

# 1 Take three arguments: the message, the cipherKey, and the alphabet.
# 2 Initialize variables.
# 3 Use a for loop to traverse each letter in the message.
# 4 For a specific letter, find the position.
# 5 For a specific letter, determine the new position given the cipher key.
# 6 If current letter is in the alphabet, append the new letter to the encrypted message.
# 7 If current letter is not in the alphabet, append the current letter.
# 8 Return the encrypted message after exhausting all the letters in the message.

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
    
    
# Decrypting a message
# Functions are useful because you can reuse them. You will write a decryptMessage() function by reusing the encryptMessage() function. For this simple encryption, you can undo the encryption by shifting each letter back. Thus, instead of adding the cipher key, you will subtract the cipher key. To avoid rewriting most of the logic, you will pass in a negative cipher key.
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
    

# Creating a main function
# You have built a collection of user-defined functions that will help you write a Caesar cipher program. The main logic of the program will, of course, also be contained in a function.

# logic for Main Function:
# 1 Define a string variable to contain the English alphabet.
# 2 To be able to shift letters, double your alphabet string.
# 3 Get a message to encrypt from the user.
# 4 Get a cipher key from the user.
# 5 Encrypt the message.
# 6 Decrypt the message.

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
runCaesarCipherProgram()