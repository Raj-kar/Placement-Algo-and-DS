def reverse_int(num):
    negative = False
    if (num < 0):
        negative = True
        num = num * - 1  # also can use abs(num)

    reverse = 0
    while(num):
        reverse = (reverse * 10) + (num % 10)
        num = round(num / 10)

    if negative:
        return reverse * -1
    else:
        return reverse


print(reverse_int(321))
print(reverse_int(-123))
print(reverse_int(210))
