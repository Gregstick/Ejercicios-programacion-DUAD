import csv


MOVS_FILE = "finanzas.csv"
CATS_FILE = "categories.csv"

MOVS_HEADERS = ["Category", "Title", "Amount"]
CATS_HEADERS = ["Category"]

def read_movements():
    try:
        with open(MOVS_FILE, 'r', encoding='utf-8', newline='') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []

def write_movements(rows):
    with open(MOVS_FILE, "w", encoding='utf-8', newline="") as f:
        w = csv.DictWriter(f, fieldnames=MOVS_HEADERS)
        w.writeheader()
        w.writerows(rows)

def read_categories():
    try:
        with open(CATS_FILE, "r", encoding='utf-8', newline="") as f:
            return [r["Category"].strip() for r in csv.DictReader(f)]
    except FileNotFoundError:
        return []

def write_categories(names):
    with open(CATS_FILE, "w", encoding='utf-8', newline="") as f:
        w = csv.DictWriter(f, fieldnames=CATS_HEADERS)
        w.writeheader()
        for n in names:
            w.writerow({"Category": n})
