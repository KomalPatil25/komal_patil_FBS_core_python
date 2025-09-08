def string(str):
    if(len(str) < 2):
        return 'String is shortfor swap.'
    else:
        ch = list(str)
        ch[0], ch[-1] = ch[-1], ch[0]
        n_str = ''.join(ch)
        return n_str

str = input("Enter the string: ")
res = string(str)
print("Original string: ", str)
print("After changing: ", res)