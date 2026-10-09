programa
{
	// Desafio 3 - Análise de Números (para equivale ao for)
	funcao inicio()
	{
		const inteiro QUANTIDADE = 5
		real numero, soma = 0.0, maior = 0.0, menor = 0.0, media
		inteiro i

		para (i = 1; i <= QUANTIDADE; i++) {
			escreva("Digite o ", i, "º número: ")
			leia(numero)
			soma = soma + numero
			se (i == 1 ou numero > maior) {
				maior = numero
			}
			se (i == 1 ou numero < menor) {
				menor = numero
			}
		}

		media = soma / QUANTIDADE

		escreva("Soma: ", soma, "\n")
		escreva("Média: ", media, "\n")
		escreva("Maior: ", maior, "\n")
		escreva("Menor: ", menor, "\n")
	}
}
