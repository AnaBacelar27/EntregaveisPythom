programa
{
	// Versão em Portugol da Lista Segura (cópia defensiva).
	// Em Portugol, vetores são passados POR REFERÊNCIA; por isso copiamos
	// item a item para um novo vetor antes de adicionar o novo elemento.

	const inteiro TAMANHO = 10

	funcao inteiro adicionar_item_seguro(cadeia original[], inteiro quantidade, cadeia item, cadeia nova[])
	{
		para (inteiro i = 0; i < quantidade; i++) {
			nova[i] = original[i]
		}
		nova[quantidade] = item
		retorne quantidade + 1
	}

	funcao inicio()
	{
		cadeia original[TAMANHO], nova[TAMANHO]
		inteiro qtd_original = 2, qtd_nova

		original[0] = "caderno"
		original[1] = "caneta"

		qtd_nova = adicionar_item_seguro(original, qtd_original, "lápis", nova)

		escreva("Original: ")
		para (inteiro i = 0; i < qtd_original; i++) { escreva(original[i], " ") }
		escreva("\nNova: ")
		para (inteiro i = 0; i < qtd_nova; i++) { escreva(nova[i], " ") }
		escreva("\n")
	}
}
