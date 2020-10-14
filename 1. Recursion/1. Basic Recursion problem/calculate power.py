''' 
Using operator Solution
'''


def powerOp(base, expo):
    print(base ** expo)


powerOp(3, 4)

''' 
Iterative Solution
'''


def powerIte(base, expo):
    res = 1
    for _ in range(1, expo+1):
        res *= base
    print(res)


powerIte(3, 4)


''' 
Recursive Solution
'''


def power(base, expo):
    if (expo <= 1):
        return base
    return power(base, expo-1) * base


print(power(3, 4))
