import pytest
from logica import finance_manager


def crear_manager_vacio():
    """Crea un manager vacío para pruebas (sin depender de archivos CSV)."""
    # Arrange
    fm = finance_manager()
    # Act
    fm.rows = []   
    # Assert 
    return fm


def test_text_falla_si_vacio():
    # Arrange
    fm = crear_manager_vacio()
    # Act + Assert
    with pytest.raises(ValueError):
        fm.text("", "campo")


def test_monto_falla_si_no_numerico():
    # Arrange
    fm = crear_manager_vacio()
    # Act + Assert
    with pytest.raises(ValueError):
        fm.monto("abc")


def test_monto_acepta_positivo():
    # Arrange
    fm = crear_manager_vacio()
    # Act
    valor = fm.monto("1000")
    # Assert
    assert valor == 1000.0


def test_create_category_agrega_categoria():
    # Arrange
    fm = crear_manager_vacio()
    # Act
    fm.create_category("Comida")
    # Assert
    assert "Comida" in fm.list_of_categories()


def test_create_category_rechaza_duplicada():
    # Arrange
    fm = crear_manager_vacio()
    fm.create_category("Casa")
    # Act + Assert
    with pytest.raises(ValueError):
        fm.create_category("casa")  


def test_create_movement_necesita_categoria_previa():
    # Arrange
    fm = crear_manager_vacio()
    # Act + Assert
    with pytest.raises(ValueError):
        fm.create_movement("Comida", "Gasto", "1000")


def test_create_movement_gasto_guarda_negativo():
    # Arrange
    fm = crear_manager_vacio()
    fm.create_category("Comida")
    # Act
    fm.create_movement("Comida", "Gasto", "2500")
    # Assert
    movs = fm.list_movement()
    assert len(movs) == 1
    assert movs[0]["Categoria"] == "Comida"
    assert movs[0]["Movimiento"] == "Gasto"
    assert movs[0]["Monto"] == "-2500.00"


def test_create_movement_ingreso_guarda_positivo():
    # Arrange
    fm = crear_manager_vacio()
    fm.create_category("Trabajo")
    # Act
    fm.create_movement("Trabajo", "Ingreso", "8000")
    # Assert
    movs = fm.list_movement()
    assert len(movs) == 1
    assert movs[0]["Categoria"] == "Trabajo"
    assert movs[0]["Movimiento"] == "Ingreso"
    assert movs[0]["Monto"] == "8000.00"
