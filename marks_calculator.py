
# Student Marks Calculator

name = input("Enter student name: ")
n = int(input("How many subjects? "))

marks = []
for i in range(n):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

total = sum(marks)
average = total / n

if average >= 90:
    grade = "O"
elif average >= 80:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
else:
    grade = "C"

print(f"\nStudent: {name}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")