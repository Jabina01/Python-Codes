def pattern(number):
    if number == 1:
        return 1
    else:
        return pattern(number-1) + 3
print(pattern(7))

