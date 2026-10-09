programa
{
	// Desafio 2 - Menu de Operações (escolha / caso equivale ao match / case)
	funcao inicio()
	{
		inteiro opcao
		real numero1, numero2

		escreva("=== MENU DE OPERAÇÕES ===\n")
		escreva("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")
		escreva("Escolha uma opção: ")
		leia(opcao)
		escreva("Primeiro número: ")
		leia(numero1)
		escreva("Segundo número: ")
		leia(numero2)

		escolha (opcao) {
			caso 1:
				escreva("Resultado: ", numero1 + numero2, "\n")
				pare
			caso 2:
				escreva("Resultado: ", numero1 - numero2, "\n")
				pare
			caso 3:
				escreva("Resultado: ", numero1 * numero2, "\n")
				pare
			caso 4:
				se (numero2 == 0) {
					escreva("Erro: divisão por zero não é permitida.\n")
				} senao {
					escreva("Resultado: ", numero1 / numero2, "\n")
				}
				pare
			caso contrario:
				escreva("Opção inválida.\n")
		}
	}
}
