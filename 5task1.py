student_details={"Alice":70,"Mark":89,"bob":90,"charlie":80}
student_name=input("Enter student name: ")
if student_name in student_details:
    print(f"{student_name}'s marks are: {student_details[student_name]}")
else:
    print("Student not found in record.")