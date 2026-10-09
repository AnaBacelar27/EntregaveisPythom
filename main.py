"""Script principal: importa os módulos criados e demonstra o reaproveitamento."""

import calculadora
import estatistica as est
from bonus import fatorial, relatorio
from lista_segura import adicionar_item_seguro
from utilidades import caixa, celsius_para_fahrenheit, ficha_aluno, validar_senha


def main():
    """Executa a demonstração de todos os módulos."""
    print("=== CALCULADORA ===")
    print(f"10 + 5 = {calculadora.somar(10, 5)}")
    print(f"10 - 5 = {calculadora.subtrair(10, 5)}")
    print(f"10 x 5 = {calculadora.multiplicar(10, 5)}")
    print(f"10 / 5 = {calculadora.dividir(10, 5)}")
    print(f"10 / 0 = {calculadora.dividir(10, 0)}")

    print("\n=== UTILIDADES ===")
    print(f"30 °C = {celsius_para_fahrenheit(30):.1f} °F")
    for senha in ("abc", "SenhaForte1"):
        valida, problemas = validar_senha(senha)
        status = "válida" if valida else f"inválida ({', '.join(problemas)})"
        print(f"Senha '{senha}': {status}")
    print(f"Total do caixa: R$ {caixa(19.90, 5.50, 12.00, desconto=10):.2f}")
    print(ficha_aluno("Beatriz", idade=21, curso="Desenvolvimento Web", turma="DevWeb III"))

    print("\n=== LISTA SEGURA ===")
    original = ["caderno", "caneta"]
    nova = adicionar_item_seguro(original, "lápis")
    print(f"Original: {original}")
    print(f"Nova:     {nova}")

    print("\n=== BÔNUS ===")
    notas = [7, 8, 8, 6, 10]
    print(f"Média: {est.media(notas):.2f} | Mediana: {est.mediana(notas)} | Moda: {est.moda(notas)}")
    print(f"6! = {fatorial(6)}")
    print(relatorio("Resumo", "Módulos importados", "Funções reutilizadas", maiusculo=True))


if __name__ == "__main__":
    main()
