# Módulo que contiene la función factorial

def factorial(n):
    """
    Calcula el factorial de un número entero positivo.

    Entrada:
    - n: entero positivo del cual se calculará el factorial.

    Salida:
    - El factorial de n.
    """
    if not isinstance(n, int):
        raise TypeError("El argumento debe ser un entero")
    if n < 0:
        raise ValueError("El argumento debe ser un entero no negativo")
    if n == 0:
        return 1 
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__=='__main__':
    for j in range(2, 100):  # Cambio el nombre de la variable 'i' a 'j'
        print(f'{j} -> {factorial(j)}')

