from persistence import read_movements, write_movements, read_categories, write_categories
from models import Category, Movement

CATEGORY = "__CATEGORIA__"

class FinanceManager:
    def __init__(self):
        self.rows = read_movements() or []
        self.categories = read_categories() or []

    def add_category(self, name: str):
        cat = Category(name).normalized()
        for c in self.categories:
            if c.lower() == cat.lower():
                raise ValueError("Category already exists.")
        self.categories.append(cat)
        write_categories(self.categories)
        return True

    def get_categories(self):
        return list(self.categories)

    def add_income(self, title: str, amount_without_sign: str, category: str):
        amount = float(self._amount_strict(amount_without_sign))
        return self.add_movement(title, +abs(amount), category)

    def add_expense(self, title: str, amount_without_sign: str, category: str):
        amount = float(self._amount_strict(amount_without_sign))
        return self.add_movement(title, -abs(amount), category)

    def add_movement(self, title: str, signed_amount: float, category: str):
        if len(self.categories) == 0:
            raise ValueError("No categories available.")
        exists = False
        for c in self.categories:
            if c.lower() == (category or "").strip().lower():
                exists = True
                break
        if not exists:
                raise ValueError("Category does not exists.")

        mv = Movement(title, signed_amount, category)
        self.rows.append(mv.to_row())
        write_movements(self.rows)
        return True

    def get_movements(self):
        out = []
        for r in (self.rows or []):
            out.append({
                "Category": (r.get("Category") or "").strip(),
                "Title": (r.get("Title") or "").strip(),
                "Amount": (r.get("Amount") or "").strip()
            })
        return out

    def _amount_strict(self, s: str) -> float:
        s = (s or "").strip()
        if s == "":
            raise ValueError("Amount must be greater than 0 (without sign).")
        try:
            val = float(s)
        except: 
            raise ValueError("Amount must be numeric.")
        if val <= 0:
            raise ValueError("Amount must be greater than 0.")
        return val