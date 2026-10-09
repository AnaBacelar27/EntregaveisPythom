programa
{
	/*
	 * Sistema de Produtos - versão em Portugol (equivalente ao sistema_produtos.py)
	 *
	 * Equivalências:
	 *  - Lista com append()      -> vetores de tamanho fixo + contador de posições
	 *  - Filtro (list comp.)     -> laço "para" com "se"
	 *  - sort() / sorted()       -> ordenação pelo método da bolha (bubble sort)
	 *  - set()                   -> simulação manual: só adiciona se ainda não existir
	 *  - tupla (min, max, média) -> três variáveis calculadas em um laço
	 */

	const inteiro MAX = 20

	cadeia nomes[MAX], categorias[MAX]
	real precos[MAX]
	inteiro total = 0

	// Cadastro de produtos (equivale a input() + append())
	funcao cadastrar()
	{
		escreva("Quantos produtos deseja cadastrar (máx. ", MAX, ")? ")
		leia(total)
		se (total > MAX) { total = MAX }

		para (inteiro i = 0; i < total; i++) {
			escreva("\n--- Produto ", i + 1, " ---\n")
			escreva("Nome: ")
			leia(nomes[i])
			escreva("Preço: R$ ")
			leia(precos[i])
			escreva("Categoria: ")
			leia(categorias[i])
		}
	}

	funcao imprimir_produto(cadeia nome, real preco, cadeia categoria)
	{
		escreva("  ", nome, " - R$ ", preco, " - ", categoria, "\n")
	}

	// Filtragem por preço (equivale à list comprehension com if)
	funcao filtrar(real limite, logico acima)
	{
		inteiro encontrados = 0
		para (inteiro i = 0; i < total; i++) {
			se ((acima e precos[i] > limite) ou (nao acima e precos[i] < limite)) {
				imprimir_produto(nomes[i], precos[i], categorias[i])
				encontrados++
			}
		}
		se (encontrados == 0) {
			escreva("  Nenhum produto encontrado.\n")
		}
	}

	// Ordenação pelo método da bolha (equivale ao sort() / sorted())
	funcao ordenar(logico crescente)
	{
		cadeia aux_nome, aux_categoria
		real aux_preco
		logico trocar

		para (inteiro i = 0; i < total - 1; i++) {
			para (inteiro j = 0; j < total - 1 - i; j++) {
				se (crescente) {
					trocar = precos[j] > precos[j + 1]
				} senao {
					trocar = precos[j] < precos[j + 1]
				}
				se (trocar) {
					aux_preco = precos[j]
					precos[j] = precos[j + 1]
					precos[j + 1] = aux_preco

					aux_nome = nomes[j]
					nomes[j] = nomes[j + 1]
					nomes[j + 1] = aux_nome

					aux_categoria = categorias[j]
					categorias[j] = categorias[j + 1]
					categorias[j + 1] = aux_categoria
				}
			}
		}
		para (inteiro i = 0; i < total; i++) {
			imprimir_produto(nomes[i], precos[i], categorias[i])
		}
	}

	// Conjunto de categorias únicas (simulação manual do set())
	funcao categorias_unicas()
	{
		cadeia unicas[MAX]
		inteiro qtd_unicas = 0
		logico repetida

		para (inteiro i = 0; i < total; i++) {
			repetida = falso
			para (inteiro j = 0; j < qtd_unicas; j++) {
				se (categorias[i] == unicas[j]) {
					repetida = verdadeiro
				}
			}
			se (nao repetida) {
				unicas[qtd_unicas] = categorias[i]
				qtd_unicas++
			}
		}

		escreva("Categorias únicas (", qtd_unicas, "): ")
		para (inteiro i = 0; i < qtd_unicas; i++) {
			escreva(unicas[i], " ")
		}
		escreva("\n")
	}

	// Estatísticas (equivale à tupla (min, max, sum/len))
	funcao estatisticas()
	{
		real menor = precos[0], maior = precos[0], soma = 0.0
		para (inteiro i = 0; i < total; i++) {
			se (precos[i] < menor) { menor = precos[i] }
			se (precos[i] > maior) { maior = precos[i] }
			soma = soma + precos[i]
		}
		escreva("Menor preço: R$ ", menor, "\n")
		escreva("Maior preço: R$ ", maior, "\n")
		escreva("Média:       R$ ", soma / total, "\n")
	}

	funcao inicio()
	{
		real limite
		caracter opcao

		cadastrar()
		se (total == 0) {
			escreva("Nenhum produto cadastrado.\n")
			retorne
		}

		escreva("\nValor para filtro: R$ ")
		leia(limite)
		escreva("Listar (A)cima ou a(B)aixo desse valor? ")
		leia(opcao)

		escreva("\n========== RELATÓRIO FINAL ==========\n")
		escreva("\nProdutos filtrados:\n")
		filtrar(limite, opcao != 'B' e opcao != 'b')

		escreva("\nOrdem crescente (bolha):\n")
		ordenar(verdadeiro)

		escreva("\nOrdem decrescente (bolha):\n")
		ordenar(falso)

		escreva("\n")
		categorias_unicas()

		escreva("\nEstatísticas:\n")
		estatisticas()
		escreva("=====================================\n")
	}
}
