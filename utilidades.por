programa
{
	inclua biblioteca Texto --> t

	// Versão em Portugol do módulo utilidades.py

	// Conversor de temperatura
	funcao real celsius_para_fahrenheit(real celsius)
	{
		retorne celsius * 9.0 / 5.0 + 32.0
	}

	// Validador de senha: mínimo de 8 caracteres
	funcao logico validar_senha(cadeia senha)
	{
		retorne t.numero_caracteres(senha) >= 8
	}

	// Caixa: Portugol não tem *args, então usamos um vetor e a quantidade de itens
	funcao real caixa(real precos[], inteiro quantidade, real desconto)
	{
		real subtotal = 0.0
		para (inteiro i = 0; i < quantidade; i++) {
			subtotal = subtotal + precos[i]
		}
		retorne subtotal - subtotal * desconto / 100.0
	}

	// Ficha do aluno: Portugol não tem **kwargs, então usamos dois vetores (chaves e valores)
	funcao ficha_aluno(cadeia nome, cadeia chaves[], cadeia valores[], inteiro quantidade)
	{
		escreva("Aluno: ", nome, "\n")
		para (inteiro i = 0; i < quantidade; i++) {
			escreva("  ", chaves[i], ": ", valores[i], "\n")
		}
	}

	funcao inicio()
	{
		real precos[3] = {19.9, 5.5, 12.0}
		cadeia chaves[2] = {"Idade", "Curso"}
		cadeia valores[2] = {"21", "Desenvolvimento Web"}

		escreva("30 °C = ", celsius_para_fahrenheit(30.0), " °F\n")
		escreva("Senha 'abc' válida? ", validar_senha("abc"), "\n")
		escreva("Total do caixa: R$ ", caixa(precos, 3, 10.0), "\n")
		ficha_aluno("Beatriz", chaves, valores, 2)
	}
}
