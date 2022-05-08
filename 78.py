# a={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# b=[]
# for i in a:
#     b.append(i)
# print(b)




# a={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# b=[]
# for i in a:
#     b.append(a[i])
# print(b)  





a={'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}   
list1=[]
for x in a.values():
    list1.append(x)
min=list1[0]
max=0
for i in list1:
    if i<min:
        min=i
    if i>max:
        max=i
print("minimum value",min)
print("maximum value",max) 



# for x,y in a.items():
#     if y==min:
#         print(x,y)
#     if y==max:
#         print(x,y)
