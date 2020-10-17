'''
input = ["a","a","b","b","c","c","c"]
output = new length is 4 --> ["a",2,"b",2,"c",3]
'''

import collections


def compresion(arr):    # code is correct, but you have to make it using O(1) space complecity !
    dict1 = collections.Counter(arr)
    arr.clear()

    for key in dict1.keys():
        _count = dict1[key]
        if _count > 1:
            arr.extend([key, *list(str(_count))])
        else:
            arr.append(key)

    return f"length is {len(arr)} and the new array is {arr}"


print(compresion(["a", "a", "b", "b", "c", "c", "c"]))
print(compresion(["a"]))
print(compresion(["a", "b", "b", "b", "b", "b",
                  "b", "b", "b", "b", "b", "b", "b", "b"]))


# NOT DONE YET !!!
def opti_comp(arr):
    i = 0
    j = 1
    _count = 0

    while j < len(arr):
        if arr[i] == arr[j]:
            pass
        else:
            arr[_count] = arr.count(arr[_count])
            i = j

        _count += 1
        j += 1

    return arr


print(opti_comp(["a", 1, "b", 2, "c", "c", "c"]))
#                                  i        j
