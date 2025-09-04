import csv
from .students import amount_of_students

file_path = r"C:\Users\grego\OneDrive\Escritorio\Greg\Ejercicios-programacion-DUAD\Semana 10 Ejercicios\students.csv"
header = ['Nombre', 'Sección', 'Nota de Español', 'Nota de Inglés', 'Nota de Sociales', 'Nota de Ciencias']

def write_csv_file(file_path, data, header):
    # data: lista de diccionarios con EXACTAMENTE estas claves = HEADER
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)
#write_csv_file(
#    'C:\\Users\\grego\\OneDrive\\Escritorio\\Greg\\LYFTER Programación\\Semana 10 Ejercicios.py',
#   amount_of_students,
#  students_grades
# )


def read_csv_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            amount_of_students.clear()

            for row in reader:
                row['Nota de Español'] = int(row['Nota de Español'])
                row['Nota de Inglés'] = int(row['Nota de Inglés'])
                row['Nota de Sociales'] = int(row['Nota de Sociales'])
                row['Nota de Ciencias'] = int(row['Nota de Ciencias'])

                amount_of_students.append(row)

        print("Datos importados correctamente")

    except ValueError:
        print("No existe un archivo CSV previamente exportado")