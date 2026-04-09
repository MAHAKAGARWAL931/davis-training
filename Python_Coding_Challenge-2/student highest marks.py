# Define dictionary (student : marks)
marks = {"A": 80, "B": 95, "C": 78}

# Assume first student has highest marks
top_student = list(marks.keys())[0]

# Loop through dictionary
for student in marks:
    
    # Compare marks
    if marks[student] > marks[top_student]:
        top_student = student   # Update top student

# Display result
print("Top student =", top_student)