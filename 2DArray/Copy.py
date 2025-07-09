score = float(input("Enter the student's score (0-100): "))

if 90 <= score <= 100:
    print("The student's grade is: A")
elif 80 <= score <= 89:
    print("The student's grade is: B")
elif 70 <= score <= 79:
    print("The student's grade is: C")
elif 60 <= score <= 69:
    print("The student's grade is: D")
elif 50 <= score <= 59:
    print("The student's grade is: E")
elif 40 <= score <= 49:
    print("The student's grade is: E-")
elif 0 <= score < 40:
    print("The student's grade is: F (Fail)")
else:
    print("Invalid score. Please enter a value between 0 and 100.")
