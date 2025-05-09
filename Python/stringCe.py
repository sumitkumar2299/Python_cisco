# f string 
name = "john"
age = 30
print(f"my name is {name} and i am {age} years old")

# format strings in python 

name = "sumit"
age = 30
print("my name is {} and i am {} years old.".format(name,age))


# f string 
name = "john"
age = 30
print(f"my name is {name} and i am {age} years old")


x = 10
y = 20
print(f"The sum of x and y is {x+y}.")

# indexing of an string 
name = "the bodyguard"
print(name[0])
print (name[1])
print(name[11])


# negative indexing 
name = "the bodyguard"
print(name[-1])
print(name[-5])
print(name[-7])



# slicing of an array 
# starting from zero you have to exclude 3rd elements 
name = "sumit kumar"
print(name[0:3])
print(name[5:8])

# stride of an string 
name = "sumit kumar"
print(name[:2])
print(name[::2])
print(name[0:5:2])


# concatenate string 
name = "sumit kumar"
statement = name + " is learning python that helps us in data science"
z = 3*statement
print(z)
print(statement);

# string manipulation 
name = "sumit kumar"
print("before uppercase",name)
b = name.upper();
print("after uppercase",b)

# replacing the old substring with a new target substrings 

x = name.replace('kumar','yadav')
print(x)

# now i want to replace a whole string how can i do this 

# y = name.replace('xyz yadav','name')
# print(y)

# name = "xyzw"
# print(name)


# find methods 

name = "sumit kumar"
# answer will be 6 k start in kumar at sixth position 
name.find('kumar')


#  if substring is not in your string 
name.find("yadav")
# it directly give -1 as an answer but you have to think why it gives -1  (because of -1 is the last elements of an string) 



# string manipulation 
name = "sumit kumar"
print("before uppercase",name)
b = name.upper();
print("after uppercase",b)

# replacing the old substring with a new target substrings 

x = name.replace('kumar','yadav')
print(x)

# now i want to replace a whole string how can i do this 

# y = name.replace('xyz yadav','name')
# print(y)

# name = "xyzw"
# print(name)


# find methods 

name = "sumit kumar"
# answer will be 6 k start in kumar at sixth position 
name.find('kumar')


#  if substring is not in your string 
name.find("yadav")
# it directly give -1 as an answer but you have to think why it gives -1  (because of -1 is the last elements of an string) 


# string manipulation 
name = "sumit kumar"
print("before uppercase",name)
b = name.upper();
print("after uppercase",b)

# replacing the old substring with a new target substrings 

x = name.replace('kumar','yadav')
print(x)

# now i want to replace a whole string how can i do this 

# y = name.replace('xyz yadav','name')
# print(y)

# name = "xyzw"
# print(name)


# find methods 

name = "sumit kumar"
# answer will be 6 k start in kumar at sixth position 
name.find('kumar')


#  if substring is not in your string 
name.find("yadav")
# it directly give -1 as an answer but you have to think why it gives -1  (because of -1 is the last elements of an string) 

# split method in string 
# it returns a list 

name = "sumit kumar"
split_string = (name.split())
print(split_string)


# learning regex 
import re
s1 = "i am a dataScience learner"
# define the pattern to search for
pattern = r"data"
# use the search function to search for the pattern in the string
result = re.search(pattern,s1)

# check if the match was found

if result:
    print("match found")
else:
    print("match not found")



import re
pattern = r"\d\d\d\d\d\d"
# matches any consecutive digit 

text = "my phone number is 123456"
match = re.search(pattern,text)
if match:
    print("phone number not found",match.group())
    # The match.group() method is used in Python's re module to retrieve the part of the string where the regular expression pattern matched.
else:
    print("No match")


s2 = 'The bodyGuard is the best album of "whitney houston"'
# use the findall() function to find all occurence of "st" in the string
result = re.findall("st",s2)

# print out the list of matched words 
print(result)



# use the string function to split the string by the \s
s3 = "i am sumit kumar"
split_array = re.split(r"\s",s3)
print(split_array)


# The sub function of a regular expression in Python is used to replace all occurrences of a pattern in a string with a specified replacement.

pattern = r"sumit kumar"
replacement = "legend"
new_string = re.sub(pattern,replacement,s3,flags=re.IGNORECASE)
print(new_string)
