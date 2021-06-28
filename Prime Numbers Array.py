# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

n = 11
def sol(num):
    ans=[]
    for i in range(num+1):
        if i>1:
            for j in range(2,i):
                if (i%j)==0:
                    break
            else:
                ans.append(i)
    return ans
print(sol(n))