def find_first_duplicate(nums):
    num_set = set()
    no_duplicate = "No-Duplicate"

    for i in range(len(nums)):

        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_duplicate

print(find_first_duplicate([2,5,3,2,1,5]))
print(find_first_duplicate([4,2,3,3,2,5]))