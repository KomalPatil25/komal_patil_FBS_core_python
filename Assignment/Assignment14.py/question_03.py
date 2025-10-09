# str = ["table chair table"]

# word = []
# for i in str:
#     word.extend(i.split())

# unique_word = set(word)

# word_freq = {}
# for i in word:
#     word_freq[i] = word_freq.get(i, 0) + 1
# print("Unique_word: ", unique_word)
# print("Word frequency: ", word_freq)


str = 'python is an is language'
li = str.split()
uni_word = []

for word in li:
    uni_word.append(word)
print(uni_word)