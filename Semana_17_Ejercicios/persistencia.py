import csv


file_path = "finanzas.csv"
header = ["Categoria", "Movimiento", "Monto"]


def read_csv_file():
    try:
        with open(file_path, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            rows = []
            for row in reader:
                try:
                    categoria = row["Categoria"]
                    movimiento = row["Movimiento"]
                    monto = row["Monto"]
                except KeyError:
        
                    continue
                rows.append({
                    "Categoria": categoria,
                    "Movimiento": movimiento,
                    "Monto": monto
                })
            return rows
    except:
        return []




def write_csv_file(rows):
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)
