'''
Question - ->
You are given an array of positive numbers where each integer represents the height of a vertical line on
a chart. Find two lines which together with the x-aixs forms a container that would hold the greatest
amount of water. Return the area of water it would be.
'''


def greatest_area(arr):
    max_area = 0
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(i+1, arr_len):
            area = min(arr[i], arr[j]) * (j - i)
            max_area = max(max_area, area)
    return max_area

# using slicing pointers or chain pointers [srink every step O(n)]


def optimized_area(arr):
    start = 0
    end = len(arr) - 1
    max_area = 0

    while start < end:
        height = min(arr[start], arr[end])
        area = height * (end - start)   # height * width
        max_area = max(max_area, area)

        if arr[start] <= arr[end]:
            start += 1
        else:
            end -= 1

    return max_area


print("optimized", optimized_area([1, 8, 6, 2, 9, 4]))
print("noraml", greatest_area([1, 8, 6, 2, 9, 4]))

print("optimized", optimized_area([1, 7, 2, 0, 1, 3]))
print("noraml", greatest_area([1, 7, 2, 0, 1, 3]))

print("optimized", optimized_area([1, 7, 2, 8, 1, 6]))
print("noraml", greatest_area([1, 7, 2, 8, 1, 6]))

print("optimized", optimized_area([]))
print("noraml", greatest_area([]))

print("optimized", optimized_area([7]))
print("noraml", greatest_area([7]))

print("optimized", optimized_area([6, 9, 3, 4, 5, 8]))
print("noraml", greatest_area([6, 9, 3, 4, 5, 8]))

print("optimized", optimized_area([2, 4]))
print("noraml", greatest_area([2, 4]))

print("optimized", optimized_area([9, 8, 1, 2, 3, 4]))
print("noraml", greatest_area([9, 8, 1, 2, 3, 4]))

'''
constrains -->
1. Does the thickness of the line affect the area ?
--> No, assume they take up no space.
2. Do the left and right sides of the graph count as walls ?
--> No, the sides can't be used a container.
3. Does a higher line inside our container affect our area ?
--> No, lines insidea a container don't affect the area.
 ** area formula  = L * W (Length * weight ) **
'''
