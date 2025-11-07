import pytest
from logic import FinanceManager


def crear_manager_vacio():
    """Crea un manager vacío para pruebas (sin depender de archivos CSV)."""
    # Arrange
    fm = FinanceManager()
    # Act
    fm.rows = []
    fm.categories = []
    # Assert
    return fm


def test_add_category_agrega_categoria():
    # Arrange
    fm = crear_manager_vacio()

    # Act
    fm.add_category("Comida")

    # Assert
    assert "Comida" in fm.get_categories()


def test_add_category_rechaza_duplicada():
    # Arrange
    fm = crear_manager_vacio()
    fm.add_category("Casa")

    # Act + Assert
    with pytest.raises(ValueError):
        fm.add_category("casa")  

def test_add_income_guarda_positivo():
    # Arrange
    fm = crear_manager_vacio()
    fm.add_category("Trabajo")

    # Act
    fm.add_income("Salario", "8000", "Trabajo")

    # Assert
    movs = fm.get_movements()
    assert len(movs) == 1
    assert movs[0]["Category"] == "Trabajo"
    assert movs[0]["Title"] == "Salario"
    assert float(movs[0]["Amount"]) == 8000.0  


def test_add_expense_guarda_negativo():
    # Arrange
    fm = crear_manager_vacio()
    fm.add_category("Casa")

    # Act
    fm.add_expense("Alquiler", "2500", "Casa")

    # Assert
    movs = fm.get_movements()
    assert len(movs) == 1
    assert movs[0]["Category"] == "Casa"
    assert movs[0]["Title"] == "Alquiler"
    assert float(movs[0]["Amount"]) == -2500.0 


def test_add_movement_error_si_sin_categoria_previa():
    # Arrange
    fm = crear_manager_vacio()

    # Act + Assert
    with pytest.raises(RuntimeError):
        fm.add_income("Venta", "500", "General")


def test_amount_error_si_no_numerico():
    # Arrange
    fm = crear_manager_vacio()
    fm.add_category("Trabajo")

    # Act + Assert
    with pytest.raises(ValueError):
        fm.add_income("Salario", "abc", "Trabajo")


def test_amount_error_si_cero_o_negativo():
    # Arrange
    fm = crear_manager_vacio()
    fm.add_category("Trabajo")

    # Act + Assert
    with pytest.raises(ValueError):
        fm.add_income("Salario", "0", "Trabajo")

    # Act + Assert
    with pytest.raises(ValueError):
        fm.add_income("Salario", "-100", "Trabajo")
