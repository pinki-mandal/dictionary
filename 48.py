a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
b={}
for i in a:
    k=len(a[i])
    b.update({a[i]:k})
print(b)    
    



