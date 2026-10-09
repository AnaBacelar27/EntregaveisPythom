"""Desafio 2 - Menu de Operações Matemáticas (match / case)."""

print("=== MENU DE OPERAÇÕES ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Escolha uma opção: ")
numero_1 = float(input("Primeiro número: "))
numero_2 = float(input("Segundo número: "))

match opcao:
    case "1":
        print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
    case "2":
        print(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")
    case "3":
        print(f"{numero_1} x {numero_2} = {numero_1 * numero_2}")
    case "4":
        if numero_2 == 0:
            print("Erro: divisão por zero não é permitida.")
        else:
            print(f"{numero_1} / {numero_2} = {numero_1 / numero_2:.2f}")
    case _:
        print(f"Opção '{opcao}' inválida.")
