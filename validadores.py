"""Funções de validação de campos com expressões regulares (módulo re)."""

import re

from excecoes import FormatoInvalidoError, IdadeInvalidaError

# usuario@dominio.com(.br): letras, números, ponto, + ou - antes do @
PADRAO_EMAIL = re.compile(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$")
# 000.000.000-00
PADRAO_CPF = re.compile(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$")
# (00) 00000-0000 ou (00) 0000-0000, espaço opcional após o DDD
PADRAO_TELEFONE = re.compile(r"^\(\d{2}\)\s?9?\d{4}-\d{4}$")
# dd/mm/aaaa com dia 01-31 e mês 01-12
PADRAO_DATA = re.compile(r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$")


def validar_email(email):
    """Retorna True se o e-mail estiver no formato usuario@dominio.ext."""
    return bool(PADRAO_EMAIL.match(email))


def validar_cpf(cpf):
    """Retorna True se o CPF estiver no formato 000.000.000-00."""
    return bool(PADRAO_CPF.match(cpf))


def validar_telefone(telefone):
    """Retorna True se o telefone estiver no formato (00) 00000-0000."""
    return bool(PADRAO_TELEFONE.match(telefone))


def validar_data(data):
    """Retorna True se a data estiver no formato dd/mm/aaaa."""
    return bool(PADRAO_DATA.match(data))


VALIDADORES = {
    "email": validar_email,
    "cpf": validar_cpf,
    "telefone": validar_telefone,
    "data_nascimento": validar_data,
}


def converter_idade(valor):
    """Converte a idade para int e valida o intervalo.

    Lança ValueError se não for número e IdadeInvalidaError se estiver fora de 0-120.
    """
    idade = int(valor)
    if not 0 <= idade <= 120:
        raise IdadeInvalidaError(idade)
    return idade


def validar_registro(registro):
    """Valida todos os campos de um registro e retorna a lista de erros encontrados."""
    erros = []
    for campo, validador in VALIDADORES.items():
        valor = registro[campo].strip()
        try:
            if not validador(valor):
                raise FormatoInvalidoError(campo, valor)
        except FormatoInvalidoError as erro:
            erros.append(str(erro))

    try:
        converter_idade(registro["idade"].strip())
    except ValueError:
        erros.append(f"idade não numérica: '{registro['idade']}'")
    except IdadeInvalidaError as erro:
        erros.append(str(erro))

    return erros
