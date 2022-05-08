# d={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# for i in d:
#     d[i].clear()
# print(d)    
    
    
str=input("enter the string")
print("string is",str)
count={}
for x in str:
    if str in count.items():
        count[x]+=1
    else:
        count=1
print(count)            
        
        
        
        