from .students import students, total_entered_students, top_3_average, average_grades, sum_all_averages
from .exportfilecsv import write_csv_file, read_csv_file, header

def menu():
        student_list = []
        while True:
            print(
                " 1. Ingresar Estudiante\n",
                "2. Ver innformación de los estudiantes ingresados\n",
                "3. Ver el top 3 de el mejor promedio\n",
                "4. Ver total promedio de todos los promedios\n",
                "5. Exportar los datos actuales a un  archivo CSV\n",
                "6. Importar datos de un archivo CSV previamente exportado\n"
            )
            option = int(input("Ingrese el número de la opción que quiere ejecutar: "))
            if option == 1:
                new_students = students()
                student_list.extend(new_students)
            elif option == 2:
                total_entered_students(student_list)
            elif option == 3:
                top = top_3_average(student_list)
                if not top:
                    print("Primero ingresa estudiantes.\n")
                else:
                    print("\nTOP 3 por promedio:")
                    i = 1
                    for item in top:
                        print(f"{i}. {item['Nombre']} → {item['Promedio']:.2f}")
                        i += 1
                    print()
            elif option == 4:
                total = sum_all_averages(student_list)
                print(f"Este es la suma total de todos los promedios: {total}")
            elif option == 5:
                write_csv_file("students.csv", student_list, header)
                print("Archivo CSV exportado correctamente")
            elif option == 6:
                charged = read_csv_file("students.csv")
                if charged:
                    student_list = charged