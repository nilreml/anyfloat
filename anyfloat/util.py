def is_power_of_two(n: int) -> bool:
    """
    Return True iff integer n is a power of two.
    """
    return (n != 0) and (n & (n - 1) == 0)
