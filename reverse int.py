# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.
def sol(n):
    if eval(n)>=0:
        s=str(n)
        s1=s[::-1]
        return s1
    else:
        s=str(n)
        return int("-"+s[:0:-1])

print(sol("-123"))