"""Desafio 5 - Par ou ímpar (operador módulo %)."""

numero = int(input("Digite um número inteiro: "))

resultado = "par" if numero % 2 == 0 else "ímpar"

print(f"O número {numero} é {resultado}.")
