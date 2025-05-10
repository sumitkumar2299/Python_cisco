x = ["M","Na","i","r"]
y = ["y","me","s","am"]

z = [i+j for i,j in zip(x,y)]
print(z)



# filter function 

list1 =["amit","rahul","sumit","",""]
y = list(filter(None,list1))
print(y);



# list comprehension 
# old list se new list bana sakte hai 

x = [1,2,3,4]
y = []

for i in x:
    y.append(i*2);

print(y)


# another way of doing this 

x1 = [1,2,3,4]
y1 = [i*2 for i in x]
print(y1)



x  = [i for i in range(20) if i%2==0]
print(x)


x2 = "sumit"
y2 = "aeiou"

z2 = [i for i in x2 if i in y2]
print(z2)

