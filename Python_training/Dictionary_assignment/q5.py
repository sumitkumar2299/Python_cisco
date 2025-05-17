sample_dict = {
    "name": "Ram",
    "age": 25,
    "salary": 8000,
    "city": "Delhi"
    }

# Keys to extract
keys = ["name", "salary"]


# by using list comprehension 

dict_after_deletion = {k:v for k, v in sample_dict.items() if k not in keys}
print(dict_after_deletion)


