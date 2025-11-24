def main():
    students=[]
    while True:
        print("--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")
        choice=int(input("Enter your choice:"))

        if choice == 1:
            add_a_new_student(students)
        elif choice == 2:
            add_grades_for_a_student(students)
        elif choice == 3:
            generate_a_full_report(students)
        elif choice == 4:
            find_the_top_student(students)
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Enter a number between 1-5")

def add_a_new_student(students):
    name = input("Enter name students: ")
    for student in students:
        if student["name"] == name:
            print(f"Student '{name}' already exists")
            return
    students.append({
       "name": name,
       "grades": []
    })
    print(f"Student '{name}' added")

def add_grades_for_a_student(students):
    name = input("Enter student name:")
    student_found = None
    for student in students:
        if student["name"] == name:
            student_found = student
            break
    if not student_found:
            print(f"Student '{name}' not found")
            return
    print(f"Adding grades for {student_found['name']}. Enter grades in range 0-100 or 'done' to finish")
    while True:
        grade_input = input("Enter a grade (or 'done' to finish):")
        if grade_input == 'done':
            break
        try:
            grade = int(grade_input)
            if grade < 0 or grade > 100:
                print("Invalid grade. Enter a number between 0-100")
                continue

            student_found["grades"].append(grade)
            print(f"Grade {grade} added")
        except ValueError:
            print("Invalid input. Enter a number or 'done'")

def generate_a_full_report(students):
    if not students:
        print("No students")
        return
    print("--- Student Report ---")
    averages = []
    valid_students = 0
    total_sum = 0
    for student in students:
        name = student["name"]
        grades = student["grades"]
    try:
        average = sum(grades)/len(grades)
        averages.append(average)
        total_sum += average
        valid_students += 1
        print(f"{name}'s average grade is {average:}")
    except ZeroDivisionError:
        averages.append(None)
        print(f"{name}'s average grade is N/A")
    if valid_students > 0:
        valid_averages = [avg for avg in averages if avg is not None]
        if valid_averages:
            max_avg = max(valid_averages)
            min_avg = min(valid_averages)
            overall_avg = total_sum/valid_students
            print(f"Max Average: {max_avg:}")
            print(f"Min Average: {min_avg:}")
            print(f"Overall Average: {overall_avg:}")
        else:
            print("No student with available grades for statistics")

def find_the_top_student(students):
    students_with_grades = []
    for student in students:
        if student["grades"]:
            try:
                average = sum(student["grades"])/len(student["grades"])
                students_with_grades.append((student["name"], average))
            except ZeroDivisionError:
                continue

    top_student = max(students_with_grades, key=lambda x: x[1])
    print(f"The student with the highest average is {top_student[0]} with a grade of {top_student[1]:}")

if __name__ == "__main__":
    main()