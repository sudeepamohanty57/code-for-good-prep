
# ------------------------------------------------
# 1. LIST COMPREHENSION
# ------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [x ** 2 for x in numbers]

print("Squares:", squares)


# ------------------------------------------------
# 2. LIST COMPREHENSION WITH CONDITION
# ------------------------------------------------

even_numbers = [x for x in numbers if x % 2 == 0]

print("Even numbers:", even_numbers)


# ------------------------------------------------
# 3. SQUARES OF EVEN NUMBERS
# ------------------------------------------------

even_squares = [x ** 2 for x in numbers if x % 2 == 0]

print("Squares of even numbers:", even_squares)


# ------------------------------------------------
# 4. FILTER NUMBERS GREATER THAN 5
# ------------------------------------------------

greater_than_five = [x for x in numbers if x > 5]

print("Numbers greater than 5:", greater_than_five)


# ------------------------------------------------
# 5. STRING COMPREHENSION
# ------------------------------------------------

names = ["sudeepa", "rahul", "ananya", "rohit"]

uppercase_names = [name.upper() for name in names]

print("Uppercase names:", uppercase_names)


# ------------------------------------------------
# 6. DICTIONARY COMPREHENSION
# ------------------------------------------------

numbers = [1, 2, 3, 4, 5]

square_dict = {x: x ** 2 for x in numbers}

print("Square dictionary:", square_dict)


# ------------------------------------------------
# 7. DICTIONARY COMPREHENSION WITH CONDITION
# ------------------------------------------------

even_square_dict = {
    x: x ** 2
    for x in numbers
    if x % 2 == 0
}

print("Even square dictionary:", even_square_dict)


# ------------------------------------------------
# 8. SET COMPREHENSION
# ------------------------------------------------

numbers = [1, 2, 2, 3, 3, 4, 5]

unique_squares = {x ** 2 for x in numbers}

print("Unique squares:", unique_squares)


# ------------------------------------------------
# 9. PRACTICAL EXAMPLE
# ------------------------------------------------

students = [
    {"name": "A", "marks": 85},
    {"name": "B", "marks": 62},
    {"name": "C", "marks": 91},
    {"name": "D", "marks": 45}
]

passed_students = [
    student["name"]
    for student in students
    if student["marks"] >= 50
]

print("Passed students:", passed_students)


# ------------------------------------------------
# 10. PRACTICAL DATA PROCESSING
# ------------------------------------------------

sales = [1200, 500, 3000, 750, 2200]

high_sales = [amount for amount in sales if amount >= 1000]

print("High sales:", high_sales)