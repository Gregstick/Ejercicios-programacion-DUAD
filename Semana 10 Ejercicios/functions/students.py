def students():
    amount_of_students = []
    while True:
        name = str(input("Ingrese el nombre del estudiante: "))
        section = input("Ingrese la sección (Ejemplo 11B): ")
        
        while True:
            try:
                spanish_grade = int(input("Ingrese la nota de Español: "))
                if 0 <= spanish_grade <= 100:
                    break
                else:
                    print("La número debe estar entre 0 y 100")
            except ValueError:
                print("Ingrese un número válido")
        while True:    
            try:
                english_grade = int(input("Ingrese la nota de Inglés: "))
                if 0 <= english_grade <= 100:
                    break
                else:
                    print("La número debe estar entre 0 y 100")
            except ValueError:
                print("Ingrese un número válido")
    
        while True:    
            try:    
                social_studies_grade = int(input("Ingrese la nota de Sociales: "))
                if 0 <= social_studies_grade <= 100:
                    break
                else:
                    print("La número debe estar entre 0 y 100")
            except ValueError:
                print("Ingrese un número válido")
    
        while True:
            try:
                science_grade = int(input("Ingrese la nota de Ciencias: "))
                if 0 <= science_grade <= 100:
                    break
                else:
                    print("La número debe estar entre 0 y 100")
            except ValueError:
                print("Ingrese un número válido del 0 al 100")
            continue

        students_grades = {
            'Nombre' : name,
            'Sección' : section,
            'Nota de Español' : spanish_grade,
            'Nota de Inglés' : english_grade,
            'Nota de Sociales' : social_studies_grade,
            'Nota de Ciencias' : science_grade,
        }
        
        
        amount_of_students.append(students_grades)
        print(amount_of_students)

        
        print(
            " 1.Quiero ingresar otro estudiante\n",
            "2.Volver al Menú principal"
            )
        yes_or_menu = int(input("Ingresa la opción que quieres ejecutar: "))
        if yes_or_menu == 1:
            continue
        else: 
            yes_or_menu == 2
            break

    return amount_of_students


def total_entered_students(students_list):
    for student in students_list:
        print(student)


def average_grades(students_list):
    averages = []
    for student in students_list:
        grades = [
            student['Nota de Español'],
            student['Nota de Inglés'],
            student['Nota de Sociales'],
            student['Nota de Ciencias']
        ]

        average_student_grades = sum(grades) / len(grades)
        averages.append({
            "Nombre" : student['Nombre'],
            "Promedio" : average_student_grades
        })
    return averages

def top_3_average(student_list):
    if not student_list:         
        return []
    promedios = average_grades(student_list)
    promedios_ordenados = sorted(promedios, key=lambda x: x["Promedio"], reverse=True)
    return promedios_ordenados[:3]

def sum_all_averages(student_list):
    sum_of_averages = []
    for student in student_list:
        grades = [
            student['Nota de Español'],
            student['Nota de Inglés'],
            student['Nota de Sociales'],
            student['Nota de Ciencias']
        ]

        average_student_grades = sum(grades) / len(grades)
        sum_of_averages.append(average_student_grades)
        sum_averages = sum(sum_of_averages) / len(sum_of_averages)
    return sum_averages