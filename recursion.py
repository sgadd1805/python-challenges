def palidrome(value):
    if len(value) <= 1:
        return True
    first = 0
    last = len(value) - 1
    if value[first] == value[last]:
        return palidrome(value[first + 1:last])
    return False


def cross_sum(value):
    if value < 10:
        return value
    last_digit = value % 10
    return last_digit + cross_sum(value // 10)


def reverse_string_simple(input):
    return input[::-1]


def reverse_string(input):
    first = input[0]
    remainder = input[1:]
    return reverse_string(remainder) + first

def list_sum(input):
    return list_sum_helper(input, 0)


def list_sum_helper(input, pos):
    if pos >= len(input):
        return 0
    return input[0] + list_sum_helper(input, pos + 1)