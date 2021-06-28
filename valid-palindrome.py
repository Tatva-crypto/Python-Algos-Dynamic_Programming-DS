# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

s = 'radkar'

def S(s):

    for i in list(s):
        temp = list(s)
        temp.remove(i)
        if is_palindrome(temp):
            return "".join(temp)

def is_palindrome(l):
    s="".join(l)
    if s[::-1]==s:
        return 1
    else:
        print(s+" -->"+"Its not palindrome")

#print(S(s))
#a=[1,2,3]
#print(a[0:0])
s="abca"
def sorrr(s):
    for i in range(len(s)):
        t=s[:i]+s[i+1:]
        if t==t[::-1]:return True
    return s==s[::-1]

print(sorrr(s))