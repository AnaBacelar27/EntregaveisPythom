"""Módulo calculadora: operações matemáticas básicas."""


def somar(a, b):
    """Retorna a soma de a e b."""
    return a + b


def subtrair(a, b):
    """Retorna a diferença entre a e b."""
    return a - b


def multiplicar(a, b):
    """Retorna o produto de a e b."""
    return a * b


def dividir(a, b):
    """Retorna a divisão de a por b, ou None se b for zero.

    A divisão por zero é tratada explicitamente para não quebrar o programa.
    """
    if b == 0:
        print("Erro: divisão por zero não é permitida.")
        return None
    return a / b


if __name__ == "__main__":
    print(f"somar(2, 3) = {somar(2, 3)}")
    print(f"subtrair(10, 4) = {subtrair(10, 4)}")
    print(f"multiplicar(3, 5) = {multiplicar(3, 5)}")
    print(f"dividir(10, 2) = {dividir(10, 2)}")
    print(f"dividir(10, 0) = {dividir(10, 0)}")
