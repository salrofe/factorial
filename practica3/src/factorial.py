def factorial(n):
    if not isinstance(n, int):
        raise TypeError("L'argument deu ser un enter")
    if n < 0:
        raise ValueError("L'argument deu ser un enter no negatiu")
    if n == 0:
        return 1 
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
   