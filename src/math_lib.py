def max(digits):
    if digits is None:
        return None

    if not digits:
        return None

    max_num = digits[0]

    for num in digits:
        if num > max_num:
            max_num = num

    return max_num


def is_perfect(digit):
    if digit is None:
        return None

    div_sum = 0
    for i in range(1, digit):
        if digit % i == 0:
            div_sum = div_sum + i

    if div_sum == digit:
        return True
    else:
        return False
