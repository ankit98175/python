# -----------------------------------------task 1 -------------------------------------------------->

student_dict ={
    input("enter the name of student 1: "): int(input("enter the marks of student 1: ")),
    input("enter the name of student 2: "): int(input("enter the marks of student 2: ")),
    
}
missing_student = input("Enter the name of the student: ")
if missing_student not in student_dict:
    print(f"{missing_student} name not found.")
else:
    print("Student Marks Dictionary:", student_dict)


# ---------------------------------------------task 2 -------------------------------------------------->
My_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", My_list)
Extracted_list = My_list[0:5]
print("Extracted List:", Extracted_list)
reversed_list = Extracted_list[::-1]
print("Reversed List:", reversed_list)