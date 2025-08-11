vowel = input("enter the vowel(a, e, i, o, u):")

# if(vowel in 'a,e,i,o,u,A,E,I,O,U' ):
if(vowel in 'aeiouAEIOU' ):
    print(f"{vowel} is vowel")
else:
    print(f"{vowel} is consonent")