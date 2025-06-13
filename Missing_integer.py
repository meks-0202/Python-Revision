nums=[7, 2 , 6, 3, 9, 4] 
def IsMissing(nums):
    nums = sorted(nums)
    missing_list=[]
    for i in range(nums[0], nums[-1]):
        if i not in nums:
            missing_list.append(i)
    return missing_list
print(IsMissing(nums))
