import random
offset = 5 #0-7 is recommendeded. This increases the complexity of the cypher significantly, but prevents the use of words that have this many characters.

# Ingredient packets: [Do encryption 0/1, first letter:last letter::0:1, character]. Second position is skipped if first is 0. for example: [1, 0, 'k'] vs. [0, '2'] or [0, '@']

def decrypt(phrase, offset):
    output = ""
    words = []
    split_phrase = phrase.split()
    for part in split_phrase:
        start = 0
        for i, char in enumerate(part):
            if char.isdigit():
                if start < i:
                    words.append(part[start:i])
                end_idx = i
                while end_idx < len(part) and part[end_idx].isdigit():
                    end_idx += 1
                words.append(part[i:end_idx])
                start = end_idx
            elif char in ['.', '!', '?']:
                if start < i:
                    words.append(part[start:i])
                words.append(char)
                start = i + 1
        if start < len(part):
            words.append(part[start:])
            
    for word in words:
        # If a ., !, or ? shows up, just append it to the string as well
        if word in ['.', '!', '?', ',', ':', '@', "'", ';', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', ','] or word.isdigit():
            output += word
            continue
        # Record 1st letter of word
        first_letter = word[0]

        # Look at 2nd letter
        second_letter = word[1]

        # Determine base position
        if second_letter.lower() in 'abcdefghijklm':
            base = 0  # First letter
        else:
            base = -1  # Last letter
 
        # Calculate position change
        word_length = len(word)
        #word_length = sum(1 for char in word if char.isalpha())
        position_change = word_length % (offset - word_length)

        # Calculate new position
        if base == 0:
            new_position = position_change - 1
        else:
            new_position = 0 - position_change

        if base == 0 and word[new_position] == 's':
            output += ' '
        else:
        # Append character at new position to result string
            output += word[new_position]

    return output

def scan_file(flag, letter):
    """Scans a file and returns a list of words that match a given letter based on its position in the word.
       The flag parameter determines whether the first or last letter is compared, and the second letter is compared to a set of letters (A-K or L-Z).
       The function reads a file line by line, stripping the leading/trailing whitespace, and checks if the word length is equal to the offset. If so, it skips the word. 
       The function then checks if the word matches the given letter at the given position (first or last) and if the second letter is in the set of letters. 
       If so, it adds the line to the output list. The function returns the list of matching words.
       """
    input_filename = "Codes/englishWords.txt"
    output = []

    # Define the ranges for the second letter
    first_half = set('abcdefghijklm')
    second_half = set('nopqrstuvwxyz')

    with open(input_filename, 'r') as input_file:
        for line in input_file:
            word = line.strip()
            wordLen = len(word)
            
            if wordLen == offset:
                continue

            shiftNum = wordLen % (offset - wordLen)

            if flag == 0:
                # Check if the first letter matches and the second letter is A-K
                if word[-1 + shiftNum].lower() == letter.lower() and word[1].lower() in first_half:
                    output.append(line)
            elif flag == 1:
                # Check if the last letter matches and the second letter is L-Z
                if word[0 - shiftNum].lower() == letter.lower() and word[1].lower() in second_half:
                    output.append(line)
    return output

def encrypt(phrase, offset):
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

choise = input("Do you want to encrypt or decrypt? (e/d): ")
prompt = input("Please enter prompt: ").lower()

if choise == "d":
    output = decrypt(prompt, offset)
elif choise == "e":
    output = encrypt(prompt, offset)

print(output)

