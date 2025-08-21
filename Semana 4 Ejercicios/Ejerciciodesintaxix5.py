counter = 0
counter += 1
grade_counter = 1
total_approved_grades = 0
total_failed_grades = 0
average_approved_grades = 0
average_failed_grades = 0
total_grades_average = 0
sum_of_grades = 0
sum_of_approved_grades = 0
sum_of_failed_grades = 0


total_grades = int(input("Ingrese la cantidad de notas"))

while (grade_counter <= total_grades):
    print("Ingrese la nota número")
    print({grade_counter})
    grade_counter = grade_counter + 1
    current_grade = int(input("Ingrese la nota"))

    sum_of_grades += current_grade

    if (current_grade < 70):
        total_failed_grades = total_failed_grades + 1
        sum_of_failed_grades += current_grade
        average_failed_grades = (sum_of_failed_grades / total_failed_grades)

    else:
        total_approved_grades = total_approved_grades + 1
        sum_of_approved_grades += current_grade
        average_approved_grades = (sum_of_approved_grades / total_approved_grades)


total_grades_average = sum_of_grades / total_grades


if total_approved_grades == 0:
    print("No hay notas aprobadas")
else:    
    print("El estudiante tiene esta cantidad de notas aprobadas")
    print(total_approved_grades)
    print("Este es el promedio de notas aprobadas")
    print(average_approved_grades)

if total_failed_grades == 0:
    print("No hay notas desaprobadas")
else:    
    print("El estudiante tiene esta cantidad de notas desaprobadas")
    print(total_failed_grades)
    print("Este es el promedio de notas desaprobadas")
    print(average_failed_grades)

print("Este es el promedio total de notas")
print(total_grades_average)