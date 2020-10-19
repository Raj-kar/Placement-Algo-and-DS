def sum_of_pair(arr, target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]

    return None


print(sum_of_pair([1, 3, 7, 9, 2], 4))
