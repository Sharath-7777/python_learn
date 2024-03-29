dt={"a":1,"b":2}
for key,value in dt.items():
    print(key,value)
    #update  delete #get
dt2={"c":3,"d":4}
dt.update(dt2)
print(dt)

dt.pop("a")
print(dt)

del dt["d"]
print(dt)

k=dt.get("b")
print(k)
print(dt["b"])











