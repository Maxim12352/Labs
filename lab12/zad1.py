import json

# Function to load a JSON file
def load_json(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data

# Function to save data to a JSON file
def save_to_json(filename, data):
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# Function to add a new student to the JSON file
def add_student(filename, student_data):
    data = load_json(filename)
    data['students'].append(student_data)
    save_to_json(filename, data)

# Function to find students by birth month
def find_students_by_month(filename, month):
    data = load_json(filename)
    matching_students = []

    for student in data['students']:
        if student['birth_date']['month'] == month:
            matching_students.append({
                "first_name": student["first_name"],
                "last_name": student['last_name']
            })

    return matching_students

# Main program
filename = 'File.json'
result_filename = 'result.json'

# 1. Display the content of the JSON file
data = load_json(filename)
print(json.dumps(data, indent=4))

# 2. Add a new record to the JSON file
new_student = {
    "last_name": "New",
    "first_name": "Student",
    "middle_name": "MiddleName3",
    "birth_date": {
        "year": 2002,
        "month": 6,
        "day": 25
    },
    "gender": "male"
}
add_student(filename, new_student)

# 3. Find data in the JSON file by birth month
while True:
    try:
        month_to_find = int(input("Enter the month number: "))
        if 1 <= month_to_find <= 12:
            break
        else:
            print("Please enter a valid month number (1-12).")
    except ValueError:
        print("Please enter a valid month number (1-12).")

matching_students = find_students_by_month(filename, month_to_find)

if matching_students:
    print(f"Students born in the month {month_to_find}:")
    for student in matching_students:
        print(f"{student['last_name']} {student['first_name']}")
else:
    print(f"No students born in the month {month_to_find}.")

# 4. Save the results to another JSON file
save_to_json(result_filename, {"matching_students": matching_students})
