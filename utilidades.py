"""Módulo utilidades: funções dos desafios da Prática Independente."""


def celsius_para_fahrenheit(celsius):
    """Converte uma temperatura de Celsius para Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_para_celsius(fahrenheit):
    """Converte uma temperatura de Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5 / 9


def validar_senha(senha, tamanho_minimo=8):
    """Valida uma senha e retorna (é_válida, lista_de_problemas).

    Regras: tamanho mínimo, ao menos uma letra maiúscula, uma minúscula e um dígito.
    """
    problemas = []
    if len(senha) < tamanho_minimo:
        problemas.append(f"deve ter pelo menos {tamanho_minimo} caracteres")
    if not any(caractere.isupper() for caractere in senha):
        problemas.append("deve ter ao menos uma letra maiúscula")
    if not any(caractere.islower() for caractere in senha):
        problemas.append("deve ter ao menos uma letra minúscula")
    if not any(caractere.isdigit() for caractere in senha):
        problemas.append("deve ter ao menos um número")
    return len(problemas) == 0, problemas


def caixa(*precos, desconto=0):
    """Soma uma quantidade variável de preços (*precos) e aplica desconto percentual.

    Retorna o total final.
    """
    subtotal = sum(precos)
    return subtotal - subtotal * desconto / 100


def ficha_aluno(nome, **dados):
    """Monta e retorna a ficha de um aluno com dados extras (**dados)."""
    linhas = [f"Aluno: {nome}"]
    for chave, valor in dados.items():
        linhas.append(f"  {chave.replace('_', ' ').capitalize()}: {valor}")
    return "\n".join(linhas)


if __name__ == "__main__":
    print(f"25 °C = {celsius_para_fahrenheit(25):.1f} °F")
    print(f"validar_senha('Abc12345') = {validar_senha('Abc12345')}")
    print(f"caixa(10, 20, 30, desconto=10) = {caixa(10, 20, 30, desconto=10)}")
    print(ficha_aluno("Ana", idade=20, curso="ADS"))
