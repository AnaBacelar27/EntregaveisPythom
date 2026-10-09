"""Desafio 1 - Classificador de Cliente (if / elif / else).

Regras:
- Diamante: renda >= 15000 e idade >= 30
- Ouro:     renda >= 8000
- Prata:    renda >= 3000
- Bronze:   demais casos
"""

idade = int(input("Idade do cliente: "))
renda = float(input("Renda mensal do cliente: R$ "))

if idade < 18:
    categoria = "Não elegível (menor de idade)"
elif renda >= 15000 and idade >= 30:
    categoria = "Diamante"
elif renda >= 8000:
    categoria = "Ouro"
elif renda >= 3000:
    categoria = "Prata"
else:
    categoria = "Bronze"

print(f"Cliente com {idade} anos e renda de R$ {renda:.2f}: {categoria}")
