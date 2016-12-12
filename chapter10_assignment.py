def sum_evens(list):
    """Find the sum of all the even numbers in a list."""
    evens = []
    for num in list:
        if num % 2 == 0:
            evens = evens + [num]
    added = sum(evens)
    return added
