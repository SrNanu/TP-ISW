# test_triangle.py

import pytest
from triangle_classifier import clasificar_triangulo

# --- 1. Pruebas basadas en Tablas de Decisión ---

def test_triangulo_equilatero():
    """Prueba la Regla 1: Triángulo Equilátero."""
    assert clasificar_triangulo(10, 10, 10) == "Equilátero"
    assert clasificar_triangulo(5, 5, 5) == "Equilátero"

def test_triangulo_isosceles():
    """Prueba la Regla 2: Triángulo Isósceles."""
    assert clasificar_triangulo(10, 10, 5) == "Isósceles"
    assert clasificar_triangulo(5, 10, 10) == "Isósceles"
    assert clasificar_triangulo(10, 5, 10) == "Isósceles"

def test_triangulo_escaleno():
    """Prueba la Regla 3: Triángulo Escaleno."""
    assert clasificar_triangulo(3, 4, 5) == "Escaleno"
    assert clasificar_triangulo(10, 12, 15) == "Escaleno"

def test_no_es_un_triangulo_valido():
    """Prueba la Regla 4: No cumple la desigualdad triangular."""
    assert clasificar_triangulo(1, 2, 3) == "No es un triángulo válido"
    assert clasificar_triangulo(5, 2, 10) == "No es un triángulo válido"

def test_lados_deben_ser_positivos():
    """Prueba la Regla 5: Lados no positivos."""
    assert clasificar_triangulo(0, 5, 5) == "Los lados deben ser positivos"
    assert clasificar_triangulo(-1, 5, 5) == "Los lados deben ser positivos"


# --- 2. Pruebas basadas en Valores Límite ---

@pytest.mark.parametrize("a, b, c, esperado", [
    # Valores mínimos positivos
    (1, 1, 1, "Equilátero"),
    (2, 2, 1, "Isósceles"),
    (2, 3, 4, "Escaleno"),

    # Límite de la desigualdad triangular (suma de dos lados igual al tercero)
    (1, 2, 3, "No es un triángulo válido"),
    (7, 3, 4, "No es un triángulo válido"),
    (10, 5, 5, "No es un triángulo válido"),

    # Valores con cero
    (0, 10, 10, "Los lados deben ser positivos"),
    (10, 0, 10, "Los lados deben ser positivos"),
    (10, 10, 0, "Los lados deben ser positivos"),

    # Valores negativos
    (-5, 5, 5, "Los lados deben ser positivos"),
    (5, -5, 5, "Los lados deben ser positivos"),
    (5, 5, -5, "Los lados deben ser positivos"),
])
def test_valores_limite_y_particiones(a, b, c, esperado):
    """
    Prueba varios casos límite y de partición de equivalencia
    utilizando la parametrización de PyTest.
    """
    assert clasificar_triangulo(a, b, c) == esperado