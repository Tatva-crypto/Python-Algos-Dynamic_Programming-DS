# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def sor(s):
    for i in ",.!?:":
       sen= s.replace(i,'')
    word=sen.split()
    return round(sum(len(i) for i in word)/len(word),2)
print(sor(sentence2))