# d1={"a":100,"b":200,"c":300}
# d2={"a":300,"b":200,"d":400}
# f={}
# for i in d1:
#     for j in d2:
#         if i==j:
#             sum=d1[i]+d2[j]
#             f.update({i:sum}) 
#         else:
#             f.update({i:d1[i]})  
#             f.update({j:d2[j]})        
# print(f)      




d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"d":400}
for i in d1:
    if i in d2:
        d2[i]=d2[i]+d1[i]
    else:
        d2[i]=d1[i]
print(d2)

