def sort_words(words):
    # Write your code here
    d = {}
    for w in words:
        sum = 0
        for s in w:
            sum = sum + (ord(s)-96)
            
        d[sum*3] = w
    
    kk = list(d.keys())
    kk.sort()
    d1 = {i:d[i] for i in kk}
    return d1.values()
            

print(sort_words(['ab', 'bz', 'aa']))