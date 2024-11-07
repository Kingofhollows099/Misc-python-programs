import random
prompt = input("Please enter prompt: ").lower()
ingredients = []
output = ""

# Ingredient packets: [Do encryption 0/1, first letter:last letter::0:1, character]. Second position is skipped if first is 0. for example: [1, 0, 'k'] vs. [0, '2'] or [0, '@']

for i in prompt:
    char = prompt[i]
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