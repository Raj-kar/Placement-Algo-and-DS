'''
Question - ->
Trapping Rainwater 
Given an array of integers representating an elevation map where the width of each bar is 1,
return how much rainwater can be trpped .
'''


def rainwater(arr):
    total, maxLeft, maxRight = 0, 0, 0
    p = 0
    pL, pR = p - 1, p + 1

    while p < len(arr):
        if pR > len(arr) - 1 and pL < 0:

            current_water = min(maxLeft, maxRight) - arr[p]
            if current_water > 0:
                total += current_water

            p += 1
            pL, pR = p - 1, p + 1
            maxLeft, maxRight = 0, 0

        if pL > -1:
            maxLeft = max(maxLeft, arr[pL])
        if pR < len(arr):
            maxRight = max(maxRight, arr[pR])
        pL -= 1
        pR += 1

    return total


print(rainwater([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]))  # 8
print(rainwater([5, 0, 3, 0, 0, 0, 2, 3, 4, 2, 1]))  # 20
print(rainwater([3, 4, 3]))  # 0
print(rainwater([4, 2, 0, 3, 2, 5]))

'''
constrains -->
1. Do the left and right sides of the graph count as well ?
--> No, the sides are not walls . 
2. Is there any Negative value ?
--> No, Only positive Interger values !
'''

''' 
TestCases  --> 
1. [0, 1, 0 , 2, 1, 0, 3, 1, 0 , 1, 2]
    return 8
2. []
    return 0
3. [3, 4, 3]
    return 0
'''
