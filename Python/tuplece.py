tuple1 = ("sumit",1,2);
print(tuple1)
print(type(tuple1));


# indexing of a tuple 

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])


# printing the type of value of each index 
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

# getting the value of the last element of a tuple

print(tuple1[-1]);

# getting the value of the second last element of a tuple

print(tuple1[-2]);
print(tuple1[-3]);


# concatenation of tuples (+)

tuple2 = tuple1+("kumar",1,2,3)
print(tuple2)


# slicing of a tuple
tuple3 = ("sumit","kumar",1234,"abcd");
# slice from index 0 to 2
ex = tuple3[0:3]
print(ex);
ex1 = tuple3[1:3]
print(ex1)

# getting the length of a tuple 
print(len(tuple3))


# sorting of a tuple 
rating = (0,1,2,3,44,5,6,7,8,9,-1)

rating_sorted = sorted(rating)
print(rating_sorted);


# creating nested tuple 

Nested_tuples = (1,2,("sumit","kumar"),(3,4),5)
print(Nested_tuples);
print(Nested_tuples[0])
print(Nested_tuples[1])
print(Nested_tuples[2])
print(Nested_tuples[3])
print(Nested_tuples[4])

# print the second element in the second nested tuples 
