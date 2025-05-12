def show():
    print("hello ")
    print("sumit")

show()


def show1():
    x = 5
    y = 10
    z = x+y
    print(z)

show1()



# local and global variable 
x = 10

def show():
    y = 20
    print(x)

def put():
    z = 30
    print(x)


x = 10
def show():
    global x
    x = 0
show()
if(x==0):
    print("hello")
else:
    print("python")
show();


# positional argument
def show(x,y,z):
    print(x,y,z)

show(12,45,58)


# default argument 


def show(x,y=5,z=90):
    print(x,y,z)

# show(12)
# # it's mandatory to pass one argument 
show(12,60)



# keyword argument 

def show(x,y,z):
    print(x,y,z)
show(z=20,x=30,y=40)

# print in x,y,z respectively 







# arbitrary argument 
# data in the form of list 
# to pass the multiple arguments (you don't know how much argument will be passed)

def show(*x):
    for i in x:
        print(i)

show(1,2,3,4,5)
show(2,3,4)
show(58)




# ** these are also abitrary arguments 
# shows results in the form of dictionary.
def show(**x):
    for k in x.keys():
        print(k,":",x[k])
show(a = "sumit", b="kumar",c="python")










def show():
    def put():
        print("hello")
    put();
show()



def show():
    print("hello")

def put():
    print("sumit")
    show()
put()



# return keyword 
# you need not to print the statement when you are returning a function.

def show(x,y):
    z = x+y
    return z

print(show(3,5))



# database -> mysql
