# Define the student's name
student_name = "Sam"

# Define the grades for various subjects
math_grade = 88
science_grade = 75
english_grade = 90
geology_grade = 69

# Calculate the total grade by summing all subject grades
total_grade = math_grade + science_grade + english_grade + geology_grade

# Define the maximum grade possible
max_grade = 400

# Calculate the total percentage based on the total grade and maximum grade
total_percentage = total_grade / max_grade * 100

# Print the student's total percentage
print(f"Sam's total percentage is {total_percentage}%")

# Convert the total percentage to an integer
total_percentage = int(total_percentage)

# Check if the student passed (total percentage is greater than or equal to 50)
did_student_pass = total_percentage >= 50

# Define if the student participated in sporting activities (assumed not participating)
sporting_activities = bool(0)

# Print whether the student participated in sporting activities
print(f"Sam participated in sporting activities: {sporting_activities}")

# Print the student's total percentage as an integer
print(f"Sam's total percentage as an integer is {total_percentage}%")

# Print whether the student passed to the next semester
print(f"Sam passed to the next semester: {did_student_pass}")
