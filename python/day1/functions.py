items=[
    {'name':'Book','price':200, 'quantity': 2},
    {'name':'Pen','price':20,'quantity':5}
]

def calculate_bill(items):
    total=0
    for item in items:
        total+= item['price'] * item['quantity']
    return total

print(calculate_bill(items))
