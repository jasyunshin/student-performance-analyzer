# Name: Jason Shin
# Period: AM
# Student Performance Analyzer

# Introduce the program
print("========================================")
print("       STUDENT PERFORMANCE ANALYZER")
print("========================================")
print("\nEnter the student's information below.")

# Collect the student's information
student_name = input("Enter the student's name: ")
grade_level = int(input("Enter the student's grade level (1-12): "))
assignment_average = float(input("Enter the student's assignment average (0-100): "))
quiz_average = float(input("Enter the student's quiz average (0-100): "))
test_average = float(input("Enter the student's test average (0-100): "))
attendance_percentage = float(input("Enter the student's attendance percentage (0-100): "))
missing_assignments = int(input("Enter the number of missing assignments: "))


# Calculate the weighted overall grade
def calculate_grade(assignment_average, quiz_average, test_average):
    assignment_portion = assignment_average * 0.3
    quiz_portion = quiz_average * 0.3
    test_portion = test_average * 0.4

    overall_grade = assignment_portion + quiz_portion + test_portion
    print(f"\nOverall Grade: {overall_grade:.1f}")
    return overall_grade


# Determine the letter grade
def letter_grade(overall_grade):
    if overall_grade >= 90:
        return "A"
    elif overall_grade >= 80:
        return "B"
    elif overall_grade >= 70:
        return "C"
    elif overall_grade >= 60:
        return "D"
    else:
        return "F"


# Determine the attendance status
def attendance_status(attendance):
    if attendance >= 95:
        return "Attendance Status: Excellent Attendance"
    elif attendance >= 90:
        return "Attendance Status: Good Attendance"
    elif attendance >= 80:
        return "Attendance Status: Attendance Warning"
    else:
        return "Attendance Status: Poor Attendance"


# Check how many assignments the student is missing
def assignment_status(missing_assignments):
    if missing_assignments == 0:
        return "Missing Assignment Status: Excellent"
    elif missing_assignments <= 2:
        return "Missing Assignment Status: Good"
    elif missing_assignments <= 4:
        return "Missing Assignment Status: Warning"
    else:
        return "Missing Assignment Status: Critical"


# Check all three academic eligibility requirements in order
def check_eligibility(overall_grade, attendance, missing_assignments):
    if overall_grade >= 70:
        if attendance >= 90:
            if missing_assignments <= 2:
                return "Academic Eligibility: ELIGIBLE\nStudent passed all three requirements."
            else:
                return "Academic Eligibility: NOT ELIGIBLE\nReason: Too many missing assignments."
        else:
            return "Academic Eligibility: NOT ELIGIBLE\nReason: Attendance is too low."
    else:
        return "Academic Eligibility: NOT ELIGIBLE\nReason: Overall grade is too low."


# Check the stricter requirements for high honors
def check_high_honors(overall_grade, attendance, missing_assignments):
    if overall_grade >= 90:
        if attendance >= 95:
            if missing_assignments == 0:
                return "High Honors: YES"
            else:
                return "High Honors: NO\nReason: Student has missing assignments."
        else:
            return "High Honors: NO\nReason: Attendance requirement not met."
    else:
        return "High Honors: NO\nReason: Grade requirement not met."


# Good standing requires both a passing grade and enough attendance
def check_good_standing(overall_grade, attendance):
    if overall_grade >= 70 and attendance >= 90:
        return "Good Standing: YES"
    else:
        return "Good Standing: NO"


# Either a low grade or very low attendance recommends support
def check_support(overall_grade, attendance):
    if overall_grade < 70 or attendance < 80:
        return "Additional Support: RECOMMENDED"
    else:
        return "Additional Support: NOT NEEDED"


# Give a message based on the student's grade level
def grade_level_message(grade_level):
    if grade_level == 9:
        return "Welcome to your freshman year!"
    elif grade_level == 10:
        return "Keep building your skills!"
    elif grade_level == 11:
        return "Junior year — keep pushing!"
    elif grade_level == 12:
        return "Senior year — finish strong!"
    else:
        return "Invalid grade level."


# Compare the three averages to find the strongest category
def strongest_category(assignment_average, quiz_average, test_average):
    if assignment_average >= quiz_average:
        if assignment_average >= test_average:
            return "Strongest Category: Assignments"
        else:
            return "Strongest Category: Tests"
    elif quiz_average >= test_average:
        return "Strongest Category: Quizzes"
    else:
        return "Strongest Category: Tests"


# Check the optional advanced student status
def check_advanced_status(overall_grade, attendance, missing_assignments):
    if (overall_grade >= 90 and attendance >= 95) or (overall_grade >= 85 and missing_assignments == 0):
        return "Advanced Status: OUTSTANDING STUDENT"
    else:
        return "Advanced Status: STANDARD STUDENT STATUS"


# Calculate the grade once and save it for the other functions
overall_grade = calculate_grade(assignment_average, quiz_average, test_average)

# Display the results from each function
print(f"Letter Grade: {letter_grade(overall_grade)}")
print(attendance_status(attendance_percentage))
print(assignment_status(missing_assignments))
print(check_eligibility(overall_grade, attendance_percentage, missing_assignments))
print(check_high_honors(overall_grade, attendance_percentage, missing_assignments))
print(check_good_standing(overall_grade, attendance_percentage))
print(check_support(overall_grade, attendance_percentage))
print(grade_level_message(grade_level))
print(strongest_category(assignment_average, quiz_average, test_average))

# Ask for the login information
print("\nStudent Login")
username = input("Enter username: ")
pin = input("Enter PIN: ")

# Check the username first, then check the PIN
if username == "student":
    if pin == "1234":
        print("Login Successful!")
    else:
        print("Login Failed: Incorrect PIN.")
else:
    print("Login Failed: Incorrect username.")

# Display an organized summary at the end
print("\n========================================")
print("            STUDENT SUMMARY")
print("========================================")
print(f"\nStudent: {student_name}")
print(f"Grade Level: {grade_level}")
print(f"\nAssignment Average: {assignment_average:.1f}")
print(f"Quiz Average: {quiz_average:.1f}")
print(f"Test Average: {test_average:.1f}")
print(f"\nOverall Grade: {overall_grade:.1f}")
print(f"Attendance: {attendance_percentage:.1f}")
print(f"Missing Assignments: {missing_assignments}")
print(check_advanced_status(overall_grade, attendance_percentage, missing_assignments))
print("\n========================================")