sample_dict ={
    "name":"sumit",
    "age":25,
    "salary":8000,
    "city":"delhi"

}

# print(sample_dict.keys());
# print(sample_dict.values())

keys = ["name","salary"]
new_dict = {}
for key in keys:
    new_dict[key] = sample_dict[key]

print(new_dict)
