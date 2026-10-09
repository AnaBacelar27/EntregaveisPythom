programa
{
	// Versão em Portugol dos desafios bônus

	// Fatorial recursivo
	funcao inteiro fatorial(inteiro n)
	{
		se (n <= 1) {
			retorne 1
		}
		retorne n * fatorial(n - 1)
	}

	// Média (estatistica.media)
	funcao real media(real valores[], inteiro quantidade)
	{
		real soma = 0.0
		para (inteiro i = 0; i < quantidade; i++) {
			soma = soma + valores[i]
		}
		retorne soma / quantidade
	}

	funcao inicio()
	{
		real notas[5] = {7.0, 8.0, 8.0, 6.0, 10.0}
		escreva("6! = ", fatorial(6), "\n")
		escreva("Média das notas: ", media(notas, 5), "\n")
	}
}
