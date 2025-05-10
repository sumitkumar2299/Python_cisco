# dictionary = unordered collection of object 
# key should always be unique value 
x = {1:"hello",2:"java",3:"python"}
print(x);

# indexing, slicing is not applicable in dictionary

d = {}
# empty dictionary

d = {1:"sumit",2:"kumar",3:"xyz"}
print(d)
print(d[1])
print(len(d))
print(d.keys())
print(d.values())

for k,v in d.items():
    print(k,":",v)



x = {"a":10,"b":20}
x["l"] = list(range(5))
x["t"]  = tuple(sorted(range(9,16),reverse=True))
print(x)

for k,v in x.items():
    print(k,":",v)

x = {"a":10,"b":20}
x.update({"a":300})
x.update({"c":300})
print(x);

del x["a"]
print(x)

# if you want to delete the whole dictionary 

x = {"a":10,"b":20}
x.clear()
print(x);

# copy dictionary 
z = x.copy();
print(z);