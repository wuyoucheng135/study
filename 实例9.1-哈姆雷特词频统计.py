#calhamlettv1.py
def getText():
    txt = open('hamlet.txt','r').read()
    txt = txt.lower()
    for ch in "`~!@#$%^&*()_+-=[{]}\|;:',<.>/?":
        txt =txt.replace(ch,' ')
    return txt
hamlet=getText()
words=hamlet.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print('{}   {}'.format(word,count))