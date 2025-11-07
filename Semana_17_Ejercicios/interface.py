import FreeSimpleGUI as sg
from logic import FinanceManager

sg.theme("SystemDefault")


def category_dialog():
    layout = [
        [sg.Text("Category name")],
        [sg.Input(key="-NAME-")],
        [sg.Push(), sg.Button("Save", key="-OK-"), sg.Button("Cancel")]
    ]
    win = sg.Window("New Category", layout, modal=True)
    event, values = win.read()
    win.close()
    if event == "-OK-":
        return values.get("-NAME-")
    return None


def movement_dialog(categories, kind):
    layout = [
        [sg.Text(f"Type: {kind}")],
        [sg.Text("Category"), sg.Combo(categories, key="-CAT-", readonly=True)],
        [sg.Text("Title"), sg.Input(key="-TITLE-")],
        [sg.Text("Amount (no sign)"), sg.Input(key="-AMOUNT-")],
        [sg.Push(), sg.Button("Save", key="-OK-"), sg.Button("Cancel")]
    ]
    win = sg.Window(f"New {kind}", layout, modal=True)
    event, values = win.read()
    win.close()
    if event == "-OK-":
        return {
            "category": values.get("-CAT-"),
            "title": values.get("-TITLE-"),
            "amount": values.get("-AMOUNT-"),
            "kind": kind
        }
    return None


def rows_for_table(movements):
    return [[m["Category"], m["Title"], m["Amount"]] for m in movements]


def main():
    fm = FinanceManager()

    headings = ["Category", "Title", "Amount"]
    table = sg.Table(
        values=[],
        headings=headings,
        key="-TABLE-",
        auto_size_columns=True,
        expand_x=True,
        expand_y=True,
        justification="left"
    )

    layout = [
        [
            sg.Button("Add Category", key="-ADD_CAT-"),
            sg.Button("Add Expense", key="-ADD_EXP-"),
            sg.Button("Add Income", key="-ADD_INC-")
        ],
        [table],
        [sg.Push(), sg.Button("Exit")]
    ]

    win = sg.Window("Personal Finance Manager (FreeSimpleGUI)", layout, resizable=True, finalize=True)

    def refresh():
        win["-TABLE-"].update(rows_for_table(fm.get_movements()))

    refresh()

    while True:
        event, values = win.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break

        if event == "-ADD_CAT-":
            name = category_dialog()
            if name is None:
                continue
            try:
                fm.add_category(name)
                sg.popup_ok("Category created.")
            except Exception as e:
                sg.popup_error(str(e))
            refresh()

        if event in ("-ADD_EXP-", "-ADD_INC-"):
            cats = fm.get_categories()
            if not cats:
                sg.popup_error("No categories available. Create one first.")
                continue

            kind = "Expense" if event == "-ADD_EXP-" else "Income"
            data = movement_dialog(cats, kind)
            if data is None:
                continue

            try:
                if data["kind"] == "Expense":
                    fm.add_expense(title=data["title"], amount_without_sign=data["amount"], category=data["category"])
                else:
                    fm.add_income(title=data["title"], amount_without_sign=data["amount"], category=data["category"])
                sg.popup_ok("Movement recorded.")
            except Exception as e:
                sg.popup_error(str(e))
            refresh()

    win.close()


if __name__ == "__main__":
    main()

