"""Sistema de Produtos - Listas, Tuplas e Conjuntos (Desafio Sprint 4)."""


def cadastrar_produtos():
    """Lê produtos via input() e retorna uma lista de dicionários (append)."""
    produtos = []
    quantidade = int(input("Quantos produtos deseja cadastrar? "))
    for indice in range(1, quantidade + 1):
        print(f"\n--- Produto {indice} ---")
        nome = input("Nome: ").strip()
        preco = float(input("Preço: R$ ").replace(",", "."))
        categoria = input("Categoria: ").strip().title()
        produtos.append({"nome": nome, "preco": preco, "categoria": categoria})
    return produtos


def filtrar_por_preco(produtos, valor_limite, acima=True):
    """Retorna os produtos acima (ou abaixo) do valor limite."""
    if acima:
        return [produto for produto in produtos if produto["preco"] > valor_limite]
    return [produto for produto in produtos if produto["preco"] < valor_limite]


def categorias_unicas(produtos):
    """Retorna um set com as categorias, sem duplicatas."""
    return {produto["categoria"] for produto in produtos}


def estatisticas_precos(produtos):
    """Retorna a tupla imutável (menor, maior, média) dos preços."""
    precos = [produto["preco"] for produto in produtos]
    return (min(precos), max(precos), sum(precos) / len(precos))


def formatar_produto(produto):
    """Retorna uma linha formatada com os dados do produto."""
    return f"  {produto['nome']:<20} R$ {produto['preco']:>9.2f}   {produto['categoria']}"


def imprimir_relatorio(produtos, filtrados, valor_limite, tipo_filtro, crescente, decrescente, categorias, estatisticas):
    """Imprime o relatório final formatado com f-strings."""
    menor, maior, media = estatisticas
    linha = "=" * 50

    print(f"\n{linha}\n{'RELATÓRIO FINAL DE PRODUTOS':^50}\n{linha}")

    print(f"\nProdutos cadastrados ({len(produtos)}):")
    for produto in produtos:
        print(formatar_produto(produto))

    print(f"\nProdutos {tipo_filtro} de R$ {valor_limite:.2f} ({len(filtrados)}):")
    for produto in filtrados:
        print(formatar_produto(produto))
    if not filtrados:
        print("  Nenhum produto encontrado.")

    print("\nOrdenados por preço crescente (sort):")
    for produto in crescente:
        print(formatar_produto(produto))

    print("\nOrdenados por preço decrescente (sorted reverse=True):")
    for produto in decrescente:
        print(formatar_produto(produto))

    print(f"\nCategorias únicas ({len(categorias)}): {', '.join(sorted(categorias))}")

    print("\nEstatísticas (tupla):")
    print(f"  Menor preço: R$ {menor:.2f}")
    print(f"  Maior preço: R$ {maior:.2f}")
    print(f"  Média:       R$ {media:.2f}")
    print(linha)


def main():
    """Fluxo principal do sistema."""
    produtos = cadastrar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    valor_limite = float(input("\nValor para filtro: R$ ").replace(",", "."))
    opcao_filtro = input("Listar produtos (A)cima ou a(B)aixo desse valor? ").strip().upper()
    acima = opcao_filtro != "B"
    tipo_filtro = "acima" if acima else "abaixo"
    filtrados = filtrar_por_preco(produtos, valor_limite, acima)

    crescente = produtos.copy()
    crescente.sort(key=lambda produto: produto["preco"])
    decrescente = sorted(produtos, key=lambda produto: produto["preco"], reverse=True)

    categorias = categorias_unicas(produtos)
    estatisticas = estatisticas_precos(produtos)

    imprimir_relatorio(produtos, filtrados, valor_limite, tipo_filtro,
                       crescente, decrescente, categorias, estatisticas)


if __name__ == "__main__":
    main()
