"""Desafio 4 - Sistema de Autenticação (while)."""

SENHA_CORRETA = "python123"
LIMITE_TENTATIVAS = 3

tentativas = 0
autenticado = False

while tentativas < LIMITE_TENTATIVAS and not autenticado:
    senha_digitada = input("Digite a senha: ")
    tentativas += 1
    if senha_digitada == SENHA_CORRETA:
        autenticado = True
    else:
        restantes = LIMITE_TENTATIVAS - tentativas
        print(f"Senha incorreta! Tentativas restantes: {restantes}")

if autenticado:
    print(f"Acesso liberado após {tentativas} tentativa(s).")
else:
    print(f"Acesso bloqueado após {tentativas} tentativas erradas.")
