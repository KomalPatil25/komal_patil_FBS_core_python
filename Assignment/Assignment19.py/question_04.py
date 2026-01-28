v = input("Enter the vowel: ")
vowel = "".join([ch for ch in v if ch not in 'aeiouAEIOU'])
print(f"String without vowels: {vowel}")