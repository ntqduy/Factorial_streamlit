def fact(value):
    if value == 0 or value == 1:
        return 1
    else:
        return value * fact(value - 1)
