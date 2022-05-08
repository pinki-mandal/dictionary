# b={}
# for i in range(20):
#     b.update({i:i})
# print(b)    

b={}
c=[]
m=[]
j=[]
for i in range(11,40):
    if i<20:
        c.append(i)
        b.update({"x":c})
    if i>20 and i<=29:
        m.append(i)
        b.update({"y":m})
    if i>30 and i<=40:
        j.append(i) 
        b.update({"z":j})    
print(b)  
for j in b:
    for k in b[j]:
        if k%5==0:
            print(k)
     
