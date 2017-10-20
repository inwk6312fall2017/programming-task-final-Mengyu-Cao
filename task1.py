import string
def biggestword(f1):
    fin=open(f1)
    listt=[]
    for line in fin:
        wordlist = line.strip()
        wordlist2 = wordlist.strip(string.punctuation)
        wordlist3 = wordlist2.split()
        for word in wordlist3:            
            listt.append(word)
        listt.sort()    
    return listt

def bigone(a,b,c):
    listt=[a,b,c]
    listt.sort()
    return listt[-1]

print (biggestword("Book1.txt"))
