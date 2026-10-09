"""Sistema de Análise de Dados - leitura de CSV, validação com regex e relatório."""

import csv
import sys

from validadores import validar_registro

COLUNAS_OBRIGATORIAS = ("nome", "email", "cpf", "telefone", "data_nascimento", "idade")
ARQUIVO_PADRAO = "dados.csv"
ARQUIVO_RELATORIO = "relatorio.txt"


def ler_registros(caminho):
    """Lê o arquivo CSV e retorna a lista de registros (dicionários).

    Lança KeyError se alguma coluna obrigatória estiver ausente.
    """
    with open(caminho, encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        colunas = leitor.fieldnames or []
        for coluna in COLUNAS_OBRIGATORIAS:
            if coluna not in colunas:
                raise KeyError(coluna)
        return list(leitor)


def analisar(registros):
    """Separa os registros em válidos e inválidos (com os motivos)."""
    validos = []
    invalidos = []
    for numero_linha, registro in enumerate(registros, start=2):
        erros = validar_registro(registro)
        if erros:
            invalidos.append((numero_linha, registro, erros))
        else:
            validos.append(registro)
    return validos, invalidos


def gerar_relatorio(validos, invalidos):
    """Monta o relatório final formatado com f-strings."""
    total = len(validos) + len(invalidos)
    percentual = len(validos) / total * 100 if total else 0
    linha = "=" * 60

    partes = [linha, f"{'RELATÓRIO DE ANÁLISE DE DADOS':^60}", linha]

    partes.append(f"\nREGISTROS VÁLIDOS ({len(validos)}):")
    for registro in validos:
        partes.append(f"  ✔ {registro['nome']:<20} {registro['email']:<28} {registro['cpf']}")

    partes.append(f"\nREGISTROS INVÁLIDOS ({len(invalidos)}):")
    for numero_linha, registro, erros in invalidos:
        partes.append(f"  ✘ Linha {numero_linha} - {registro['nome']}")
        for erro in erros:
            partes.append(f"      • {erro}")

    partes.append("\nESTATÍSTICAS:")
    partes.append(f"  Total de registros:  {total}")
    partes.append(f"  Registros válidos:   {len(validos)}")
    partes.append(f"  Registros inválidos: {len(invalidos)}")
    partes.append(f"  Taxa de aprovação:   {percentual:.1f}%")
    partes.append(linha)
    return "\n".join(partes)


def main():
    """Executa a análise do arquivo informado (ou dados.csv por padrão)."""
    caminho = sys.argv[1] if len(sys.argv) > 1 else ARQUIVO_PADRAO
    print(f"Analisando o arquivo '{caminho}'...\n")

    try:
        registros = ler_registros(caminho)
    except FileNotFoundError:
        print(f"Erro: o arquivo '{caminho}' não foi encontrado.")
    except KeyError as erro:
        print(f"Erro: coluna obrigatória ausente no CSV: {erro}")
    else:
        validos, invalidos = analisar(registros)
        relatorio = gerar_relatorio(validos, invalidos)
        print(relatorio)
        with open(ARQUIVO_RELATORIO, "w", encoding="utf-8") as saida:
            saida.write(relatorio + "\n")
        print(f"\nRelatório salvo em '{ARQUIVO_RELATORIO}'.")
    finally:
        print("Análise finalizada.")


if __name__ == "__main__":
    main()
