a={'c1': 'Red', 'c2': 'Green', 'c3': None}
b={}
for i in a:
    if a[i]==None:
        pass
    else:
        b.update({i:a[i]})
print(b)        
        
