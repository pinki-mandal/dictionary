num=int(input("enter the number"))
i=1
m={}
while i<num: 
    m.update({i:i*i})
    i=i+1
print(m)
    