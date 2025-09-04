from .students import amount_of_students

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

def top_3_averages():
    promedios = average_grades(amount_of_students)
    if not promedios:          # si aún no hay estudiantes
        return []
    # Ordena la LISTA completa por 'Promedio' (no cada diccionario por separado)
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

