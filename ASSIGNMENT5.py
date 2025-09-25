#TASK 1

print("\n Task 1\n")



stu_marksheet={
    "rajnish": 95,
    "rahul": 82,
    "rohit": 70,
    "mohit": 65,
    "raunak": 85
}

name=input("Enter the name of the student:")

if name in stu_marksheet:  
    marks=stu_marksheet[name]
    print(f"marks of {name} is {marks}")

else:
    print("Student not found")



#TASK 2

print("\n Task 2\n")   

numbers=list(range(1,11))
print("original list:",numbers)

extrac_numbers=numbers[:5]
print("Extracted first five elements:",extrac_numbers)

reversed_numbers=extrac_numbers[::-1]
print("Reversed extracted elements:",reversed_numbers)
