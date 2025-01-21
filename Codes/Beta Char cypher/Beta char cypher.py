import random
import re
import os
import sys

def resourcePath(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("Codes\\Beta Char cypher\\")

    return os.path.join(base_path, relative_path)


# Ingredient packets: [Do encryption 0/1, first letter:last letter::0:1, character]. The second position is skipped if the first is 0. For example: [1, 0, 'k'] vs. [0, '2'] or [0, '@']

specialCharList = ['.', '!', '?', ',', ':', '@', "'", ';', '$', '%', '^', '&', '*', '(', ')', '[', ']', '_', '+', '-', ',', '#']

def futureCheck(position, word):
    pattern = r'^[^a-zA-Z\s]*$'
    return bool(re.match(pattern, word[position:]))
        
def decrypt(phrase, offset):
    """
    Decrypts a phrase encrypted by the Beta Char Cypher algorithm.

    Parameters
    ----------
    phrase : str
        The phrase to decrypt.
    offset : int
        The key to decrypt with.

    Returns
    -------
    str
        The decrypted phrase.
    """
    output = ""
    words = []
    splitPhrase = phrase.split()

    for part in splitPhrase: #for each word
        iterNum = 0
        exceptionEnabled = False
        for i, char in enumerate(part): #for each character
            if not exceptionEnabled:
                if futureCheck(i, part):
                    iterNum = i
                    exceptionEnabled = True

        if exceptionEnabled:
            words.append(part[:iterNum])
            words.append(part[iterNum:])
        else:
            words.append(part)

            
    for word in words:
        # If a ., !, or ? shows up, just append it to the string as well
        if all(char in specialCharList or char.isdigit() for char in word):
            output += word
            continue
        # Record 1st letter of word
        firstLetter = word[0]

        # Look at 2nd letter
        secondLetter = word[1]

        # Determine base position
        if secondLetter.lower() in 'abcdefghijklm':
            base = 0  # First letter
        else:
            base = -1  # Last letter
 
        # Calculate position change
        wordLength = len(word)
        #wordLength = sum(1 for char in word if char.isalpha())
        positionChange = wordLength % (offset - wordLength)

        # Calculate new position
        if base == 0:
            newPos = positionChange - 1
        else:
            newPos = 0 - positionChange

        if base == 0 and word[newPos] == 's':
            output += ' '
        else:
        # Append character at new position to result string
            output += word[newPos]

    return output

def scan_file(flag, letter):

    """
    Scans a file for words that fit certain criteria and returns a list of words.

    Parameters
    ----------
    flag : 0, 1
        0: Look for words with the last letter being the given letter and the second letter being in the first half of the alphabet.
        
        1: Look for words with the first letter being the given letter and the second letter being in the second half of the alphabet.
    letter : str
        The letter to look for in the word.

    Returns
    -------
    list
        A list of words that fit the criteria.
    """
    inputFile = resourcePath("englishWords.txt")
    output = []

    # Define the ranges for the second letter
    firstHalf = set('abcdefghijklm')
    secondHalf = set('nopqrstuvwxyz')

    with open(inputFile, 'r') as input_file:
        for line in input_file:
            word = line.strip()
            wordLen = len(word)
            
            if wordLen == offset:
                continue

            shiftNum = wordLen % (offset - wordLen)

            if flag == 0:
                if word[-1 + shiftNum].lower() == letter.lower() and word[1].lower() in firstHalf:
                    output.append(line)
            elif flag == 1:
                if word[0 - shiftNum].lower() == letter.lower() and word[1].lower() in secondHalf:
                    output.append(line)
    return output

def encrypt(phrase, offset):
    """
    Encrypts a phrase using the Beta Char Cypher algorithm.

    Parameters
    ----------
    phrase : str
        The phrase to encrypt.
    offset : int
        The key to encrypt with.

    Returns
    -------
    str
        The encrypted phrase.
    """
    
    output = ""
    ingredients = []
    for i in phrase:
        char = i
        if char == ' ':
            ingredients.append([1, 0, 's'])
            continue
        elif char == 's':
            ingredients.append([1, 1, 's'])
            continue
        elif not char.isalpha():
            ingredients.append([0, char])
            continue
        else:
            ingredients.append([1, random.randint(0,1), char])

    for i in ingredients:
        if i[0] == 0:
            output += str(i[1])
        elif i[0] == 1:
            output += ' ' + random.choice(scan_file(i[1], i[2])).replace('\n', '')

    return output

choice = input("Do you want to encrypt or decrypt? (e/d): ")
prompt = input("Please enter prompt: ").lower()
offset = int(input("Please enter the key #: ")) #0-7 is recommendeded. This increases the complexity of the cipher significantly but prevents the use of words that have this many characters. Its also not incredibly difficult to figure out the key, as using any other key of near length will most likely fail.

passCheck = False
while not passCheck:
    if choice == "d":
        passCheck = True
        output = decrypt(prompt, offset)
    elif choice == "e":
        passCheck = True
        output = encrypt(prompt, offset)
    else:
        print("Invalid input. Please try again.")

print(output)

import pyperclip

while True:
    copyCheck = input("Would you like to copy the output to your clipboard? (y/n): ")
    if copyCheck.lower() == "y":
        pyperclip.copy(output)
        print("Output copied to clipboard.")
        break
    elif copyCheck.lower() == "n":
        break
    else:
        print("Invalid input. Please try again.")

