
students = {
    "liam": 14,
    "Andy": 12,
    "Amy": 17,
    "Ellie": 22
}

print(students["Andy"])

students["Bob"] = 13
print(len(students))
print(students)
print(students.keys())
print(students.values())

names = {
    "Damien": 33,
    "Elle": 12,
    "Kristian": 24
}

students.update(names)
print(students)