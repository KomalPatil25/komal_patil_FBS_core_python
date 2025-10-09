def group_anagram(words):
    anagram_group = {}

    for word in words:
        key = ''.join(sorted(word))

        if(key not in anagram_group):
            anagram_group[key] = []

    anagram_group[key].append(word)
    return list(anagram_group.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = group_anagram(words)
print("Grouped Anagram:")
for group in res:
    print(group)