a={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
b={}
for i in a:
    for x in i: 
            k=i.replace(' ','',)
            for i,x in a.items():
                b.update({k:x})
print(b)                                     

# b={}
# for i in a:
#     for x in i:
#         k=i.replace(' ','',)
#         for i,x in a.items():
#             b.update({k:x})
# print(b)            

# b={}
# for i in a:
#     for x in i:
#         k=i.replace(' ','',)
#         for i,x in a.items():
#             b.update({k:x})
# print(b)            
    
