#list
thislst= [4,5,2,6,1,5.3,"hi"]
print(thislst)
thislst.append(7)
print(thislst)
thislst.insert(1, 8)
print(thislst)
thislst.remove(5)
print(thislst)
thislst.reverse()
print(thislst)
thislst.extend("h")
print(thislst)


#dictionary

dit={"Name":"Raj", "Class":"Python", "Age":25}
print(dit)
x=dit.copy()
print(x)
print(dit.get("Name"))
print(dit.items())
print(dit.pop("Age"))
dit.update({"Name":"Arjun"})
print(dit)
