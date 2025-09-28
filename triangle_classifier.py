def clasificar_triangulo(a, b, c):
    """
    Clasifica un triángulo en Equilátero, Isósceles o Escaleno.
    Valida que los lados formen un triángulo válido.
    """
    # Validar que los lados son positivos y que cumplen la desigualdad triangular
    if not (a > 0 and b > 0 and c > 0):
        return "Los lados deben ser positivos"
    if not (a + b > c and a + c > b and b + c > a):
        return "No es un triángulo válido"

    # Clasificación del triángulo
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
