# # packing and unpacking 

# x = (12,14,16)
# (a,b,c) =x;
# print(a);
# print(b);
# print(c);

# # del x 
# # # print(x);
# y = list(x);
# print(y)

# enumerate function 

ex =  ("ram","shyam")
for i,v in enumerate(ex):
    print(i,": ",v);



x = [12,1,445]
y = ["hello","java","python"]

for i,v in enumerate(y):
    x.insert(i+2,v)

print(x)