def permutations(string, l, r):
    if l == r:
        print(string)
        return

    for i in range(l, r + 1):
        string = string.replace(string[l], string[i])
        permutations(string, l+1, r)
        string = string.replace(string[l], string[i])
        

permutations("abc", 0, 2)
