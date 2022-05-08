dic={"ball":"red","bat":4,"wicket":8,"ball":"green","bat":3}
m={}
for i in dic:
    if i not in dic:
        m.update(dic)
a=dic
print("List After removing duplicates ",a)
