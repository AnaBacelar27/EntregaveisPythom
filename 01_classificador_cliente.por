programa
{
	// Desafio 1 - Classificador de Cliente (se / senao se / senao)
	funcao inicio()
	{
		inteiro idade
		real renda
		cadeia categoria

		escreva("Idade do cliente: ")
		leia(idade)
		escreva("Renda mensal do cliente: R$ ")
		leia(renda)

		se (idade < 18) {
			categoria = "Não elegível (menor de idade)"
		} senao se (renda >= 15000 e idade >= 30) {
			categoria = "Diamante"
		} senao se (renda >= 8000) {
			categoria = "Ouro"
		} senao se (renda >= 3000) {
			categoria = "Prata"
		} senao {
			categoria = "Bronze"
		}

		escreva("Categoria do cliente: ", categoria, "\n")
	}
}
