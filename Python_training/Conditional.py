x = 100
if(x<20):
    print("python")
else:
    print("value not matched");

marks = int(input("enter your marks"));

if(marks>90):
    print('a++')
elif(marks>=80):
    print("b")
elif(marks>=70):
    print("c");
else:
    print("you guys are fail")


# nested if 


age = int(input("enter your age"));
if(age>30):
    salary = int(input("enter salary: "))
    if(salary>80000):
        print("3 year experience")
    else:
        print("no experience");
else:
    print("student")



# my approach

year = int(input("enter your year"));
if(year%4==0 and year%100 == 0):
    print("leap year")
else:
    print("not a leap year");



unit = int(input("enter your input"));
if(unit<50 and unit>0):
    print("charge is :",0.5*unit)
elif(unit>50 and unit<150):
    print("charge is ",0.75*unit)
elif(unit>150 and unit<250):
    print("charge is ",1.20*unit)













