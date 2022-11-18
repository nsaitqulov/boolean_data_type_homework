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
    z=a==int(a)
    return x and y and z
print(main(1.999))