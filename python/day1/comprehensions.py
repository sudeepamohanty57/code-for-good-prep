numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Square_of_even_num(numbers):
    even_square=[x**2 for x in numbers if x%2==0]
    return even_square

print("list of squares of even numbers:", Square_of_even_num(numbers))