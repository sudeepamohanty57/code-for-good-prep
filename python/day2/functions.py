
# ------------------------------------------------
# 1. BASIC FUNCTION
# ------------------------------------------------

def greet():
    print("Hello! Welcome to Python.")


greet()


# ------------------------------------------------
# 2. FUNCTION WITH PARAMETER
# ------------------------------------------------

def greet_user(name):
    print("Hello", name)


greet_user("Sudeepa")
greet_user("Rahul")


# ------------------------------------------------
# 3. FUNCTION WITH RETURN VALUE
# ------------------------------------------------

def add(a, b):
    return a + b


result = add(10, 20)

print("Sum:", result)


# ------------------------------------------------
# 4. MULTIPLE PARAMETERS
# ------------------------------------------------

def calculate_average(a, b, c):
    return (a + b + c) / 3


average = calculate_average(80, 90, 85)

print("Average:", average)


# ------------------------------------------------
# 5. DEFAULT PARAMETER
# ------------------------------------------------

def greet_person(name="User"):
    return f"Hello, {name}!"


print(greet_person())
print(greet_person("Sudeepa"))


# ------------------------------------------------
# 6. FUNCTION WITH CONDITION
# ------------------------------------------------

def check_even(number):

    if number % 2 == 0:
        return True

    return False


print(check_even(10))
print(check_even(7))


# ------------------------------------------------
# 7. FUNCTION TO FIND MAXIMUM
# ------------------------------------------------

def find_max(numbers):

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


numbers = [10, 45, 23, 67, 12]

print("Maximum:", find_max(numbers))


# ------------------------------------------------
# 8. FUNCTION TO FILTER EVEN NUMBERS
# ------------------------------------------------

def get_even_numbers(numbers):

    even_numbers = []

    for number in numbers:

        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print("Even numbers:", get_even_numbers(numbers))


# ------------------------------------------------
# 9. FUNCTION USING LIST COMPREHENSION
# ------------------------------------------------

def square_even_numbers(numbers):

    return [
        number ** 2
        for number in numbers
        if number % 2 == 0
    ]


numbers = [1, 2, 3, 4, 5, 6]

print("Even squares:", square_even_numbers(numbers))


# ------------------------------------------------
# 10. FUNCTION WITH DICTIONARY
# ------------------------------------------------

def get_student_name(student):

    return student["name"]


student = {
    "name": "Sudeepa",
    "marks": 90
}

print("Student name:", get_student_name(student))


# ------------------------------------------------
# 11. FUNCTION TO CALCULATE GRADE
# ------------------------------------------------

def calculate_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 50:
        return "D"

    else:
        return "F"


print(calculate_grade(95))
print(calculate_grade(78))
print(calculate_grade(45))


# ------------------------------------------------
# 12. *ARGS
# ------------------------------------------------

def calculate_sum(*numbers):

    total = 0

    for number in numbers:
        total += number

    return total


print("Sum:", calculate_sum(10, 20))
print("Sum:", calculate_sum(10, 20, 30, 40))


# ------------------------------------------------
# 13. **KWARGS
# ------------------------------------------------

def display_student(**details):

    for key, value in details.items():
        print(key, ":", value)


display_student(
    name="Sudeepa",
    age=20,
    course="Data Science"
)


# ------------------------------------------------
# 14. LAMBDA FUNCTION
# ------------------------------------------------

square = lambda x: x ** 2

print("Square:", square(5))


# ------------------------------------------------
# 15. PRACTICAL FUNCTION
# ------------------------------------------------

def process_sales(sales):

    total = sum(sales)

    average = total / len(sales)

    high_sales = [
        sale
        for sale in sales
        if sale >= 1000
    ]

    return {
        "total": total,
        "average": average,
        "high_sales": high_sales
    }


sales = [500, 1200, 800, 2000, 1500]

result = process_sales(sales)

print("Sales analysis:", result)