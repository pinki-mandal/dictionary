dic={"ball":"red","bat":4,"wicket":8,"ball":"green","bat":3}
m={}
for i in dic:
    if i not in m:
        m.update({i:dic[i]})
print(m)

# dic=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# m={}
# for i in dic:
#     if i not in m:
#         m.update({i:dic[i]})
# print(m)        

