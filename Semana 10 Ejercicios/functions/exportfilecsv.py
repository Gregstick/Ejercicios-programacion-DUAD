import csv


file_path = r"C:\Users\grego\OneDrive\Escritorio\Greg\Ejercicios-programacion-DUAD\Semana 10 Ejercicios\students.csv"
header = ['Nombre', 'Sección', 'Nota de Español', 'Nota de Inglés', 'Nota de Sociales', 'Nota de Ciencias']

def write_csv_file(file_path, data, header):
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)


def read_csv_file(file_path):
    filas = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                row['Nota de Español'] = int(row['Nota de Español'])
                row['Nota de Inglés'] = int(row['Nota de Inglés'])
                row['Nota de Sociales'] = int(row['Nota de Sociales'])
                row['Nota de Ciencias'] = int(row['Nota de Ciencias'])

                filas.append(row)

        print("Datos importados correctamente")

    except ValueError:
        print("No existe un archivo CSV previamente exportado")
    
    return filas