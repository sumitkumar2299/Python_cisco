# # # lists in python 

# # indexing in python 
# # index starts from zero 

List= ["sumit",7.0,1992]
print(List[0]);

# list can any dataType and also nested list 

list1 = ["sumit","rahul","xyz",["abc","def"],("A",1)];
print(list1)


# operation in list 

list2 = ["sumit","abc","def","ghi",5]

# list slicing 
# 5 will always be excluded 
x = list2[3:5];
print(x);



list = ["sumit","kumar",44,7.0,]
print(list);

# use append to add element in the list 

list.append('sumit1');
print(list);

# if i have to add more than one element in the list?
y = list.append(["john","doe"]);
print(y);


# use extends to add elements in the list 

L = ["sumit_python",1.0];
L.extend(["pop",10]);
print(L);


# yeh nested list bana dega.
L.append(["pop",10]);
print(L)




# changing the element based on the index 

A = ["sumit",10,1.2]
print("before change",A);
A[0] = "kumar";
print("after change",A);

# Deleting element based on their index 

print("before deleting the element",A);
del(A[0])
print("after deletion of an element",A);


# most important -> copy and clone in the list 



# follow hitesh sir lecture 




# list practice 

fruits = ["apple","banana","orange"]
fruits.append("mango")
print(fruits);


my_list = [1,2,3,4,5]
new_list = my_list.copy()
print(new_list)


my_list = [1,2,3,4,5,6,6,7,6];
count = my_list.count(6)
print(count);


my_list = [10,20,30,40,50]
del my_list[2];
print(my_list);

