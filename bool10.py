def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    import math
    x=math.sqrt(a)
    y=x==int(x)
    return y
print(main(121))