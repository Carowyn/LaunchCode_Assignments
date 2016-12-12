def is_prime(num):
    """Takes a single integer argument (n) and checks whether the integer is prime."""
    div = 2                        # divided by
    for i in range(num):
        while div < num:           # while divided by is less than number
            if num % div == 0:
                return False
            else:
                div = div + 1

    return True