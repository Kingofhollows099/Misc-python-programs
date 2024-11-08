input_filename = "Codes/englishWords.txt"
output_filename = "Database managment/output.txt"
max = 0

with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
    for line in input_file:
        word = line.strip()
        wordLen = len(word)
        if wordLen != 32:
            output_file.write(line)