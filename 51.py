a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1,7,8,7]}   
for i,k in a.items():
    for j in k:
        if j%2!=0:
            a[i].remove(j)
print(a)            

