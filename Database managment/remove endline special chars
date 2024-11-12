input_filename = "Codes\Beta Char cypher\englishWords.txt"
output_filename = "Database managment/output.txt"

with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
    for line in input_file:
        word = line.strip()
        allow = True
        for i, char in enumerate(word):
            if char in ['.', '!', '?', ',', ':', '@', "'", ';', '$', '%', '^', '&', '*', '(', ')', '[', ']', '_', '+', '-', ',', '#'] and i == len(word) - 1:
                allow = False
        if allow:
            output_file.write(word + '\n')