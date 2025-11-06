import FreeSimpleGUI as sg
from logica import finance_manager

sg.theme("SystemDefault")


def dialogo_categoria():
    layout = [
        [sg.Text("Nombre de la categoría")],
        [sg.Input(key="-NOMBRE-")],
        [sg.Push(), sg.Button("Guardar", key="-OK-"), sg.Button("Cancelar")]
    ]
    win = sg.Window("Nueva categoría", layout, modal=True)
    ev, val = win.read()
    win.close()
    if ev == "-OK-":
        return val.get("-NOMBRE-")
    return None


def dialogo_monto_y_categoria(categorias, tipo_mov):
    layout = [
        [sg.Text(f"Tipo de movimiento: {tipo_mov}")],
        [sg.Text("Categoría")],
        [sg.Combo(categorias, key="-CATEG-", readonly=True)],
        [sg.Text("Monto (sin signo)")],
        [sg.Input(key="-MONTO-")],
        [sg.Push(), sg.Button("Guardar", key="-OK-"), sg.Button("Cancelar")]
    ]
    win = sg.Window(f"Nuevo {tipo_mov}", layout, modal=True)
    ev, val = win.read()
    win.close()
    if ev == "-OK-":
        return {
            "categoria": val.get("-CATEG-"),
            "monto": val.get("-MONTO-"),
            "tipo": tipo_mov
        }
    return None


def _rows_para_tabla(movs):
    return [[m["Categoria"], m["Movimiento"], m["Monto"]] for m in movs]


def main():
    g = finance_manager()

    headings = ["Categoria", "Movimiento", "Monto"]
    tabla = sg.Table(
        values=[],
        headings=headings,
        key="-TABLA-",
        auto_size_columns=True,
        expand_x=True,
        expand_y=True,
        justification="left"
    )

    layout = [
        [
            sg.Button("Agregar Categoría", key="-ADD_CAT-"),
            sg.Button("Agregar Gasto", key="-ADD_GASTO-"),
            sg.Button("Agregar Ingreso", key="-ADD_ING-")
        ],
        [tabla],
        [sg.Push(), sg.Button("Salir")]
    ]

    win = sg.Window("Gestor de Finanzas (FreeSimpleGUI)", layout, resizable=True, finalize=True)

    def refresh():
        win["-TABLA-"].update(_rows_para_tabla(g.list_movement()))

    refresh()

    while True:
        ev, val = win.read()
        if ev in (sg.WINDOW_CLOSED, "Salir"):
            break

        if ev == "-ADD_CAT-":
            nombre = dialogo_categoria()
            if nombre is None:
                continue
            try:
                g.create_category(nombre)
                sg.popup_ok("Categoría creada.")
            except Exception as e:
                sg.popup_error(str(e))
            refresh()

        if ev in ("-ADD_GASTO-", "-ADD_ING-"):
            cats = g.list_categories()
            if not cats:
                sg.popup_error("No hay categorías disponibles. Cree una antes de agregar movimientos.")
                continue

            tipo = "Gasto" if ev == "-ADD_GASTO-" else "Ingreso"
            data = dialogo_monto_y_categoria(cats, tipo)
            if data is None:
                continue

            try:
                g.create_movement(
                    data["categoria"],   
                    data["tipo"],        
                    data["monto"]        
                )
                sg.popup_ok("Movimiento registrado.")
            except Exception as e:
                sg.popup_error(str(e))
            refresh()

    win.close()


if __name__ == "__main__":
    main()

