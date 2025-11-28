import pytest
from Unit_testing_Ejercicio2_Semana6 import sum_of_numbers, string, string_upper_and_lower_case, separated_string, prime_numbers


def test_sum_of_numbers_lista_grande():
    # Arrange
    numbers = [50, 5004, 5069, 44, 1000, 90, 80, 99999, 1333444]
    # Act
    resultado = sum_of_numbers(numbers)
    # Assert
    assert resultado == sum(numbers)

def test_sum_of_numbers_lista_vacia():
    # Arrange
    numbers = []
    # Act
    resultado = sum_of_numbers(numbers)
    # Assert
    assert resultado == 0

def test_sum_of_numbers_con_negativos():
    # Arrange
    numbers = [-5, 5, -10, 10, 3]
    # Act
    resultado = sum_of_numbers(numbers)
    # Assert
    assert resultado == (-5 + 5 - 10 + 10 + 3)



def test_string_hola_mundo():
    # Arrange
    texto = "Hola mundo"
    # Act
    resultado = string(texto)
    # Assert
    assert texto in resultado
    assert "odnum aloH" in resultado
    assert "--->" in resultado  

def test_string_un_caracter():
    # Arrange
    texto = "A"
    # Act
    resultado = string(texto)
    # Assert
    assert "A" in resultado
    assert "--->" in resultado

def test_string_palabra_python():
    # Arrange
    texto = "Python"
    # Act
    resultado = string(texto)
    # Assert
    assert texto in resultado
    assert "nohtyP" in resultado
    assert "--->" in resultado



def test_upper_lower_incluye_frase_base(capsys):
    # Arrange / Act
    string_upper_and_lower_case()
    salida = capsys.readouterr().out
    # Assert
    assert "I love Nación Sushi" in salida

def test_upper_lower_incluye_las_etiquetas(capsys):
    # Arrange / Act
    string_upper_and_lower_case()
    salida = capsys.readouterr().out
    # Assert
    assert "upper cases" in salida
    assert "lower cases" in salida

def test_upper_lower_cantidades_correctas(capsys):
    # Arrange
    texto = "I love Nación Sushi"
    mayus = sum(1 for c in texto if c.isupper())
    minus = sum(1 for c in texto if not c.isupper())
    # Act
    string_upper_and_lower_case()
    salida = capsys.readouterr().out
    # Assert
    esperado = f"There is {mayus} upper cases and {minus} lower cases"
    assert esperado in salida



def test_separated_string_orden_lista_larga(capsys):
    # Arrange
    texto = "python - variable - funcion - computadora - monitor"
    # Act
    separated_string(texto)
    salida = capsys.readouterr().out.strip()
    # Assert
    assert salida == "computadora - funcion - monitor - python - variable"

def test_separated_string_lista_corta(capsys):
    # Arrange
    texto = "b - a - c"
    # Act
    separated_string(texto)
    salida = capsys.readouterr().out.strip()
    # Assert
    assert salida == "a - b - c"

def test_separated_string_con_duplicados(capsys):
    # Arrange
    texto = "uva - pera - manzana - pera"
    # Act
    separated_string(texto)
    salida = capsys.readouterr().out.strip()
    # Assert
    assert salida == "manzana - pera - pera - uva"



def test_prime_numbers_mezcla_primos_y_no(capsys):
    # Arrange
    lista = [1, 4, 6, 7, 13, 9, 67]
    # Act
    prime_numbers(lista)
    salida = capsys.readouterr().out.strip()
    # Assert
    assert salida == str([7, 13, 67])

def test_prime_numbers_varios_primos_pequenos(capsys):
    # Arrange
    lista = [2, 3, 5, 8, 10]
    # Act
    prime_numbers(lista)
    salida = capsys.readouterr().out.strip()
    # Assert
    assert salida == str([2, 3, 5])

def test_prime_numbers_sin_primos(capsys):
    # Arrange
    lista = [0, 1, 4, 6, 8, 9, 10]
    # Act
    prime_numbers(lista)
    salida = capsys.readouterr().out.strip()
    # Assert
    assert salida == str([])
