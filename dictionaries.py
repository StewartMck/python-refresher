students = {"John":16, "Mark":18, "Sally":19, "Peter":17}
overEighteen = []

for name, age in students.items():
    if age >= 18:
        overEighteen.append(name)


print('Students 18 or older:', overEighteen)

print("John is:", students["John"])

#Adding a student
students["Susan"] = 21
print(students)

#Removing a student
del(students["Peter"])
print(students)