str=input("enter the string")
print("string is",str)
count={}
for x in str:
    if x in count.keys():
        count[x]+=1
    else:
        count[x]=1
print(count)    








# d= {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# dict={}
# for i in d.values():
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict) 


# a= {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}


# a={'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# for i in a:
#     for j in a:
#         if a[i]>a[j]:
#             a[i]=a[j]
#             print(i)
        
        
# a= {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
# b=[]
# for i,j in a.items():
#     if len(j)<=1:
#        b.append(i)
# print(b)

        
        
       