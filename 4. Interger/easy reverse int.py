def reverse_int(num):
    Negative = False
    try:
        num = int(num)
        if (num < 0):
            Negative = True
            num = num * - 1  # also can use abs(num)

        reverse = 0
        while(num):
            reverse = (reverse * 10) + (num % 10)
            num = num // 10

        if Negative:
            return int(reverse * -1)
        else:
            return int(reverse)
    except:
        return "Invalid input"


print(reverse_int(321))
print(reverse_int(-123))
print(reverse_int(210))

# validation check
print(reverse_int("200"))   # 2
print(reverse_int("hey reversed !"))
print(reverse_int(900000))
