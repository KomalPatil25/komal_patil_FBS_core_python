def nthIndex(str, n):
    if(n < 0 or n > len(str)):
        return 'Invalid index.'
    else:
        result = str[:n] + str[n+1: ]
        return result
    
str = input("Enter the string: ")
n = int(input("Enter the number to remove nth index: "))
final_res = nthIndex(str, n)
print(final_res)
