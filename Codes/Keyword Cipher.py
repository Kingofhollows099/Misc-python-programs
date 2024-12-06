#Instructions and notes

#Hello! To use this encrypter, first you need to know how the cypher works.
#With the keyword cypher, You first create the keyword. (a word tha the cypher cannot be decoded without.)
#The Keyword must not have any repeating letters. So cantrip would work while goodbye would not.
#And you move all the letters from the alphabet to the front to spell the word. So if my keyword was master,
#the encoded alphabet would be m = a, a = b, s = c, t = d, e = e, r = f, b = g, c = h, d = i, f = j, etc.
#the code will eventually correct itself as it nears the end of the alphabet. 

import string

def keywordEncrypt(keyword, msg):
    alpha = string.ascii_lowercase
    mainA = string.ascii_lowercase
    newAlpha = ''
    newAlpha += keyword
    for l in alpha:
        if l in list(keyword):
            alpha = alpha.replace(l, '')
    newAlpha += alpha
    cipher = dict(zip(mainA, newAlpha))
    cipherU = dict(zip(mainA.upper(), newAlpha.upper()))
    encrypt = ''
    for i in msg.lower():
        if i.isalpha():
            if i.islower():
                encrypt += cipher[i.lower()]
            elif i.isupper():
                encrypt += cipherU[i.upper()]
        else:
            encrypt += i
    return encrypt
print(keywordEncrypt(input('What is the keyword? '), input('What is the sentence? ')))
