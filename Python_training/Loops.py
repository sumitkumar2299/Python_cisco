# x = 1

# #  while ke andar sirf statement jata hai 
# while(x<=5):
#     print("hello")
#     x = x+1



num = 12345;
sum = 0
while(num!=0):
    remainder = num%10
    sum = sum*10+remainder
    num = num//10
    # if we use / this it will return float value 
print(sum)





# for i in "Hello":
#     print(i,end = " ")

for i in range(5):
    print(i,end = " ")


for i in range(10):
    if(i==50):
        print("python")
        break
else:
    print("java")







