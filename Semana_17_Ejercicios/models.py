class Category:
    def __init__(self, name: str):
        name = (name or "").strip()
        if name == "":
            raise ValueError("Category name cannot be empty.")
        self.name = name

    def normalized(self) -> str:
        return self.name


class Movement:
    def __init__(self, title: str, amount: float, category: str):
        title = (title or "").strip()
        if title == "":
            raise ValueError("Title cannot be empty.")

        try:
            amount = float(amount)
        except:
            raise ValueError("Amount must be numeric.")

        category = (category or "").strip()
        if category == "":
            raise ValueError("Category cannot be empty.")

        self.title = title
        self.amount = amount         
        self.category = category

    def to_row(self) -> dict:
        return {
            "Category": self.category,
            "Title": self.title,
            "Amount": f"{self.amount:.2f}",
        }
