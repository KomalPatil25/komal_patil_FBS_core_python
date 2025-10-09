def max_product_pair(numbers):
    nums = list(set(numbers))

    if(len(nums) < 2):
        return None, None, None
    
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in nums:
        if(num > max1):
            max2 = max1
            max1 = num

        elif(num > max2):
            max2 = num

        if(num < min1):
            min2 = min1
            min1 = num

        elif(num < min2):
            min2 = num

    product1 = max1 * max2
    product2 = min1 * min2

    if(product1 >= product2):
        return max1, max2, product1
    else:
        return min1, min2, product2
    
numbers = [1, 10, -5, -2, 7, 3]
res = max_product_pair(numbers)
print(res)
        
