"""
Arithmetic operators +,-,*,/,%,**,//
Assignment operators =,+=,-=,*=,/=,//=,**=
Comparison operators ==,!=,>,<,>=,<=
Logical operators     and, or, not
Identity operators     is, is not
Membership operators   in , not in
"""

# Arithmetic operators
print('Arithmetic operators')
print(5+7)

# Assignment operators
a = 5
a += 2
print('Assignment operators')
print(a)

# Comparison operators
a = 10
print('Comparison operators')
print(a >= 8)

# Logical operators  ----   and, or, not
print('Logical operators')
print(5 > 10 or 5 < 10)

# Identity operators     is, is not
print('Identity operators')
a = ["apple", "banana"]
c = a

print(c is a)

# Membership operators   in , not in
print('mbership operators')
a = ["apple", "banana"]
print("banana" in a)
