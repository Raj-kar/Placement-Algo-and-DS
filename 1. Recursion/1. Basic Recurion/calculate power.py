def power_op(base, expo):
    ''' Using default operator'''
    print(base ** expo)


power_op(3, 4)


def power_ite(base, expo):
    '''Iterative Solution'''
    res = 1
    for _ in range(1, expo+1):
        res *= base
    return res


print(power_ite(3, 4))


def power(base, expo):
    '''Recursive Solution'''
    if expo == 0:
        return 1
    return power(base, expo-1) * base


print(power(3, 4))


def fast_power(base, expo):
    ''' Optimized way by Recursion !  nearby O(log n)'''
    if expo == 0:
        return 1
    if expo % 2 == 0:
        return fast_power(base*base, expo/2)
    return fast_power(base, expo - 1) * base


print(fast_power(3, 4))
