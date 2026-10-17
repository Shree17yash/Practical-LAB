
num_students = int(input("Enter the number of students: "))

total_class_score = 0

for student in range(1, num_students + 1):
    print(f"\nStudent {student}")
    total_student_score = 0

    for test in range(1, 6):
        score = float(input(f"Enter score for test {test}: "))
        total_student_score += score

    average = total_student_score / 5
    print(f"Average score of Student {student}: {average:.2f}")

    total_class_score += total_student_score

# Calculate the overall class average
class_average = total_class_score / (num_students * 5)

print(f"\nOverall class average: {class_average:.2f}")
