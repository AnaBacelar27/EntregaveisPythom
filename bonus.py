"""Desafios bônus: fatorial recursivo e relatório com *linhas e **config."""


def fatorial(n):
    """Calcula n! de forma recursiva. Lança ValueError para n negativo."""
    if n < 0:
        raise ValueError("fatorial não definido para números negativos")
    if n <= 1:
        return 1
    return n * fatorial(n - 1)


def relatorio(titulo, *linhas, **config):
    """Monta um relatório com título, linhas variáveis e configurações opcionais.

    Configurações aceitas: largura (int), caractere (str), maiusculo (bool).
    """
    largura = config.get("largura", 40)
    caractere = config.get("caractere", "=")
    if config.get("maiusculo", False):
        titulo = titulo.upper()

    partes = [caractere * largura, titulo.center(largura), caractere * largura]
    for numero, linha in enumerate(linhas, start=1):
        partes.append(f"{numero}. {linha}")
    partes.append(caractere * largura)
    return "\n".join(partes)


if __name__ == "__main__":
    print(f"5! = {fatorial(5)}")
    print(relatorio("Teste", "linha 1", "linha 2", largura=30, caractere="-"))
