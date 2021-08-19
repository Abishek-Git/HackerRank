"""
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.


"""


total = int(input())
data = []
points = []
for i in range(total):
    name = input()
    grade = float(input())
    data += [[name, grade]]
    points.append(grade)

points.sort()

temp = 0
for i in points:
    if(float(i) > float(points[0])):
        temp = float(i)
        break

final_list = []
for item in data:
    if(float(item[1]) == temp):
        final_list.append(item[0])


final_list.sort()
for itm in final_list:
    print(itm)
