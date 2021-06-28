# Given an array containing None values fill in the None values with most recent
# non None value in the array
from numpy import record

array1 = [None,2,3,None,None,5,None]

def sol(ar):
    k=[]
    recent=0
    for i in ar:
        if i!=None:
            k.append(i)
            recent=i
        if i==None:
            k.append(recent)
    return k
print(sol(array1))