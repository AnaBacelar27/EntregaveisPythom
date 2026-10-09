"""Módulo estatistica (bônus): média, mediana e moda.

Uso com alias: import estatistica as est
"""


def media(valores):
    """Retorna a média aritmética dos valores, ou None se a lista estiver vazia."""
    if not valores:
        return None
    return sum(valores) / len(valores)


def mediana(valores):
    """Retorna a mediana dos valores, ou None se a lista estiver vazia."""
    if not valores:
        return None
    ordenados = sorted(valores)
    meio = len(ordenados) // 2
    if len(ordenados) % 2 == 0:
        return (ordenados[meio - 1] + ordenados[meio]) / 2
    return ordenados[meio]


def moda(valores):
    """Retorna a lista com o(s) valor(es) mais frequente(s)."""
    if not valores:
        return []
    frequencias = {}
    for valor in valores:
        frequencias[valor] = frequencias.get(valor, 0) + 1
    maior_frequencia = max(frequencias.values())
    return [valor for valor, total in frequencias.items() if total == maior_frequencia]


if __name__ == "__main__":
    dados = [3, 7, 7, 2, 9, 4]
    print(f"media={media(dados):.2f} mediana={mediana(dados)} moda={moda(dados)}")
