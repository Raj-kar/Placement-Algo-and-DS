def reverse_int(num):
    negative = False
    try:
        num = int(num)
        if (num < 0):
            negative = True
            num = num * - 1  # also can use abs(num)

        reverse = 0
        while(num):
            reverse = (reverse * 10) + (num % 10)
            num = int(num / 10)

        if 2 ** 31 < int(reverse):
            return 0
        if negative:
            return int(reverse * -1)
        else:
            return int(reverse)
    except:
        return None


print(reverse_int(321))
print(reverse_int(-123))
print(reverse_int(210))

# validation check
print(reverse_int("200"))   # 2
print(reverse_int("hey reversed !"))
print(reverse_int(900000))
