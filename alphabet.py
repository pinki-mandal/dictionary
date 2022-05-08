a={"A":[3,9,0,7],"B":[6,2,4,5]}
b={}
for x,y in a.items():
    s=[]
    a=" "
    if type(y)==list:
        a=x
        i=1
        while i<len(y)+1:
            s.append(y[-i])
            i+=1
            b.update({a:s})
print(b)            
    
