from typing import List

def twoSum(nums : List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]
    return -1

input_nums = [3, 3]
input_target = 6
output = twoSum(input_nums, input_target)
print(output)