list1=["one","two","three","four"]
list2=[1,2,3,4,5,]
d={}
i=0
while i<len(list1):
    d[list1[i]]=list2[i]
    i=i+1
print(d)
