# a={'key1': 1, 'key2': 3, 'key3': 2}
# b={'key1': 1, 'key2': 2}
# for i in a:
#     for j in b:
#         if i==j and a[i]==b[j]:
#             print(i,":",a[i])
    
    

a=[2,4,5,7] 
b={} 
sum=0
i=0
while i<len(a):
    sum+=a[i]
    b.update({i:sum})
    i+=1
print(b)



# city=input("enter the city name") 
# if city=="delhi":
#     print("red fort")
# elif city=="jaipur":
#     print("jal mahal")
# elif city=="agra":
#     print("taj mahal")
# else:
#     print("nothing")  

