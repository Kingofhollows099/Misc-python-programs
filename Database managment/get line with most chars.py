input_filename = "Database managment\output.txt"
words = []

with open(input_filename, 'r') as input_file:
        for line in input_file:
            word = line.strip()
            wordLen = len(word)
            if wordLen == 32:
                words.append(line)
print(words)