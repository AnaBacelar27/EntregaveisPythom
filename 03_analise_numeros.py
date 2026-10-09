"""Desafio 3 - Análise de Números (for)."""

QUANTIDADE = 5

soma = 0
maior = None
menor = None

for posicao in range(1, QUANTIDADE + 1):
    numero = float(input(f"Digite o {posicao}º número: "))
    soma += numero
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

media = soma / QUANTIDADE

print(f"Soma:  {soma}")
print(f"Média: {media:.2f}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
