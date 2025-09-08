# str = 'I an playing a game.'
# print(str.replace('a', '$'))

text = 'I am playing a game.'
new_text = " "

for char in text:
    if(char == 'a'):
        new_text += '$'
    else:
        new_text += char

print("Original string is: ", text)
print("Modified text is: ", new_text)