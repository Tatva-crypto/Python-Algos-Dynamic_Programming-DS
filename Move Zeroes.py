#Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
#the non-zero elements.

array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]

def sol(ar):
    for num,i in enumerate(ar):
        if i==0:
            ar.remove(i)
            ar.append(i)
    return ar
print(sol(array2))