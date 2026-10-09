programa
{
	// Desafio 4 - Sistema de Autenticação (enquanto equivale ao while)
	funcao inicio()
	{
		const cadeia SENHA_CORRETA = "python123"
		const inteiro LIMITE_TENTATIVAS = 3
		cadeia senha_digitada
		inteiro tentativas = 0
		logico autenticado = falso

		enquanto (tentativas < LIMITE_TENTATIVAS e nao autenticado) {
			escreva("Digite a senha: ")
			leia(senha_digitada)
			tentativas = tentativas + 1
			se (senha_digitada == SENHA_CORRETA) {
				autenticado = verdadeiro
			} senao {
				escreva("Senha incorreta! Tentativas restantes: ", LIMITE_TENTATIVAS - tentativas, "\n")
			}
		}

		se (autenticado) {
			escreva("Acesso liberado após ", tentativas, " tentativa(s).\n")
		} senao {
			escreva("Acesso bloqueado após ", tentativas, " tentativas erradas.\n")
		}
	}
}
