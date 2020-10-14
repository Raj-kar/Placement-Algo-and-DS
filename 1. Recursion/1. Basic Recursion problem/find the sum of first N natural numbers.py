''' 
Iterative Solution
'''


def sumOfNatural(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


print(sumOfNatural(10))

''' 
Recursive Solution
'''


def sumOfNatural2(n):
    if (n == 1):
        return 1
    else:
        return sumOfNatural(n - 1) + n
    

print(sumOfNatural2(10))