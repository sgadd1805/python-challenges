def count_digits(value):
    if value < 10:
        return 1
    return count_digits(value // 10) + 1


def proper_divisor(value):
    result = [1]
    for i in range(2, value // 2 + 1):
        if value % i == 0:
            result.append(i)

    return result


def prime_numbers(value):
    for i in range(2, value // 2 + 1):
        if value % i == 0:
            return False
    return True


def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def factorial_rec(n):
    if n == 1:
        return 1
    return n * factorial_rec(n - 1)


factorial = lambda n: n if n == 1 else n * factorial(n - 1)

def to_binary(n):
    if n <= 1:
        return str(n)
    remainder, last_digit = divmod(n, 2)
    return to_binary(remainder) + str(last_digit)


def is_power_of_2(n):
    if n < 2:
        return n == 1
    if n % 2 != 0:
        return False
    return is_power_of_2(n // 2)

