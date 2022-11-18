def main(a):
    """Check the natural number.Natural numbers are numbers used in counting.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    x=a>0
    y=a==int(a)
    return x and y
print(main(7))