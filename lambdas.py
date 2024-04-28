from functools import reduce

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
# doubled will be [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# even_numbers will be [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
# sum_of_numbers will be 15

# cmp_to_key(): Convert a comparison function to a key function.
# lru_cache(): Least-recently-used cache decorator.
# total_ordering(): Class decorator that fills in missing ordering methods.
# partial(): Return a new partial object which when called will behave like func called with the positional arguments args and keyword arguments keywords.
# partialmethod(): Return a new partialmethod descriptor which behaves like partial except that it is designed to be used as a method definition rather than being directly callable.
# reduce(): Apply a function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value.
# singledispatch(): Transform a function into a single-dispatch generic function.
# singledispatchmethod(): Transform a method into a single-dispatch generic method.
# update_wrapper(): Update a wrapper function to look like the wrapped function.
# wraps(): Decorator factory to apply update_wrapper() to a wrapper function.