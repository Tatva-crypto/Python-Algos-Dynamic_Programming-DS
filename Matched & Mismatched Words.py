#Given two sentences, return an array that has the words that appear in one sentence and not
#the other and an array with the words in common.

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

def sol(s1,s2):
    t1=set(s1.split())
    t2=set(s2.split())
    return sorted(list(t1^t2)),sorted(list(t1&t2))
print(sol(sentence1,sentence2))