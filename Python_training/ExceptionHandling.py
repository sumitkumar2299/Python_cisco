# try ke sath except block ka use karna hai 

# try,catch and block are the three keyword 

while True:
    try:
        x = int(input("enter a number:"))
        print(x)
        break
    except ValueError as v:
        print(v)






# io error

try:
    f = open("stp_25.txt")
    s = f.readline()
    i = int(s.strip())
except IOError as i:
    print("io error",i)
except ValueError as v:
    print("value error",v)
except:
    print("unexpected error")