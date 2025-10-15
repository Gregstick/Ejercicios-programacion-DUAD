class Student:
    def __init__(self, name, section, spanish_grade, english_grade, social_studies_grade, science_grade):
        self.name = name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_studies_grade = social_studies_grade
        self.science_grade = science_grade

    def grades(self):
        return[
            self.spanish_grade,
            self.english_grade,
            self.social_studies_grade,
            self.science_grade
        ]

    def average(self):
        grades = self.grades()
        return sum(grades) / len(grades)




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

        student = Student(name, section, spanish_grade, english_grade, social_studies_grade, science_grade)
        
        amount_of_students.append(student)
        print("\nLista actual de estudiantes ingresados:")
        for s in amount_of_students:
            print(f"{s.name} - Español: {s.spanish_grade}, Inglés: {s.english_grade}, Sociales: {s.social_studies_grade}, Ciencias: {s.science_grade}")

        
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
        print("\n".join(student.name for student in students_list))

def average_grades(students_list):
    averages = []
    for student in students_list:
        averages.append({
            "Nombre": student.name,
            "Promedio": student.average()
        })
    return averages

def top_3_average(student_list):
    if not student_list:         
        return []
    promedios = average_grades(student_list)
    promedios_ordenados = sorted(promedios, key=lambda x: x["Promedio"], reverse=True)
    return promedios_ordenados[:3]

def sum_all_averages(student_list):
    promedios = []
    for student in student_list:
        grades = [student.spanish_grade, student.english_grade, student.social_studies_grade, student.science_grade]
        promedios.append(sum(grades) / len(grades))
    return sum(promedios) / len(promedios)