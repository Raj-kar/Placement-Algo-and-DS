def solution(arr):
    index = 0
    i = 0

    while(i < len(arr)):
        j = i
        while (j < len(arr) and arr[j] == arr[i]):
            j += 1
            
        arr[index + 1] = arr[i]
        if j - i > 1:
            _count = str(j - i)
            for char in _count:
                arr[index + 1] = char

        i = j

        print(arr)
        return index


print(solution(["a", "a", "b", "b", "c", "c", "c"]))
