import csv
from S10_functions_duplicate.students import Student

file_path = r"C:\Users\grego\OneDrive\Escritorio\Greg\Ejercicios-programacion-DUAD\Semana 10 Ejercicios\students.csv"
header = ['Nombre', 'Sección', 'Nota de Español', 'Nota de Inglés', 'Nota de Sociales', 'Nota de Ciencias']

def write_csv_file(file_path, data, header):
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()

        rows = []
        for student in data:
            rows.append({
                "Nombre" : student.name,
                "Sección" : student.section,
                "Nota de Español" : student.spanish_grade,
                "Nota de Inglés" : student.english_grade,
                "Nota de Sociales" : student.social_studies_grade,
                "Nota de Ciencias" : student.science_grade
            })

            writer.writerows(rows)
        print("Archivo CSV exportado correctamente.")


def read_csv_file(file_path):
    filas = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student(
                    name=row['Nombre'],
                    section=row['Sección'],
                    spanish_grade=int(row['Nota de Español']),
                    english_grade=int(row['Nota de Inglés']),
                    social_studies_grade=int(row['Nota de Sociales']),
                    science_grade=int(row['Nota de Ciencias'])
                )
                filas.append(student)

        print("Datos importados correctamente")

    except ValueError:
        print("No existe un archivo CSV previamente exportado")
    
    return filas