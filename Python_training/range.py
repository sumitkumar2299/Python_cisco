# range (5) -> start from 0 and stop n-1

# range(n,m) -> start n and stop m-1 
# range(1,10,2)-> start from 1 and stop 9 step-> 2


for i in range(5):
    print(i, end = " ")


for i in range(5,10):
    print(i, end = " ")

for i in range (10,5):
    print(i,end =" ")


for i in range(1,10,2):
    print(i, end = " ");


for i in range(5):
    if(i==2):
        print("record found")
        break
else:
    print("record not found");


for i in range(5):
    if(i==3):
        continue
    print(i,end= " ")



# pass statement 

for i in range(5):
    if(i==3):
        pass
else:
    print("pyhton");

for i in range(5):
    print(i,end = "----- ")



for j in range(5):
    print(j,sep = "----")


