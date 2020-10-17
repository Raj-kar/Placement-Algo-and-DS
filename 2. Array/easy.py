'''
Question - ->
Return indixes of the sum of pair from an array .     '''


def sum_of_pair(nums, target):
    numsMap = {}

    for i in range(len(nums)):
        if nums[i] in numsMap:
            return (numsMap[nums[i]], i)
        else:
            numsMap[target - nums[i]] = i
    return None


print(sum_of_pair([1, 3, 7, 9, 2], 11))  # (3,4)
print(sum_of_pair([1, 3, 7, 9, 2], 5))  # (1,4)
print(sum_of_pair([1, 3, 7, 9, 2], 14))  # None

''' 
constrains -->
1. Are the numbers positive or can be there be negatives ?
--> All numbers are positive. 
2. Are there dublicate numbers ?
--> No, there are no dublicate numbers. 
3. Where do we return if there's no solution ?
--> Just Return False or Null(None). 
4. Will there always be a solution ?
--> Yes, there is always a solution. 
5. Can there be multiple paires that add up to the target ?
--> No, Only 1 pair of numbers add up to the target .
'''
