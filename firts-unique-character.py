# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.
a='alphabet'
b='barbados'
c='crruunnchhyy'
from collections import Counter
def nn(sr):
    d=Counter(sr)
    for i,stringg in enumerate(sr):
        if d[stringg]==1:
            return i
    return -1
#print(nn(b))

def n1(s):
    frequency = {}
    for i in s:
        if i not in frequency:
            frequency[i]=1
        else:
            frequency[i]+=1
    for i in range(len(s)):
        if frequency[s[i]]==1:
            return i,frequency
    return -1
print(n1(a))