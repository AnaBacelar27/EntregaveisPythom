"""Exceções personalizadas para as regras de negócio da análise."""


class ValidacaoError(Exception):
    """Classe base para erros de validação de registros."""


class FormatoInvalidoError(ValidacaoError):
    """Lançada quando um campo não respeita o formato esperado."""

    def __init__(self, campo, valor):
        self.campo = campo
        self.valor = valor
        super().__init__(f"{campo} em formato inválido: '{valor}'")


class IdadeInvalidaError(ValidacaoError):
    """Lançada quando a idade está fora do intervalo permitido (0 a 120)."""

    def __init__(self, idade):
        self.idade = idade
        super().__init__(f"idade fora do intervalo permitido (0-120): {idade}")
