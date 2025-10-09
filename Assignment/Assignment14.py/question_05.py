def longest_prefix(words):
    prefix = " "
    for chars in zip(*words):
        if(len(set(chars))) == 1:
            prefix += chars[0]
        else:
            break
    return prefix

words = ["flowera", "flow", "flight"]
res = longest_prefix(words)
print("Lengest Common Prefix:", res)