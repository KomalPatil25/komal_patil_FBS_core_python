text = input("Enter the text: ")
word = [word for word in text.split() if len(word) <= 5]
print("Words with less than 5 letters: ", word)