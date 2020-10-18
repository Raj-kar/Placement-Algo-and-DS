def palindrome(num):
    if num < 0:
        return False
    NUM = num
    reverse = 0
    while(num):
        rem = num % 10
        reverse = (reverse * 10) + rem
        num = int(num / 10)

    if NUM == reverse:
        return True
    else:
        return False


print(palindrome(121))
print(palindrome(10))
print(palindrome(-123))
