from persistencia import read_csv_file, write_csv_file

CATEGORY = "__CATEGORIA__"

class finance_manager:
    def __init__(self):
        self.rows = read_csv_file()  

    def text(self, s, name):
        s = (s or "").strip()
        if s == "":
            raise ValueError(f"El {name} no puede estar vacío")
        return s

    def monto(self, amount):
        try:
            value = float(amount)
        except:
            raise ValueError("El monto debe ser numérico.")
        if value <= 0:
            raise ValueError("El monto debe ser mayor a 0.")
        return value

    def list_of_categories(self):
        categories = []
        for r in self.rows:
            if r.get("Movimiento", "") == CATEGORY:
                name = (r.get("Categoria") or "").strip()
                if name != "" and (name not in categories):
                    categories.append(name)
        return categories

    def list_of_movement(self):
        movement = []
        for r in self.rows:
            if r.get("Movimiento", "") != CATEGORY:
                movement.append(r)
        return movement

    def create_category(self, name):
        name = self.text(name, "nombre de la categoría")
        category = self.list_of_categories()

        if name.lower() in [c.lower() for c in category]:
            raise ValueError("Ya existe una categoría con ese nombre.")

        self.rows.append({"Categoria": name, "Movimiento": CATEGORY, "Monto": ""})
        write_csv_file(self.rows)
        return True

    def list_categories(self):
        return self.list_of_categories()

    def create_movement(self, category, type_of_movement, amount):
        categories = self.list_of_categories()
        if len(categories) == 0:
            raise ValueError("No hay categorías disponibles. Cree una antes de agregar movimientos")

        category = self.text(category, "categoría")

        if category.lower() not in [c.lower() for c in categories]:
            raise ValueError("La categoría seleccionada no existe")

        _type = self.text(type_of_movement, "tipo de movimiento")
        if _type not in ("Gasto", "Ingreso"):
            raise ValueError("El movimiento debe ser 'Gasto' o 'Ingreso'.")

        value = self.monto(amount)
        value = -abs(value) if _type == "Gasto" else abs(value)

        self.rows.append({"Categoria": category, "Movimiento": _type, "Monto": f"{value:.2f}"})
        write_csv_file(self.rows)
        return True

    def list_movement(self):
        movements = []
        for r in self.list_of_movement():
            movements.append({
                "Categoria": (r.get("Categoria") or "").strip(),
                "Movimiento": (r.get("Movimiento") or "").strip(),
                "Monto": (r.get("Monto") or "").strip()
            })
        return movements

