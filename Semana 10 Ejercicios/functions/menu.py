from .students import students, amount_of_students
from .allstudents import total_entered_students
from .topaverages import top_3_averages, average_grades, sum_all_averages
from .exportfilecsv import write_csv_file, read_csv_file, header

def menu():
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
                return students()
            elif option == 2:
                return total_entered_students()
            elif option == 3:
                top = top_3_averages()
                if not top:
                    print("Primero ingresa estudiantes.\n")
                else:
                    print("\nTOP 3 por promedio:")
                    # Versión SIN enumerate (como pediste):
                    i = 1
                    for item in top:
                        print(f"{i}. {item['Nombre']} → {item['Promedio']:.2f}")
                        i += 1
                    print()
            elif option == 4:
                total = sum_all_averages(amount_of_students)
                print(f"Este es la suma total de todos los promedios: {total}")
            elif option == 5:
                write_csv_file("students.csv", amount_of_students, header)
                print("Archivo CSV exportado correctamente")
            elif option == 6:
                read_csv_file("students.csv")