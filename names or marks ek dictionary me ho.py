# {
#  'sonu':85,
#  'Kartik':90,
#  'Deepak':96,
#  'Aman':76,
#  'Somesh':60,
#  'Umesh':85,
#  'Amarpal':70,
#  'Roshan':57,
#  'Riyaz':98,
#  'Shabid':56
# }


n={}
for i in range(10):
    names=input("enter the number")
    marks=int(input("enter the number"))
    n.update({names:marks})
    print(n)    

