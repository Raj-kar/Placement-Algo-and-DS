def sum_of_natural(num):
    '''Using Iterative approatch '''
    res = 0
    for i in range(1, num+1):
        res += i
    return res


print(sum_of_natural(10))


def sum_of_natural_2(num):
    '''Recursive Solution'''
    if num == 1:
        return 1
    return sum_of_natural_2(num - 1) + num


print(sum_of_natural_2(10))
