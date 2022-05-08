a={"a":3,"b":5}
b={}
for i in a:
    b.update(a)
    print({a[i]:i})