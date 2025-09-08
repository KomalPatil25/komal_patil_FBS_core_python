def number(li, num):
    if(num in li):
        return num
    else:
        return None

li = [10, 72, 56, 39, 10, 53, 91, 10, 39]
num = int(input("Enter the number: "))
count = li.count(num)
res = number(li, num)
if(res):
    print(f'Element present in list.{count}')
else:
    print(f'Element not present in list.')