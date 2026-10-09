programa
{
	// Versão em Portugol do módulo calculadora.py
	// Em Portugol os parâmetros simples são passados POR VALOR;
	// em Python, a passagem é POR ATRIBUIÇÃO (referência ao objeto).

	funcao real somar(real a, real b) { retorne a + b }
	funcao real subtrair(real a, real b) { retorne a - b }
	funcao real multiplicar(real a, real b) { retorne a * b }

	// Trata a divisão por zero sem quebrar o programa (retorna 0 e avisa)
	funcao real dividir(real a, real b)
	{
		se (b == 0) {
			escreva("Erro: divisão por zero não é permitida.\n")
			retorne 0.0
		}
		retorne a / b
	}

	funcao inicio()
	{
		escreva("10 + 5 = ", somar(10.0, 5.0), "\n")
		escreva("10 - 5 = ", subtrair(10.0, 5.0), "\n")
		escreva("10 x 5 = ", multiplicar(10.0, 5.0), "\n")
		escreva("10 / 5 = ", dividir(10.0, 5.0), "\n")
		escreva("10 / 0 = ", dividir(10.0, 0.0), "\n")
	}
}
