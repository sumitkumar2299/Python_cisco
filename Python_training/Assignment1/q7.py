# entering marks of 5 subjects and calculate, total and average and percentage 

total_marks = 0;

for i in range(1,6):
    print(f"marks in subject {i} is")
    marks = int(input(":"))
    total_marks = total_marks+marks;
print(f"Total marks obtained is:{total_marks}")

obtained_marks = 100*i;
average = total_marks/i;
print(average);

percentage = (total_marks/obtained_marks)*100;
print(percentage)







    

