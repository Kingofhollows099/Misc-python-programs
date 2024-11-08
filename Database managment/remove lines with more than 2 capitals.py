def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            word = line.strip()  # Remove leading/trailing whitespace
            if sum(1 for char in word if char.isupper()) <= 1:
                output_file.write(line)

# Example usage
input_file = "words.txt"
output_file = "output.txt"

process_file(input_file, output_file)
print(f"Processing complete. Results saved to {output_file}")