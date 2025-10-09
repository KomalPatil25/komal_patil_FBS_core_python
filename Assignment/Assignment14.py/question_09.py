def three_sum(nums, target):
    result = []
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if(nums[i] + nums[j] + nums[k] == target):
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    if triplet not in result:
                        result.append(triplet)
    return result

numbers = [1, 2, -1, 0, -2, 1, -1, 2]
target = 2
res = three_sum(numbers, target)
print("Unique Triplets:", res)