def main(a):
    """
    check the whole number. Integers are 0 and a positive number.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    x=a>=0
    y=a<10
    return x and y
print(main(3))