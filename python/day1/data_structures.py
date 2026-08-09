students = [
    {"name": "A", "marks": 85},
    {"name": "B", "marks": 72},
    {"name": "C", "marks": 91},
    {"name": "D", "marks": 65}
]

def highest_marks(students):
    max_m=0
    for student in students:
        if student['marks']>max_m:
            max_m= student['marks']
    return max_m

print("Highest marks:", highest_marks(students))

def lowest_marks(students):
    min_m= students[0]['marks']
    for student in students:
        if student['marks']<min_m:
            min_m= student['marks']
    return min_m

print("Lowest marks:", lowest_marks(students))


def avg_marks(students):
    avg=0
    for student in students:
        avg=(avg+ student['marks'])/len(students)
    return avg

print("Average marks:", avg_marks(students))

def students_scoring_more_than_equal_to_80(students):
    lst=[]
    for student in students:
        if student['marks']>=80:
            lst.append(student['name'])
    return lst

print("Students scoring >=80:", students_scoring_more_than_equal_to_80(students))
