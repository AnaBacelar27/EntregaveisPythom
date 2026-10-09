"""Modelagem de um sistema bancário orientado a objetos."""

import re
from abc import ABC, abstractmethod


class Cliente:
    """Titular de uma ou mais contas."""

    PADRAO_EMAIL = re.compile(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$")
    PADRAO_CPF = re.compile(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$")

    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    @property
    def nome(self):
        """Nome do cliente (não pode ser vazio)."""
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor or not valor.strip():
            raise ValueError("O nome do cliente não pode ser vazio.")
        self._nome = valor.strip()

    @property
    def cpf(self):
        """CPF no formato 000.000.000-00 (somente leitura após a criação)."""
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        if hasattr(self, "_cpf"):
            raise AttributeError("O CPF não pode ser alterado.")
        if not self.PADRAO_CPF.match(valor):
            raise ValueError(f"CPF inválido: '{valor}'")
        self._cpf = valor

    @property
    def email(self):
        """E-mail no formato usuario@dominio.ext."""
        return self._email

    @email.setter
    def email(self, valor):
        if not self.PADRAO_EMAIL.match(valor):
            raise ValueError(f"E-mail inválido: '{valor}'")
        self._email = valor.lower()

    def __str__(self):
        return f"{self.nome} (CPF {self.cpf})"

    def __repr__(self):
        return f"Cliente(nome={self.nome!r}, cpf={self.cpf!r}, email={self.email!r})"

    def __eq__(self, outro):
        return isinstance(outro, Cliente) and self.cpf == outro.cpf

    def __hash__(self):
        return hash(self.cpf)


class Conta(ABC):
    """Classe abstrata que define o contrato de qualquer conta bancária."""

    _proximo_numero = 1

    def __init__(self, titular, saldo_inicial=0.0):
        if not isinstance(titular, Cliente):
            raise TypeError("O titular deve ser um Cliente.")
        self._titular = titular
        self._numero = Conta._proximo_numero
        Conta._proximo_numero += 1
        self._saldo = 0.0
        self.saldo = saldo_inicial

    @property
    def titular(self):
        """Cliente dono da conta (composição: a conta TEM um cliente)."""
        return self._titular

    @property
    def numero(self):
        """Número sequencial da conta (somente leitura)."""
        return self._numero

    @property
    def saldo(self):
        """Saldo atual da conta."""
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < self.limite_negativo():
            raise ValueError(f"Saldo não pode ficar abaixo de R$ {self.limite_negativo():.2f}.")
        self._saldo = valor

    def limite_negativo(self):
        """Menor saldo permitido. Por padrão a conta não pode ficar negativa."""
        return 0.0

    def depositar(self, valor):
        """Deposita um valor positivo na conta."""
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor

    def sacar(self, valor):
        """Saca um valor positivo, respeitando as regras de saldo e tarifa da conta."""
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        self.saldo -= valor + self.tarifa_saque()

    def tarifa_saque(self):
        """Tarifa cobrada a cada saque."""
        return 0.0

    @abstractmethod
    def tipo(self):
        """Nome legível do tipo de conta."""

    @abstractmethod
    def calcular_rendimento_mensal(self):
        """Valor que a conta rende (ou custa) no mês. Método polimórfico."""

    def __str__(self):
        return f"{self.tipo()} nº {self.numero:03d} | {self.titular.nome} | Saldo: R$ {self.saldo:,.2f}"

    def __repr__(self):
        return f"{type(self).__name__}(titular={self.titular.nome!r}, saldo={self.saldo:.2f})"

    def __eq__(self, outra):
        return isinstance(outra, Conta) and self.numero == outra.numero

    def __lt__(self, outra):
        return self.saldo < outra.saldo


class ContaCorrente(Conta):
    """Conta com cheque especial e tarifa por saque."""

    TARIFA_SAQUE = 1.50
    TAXA_MANUTENCAO = 15.00

    def __init__(self, titular, saldo_inicial=0.0, limite_cheque_especial=500.0):
        if limite_cheque_especial < 0:
            raise ValueError("O limite do cheque especial não pode ser negativo.")
        self._limite_cheque_especial = limite_cheque_especial
        super().__init__(titular, saldo_inicial)

    @property
    def limite_cheque_especial(self):
        """Valor máximo que o saldo pode ficar negativo."""
        return self._limite_cheque_especial

    def limite_negativo(self):
        return -self._limite_cheque_especial

    def tarifa_saque(self):
        return self.TARIFA_SAQUE

    def tipo(self):
        return "Conta Corrente"

    def calcular_rendimento_mensal(self):
        """Conta corrente não rende: cobra manutenção."""
        return -self.TAXA_MANUTENCAO

    def __str__(self):
        return f"{super().__str__()} | Cheque especial: R$ {self.limite_cheque_especial:,.2f}"


class ContaPoupanca(Conta):
    """Conta que rende juros mensais e não pode ficar negativa."""

    def __init__(self, titular, saldo_inicial=0.0, taxa_juros=0.005):
        super().__init__(titular, saldo_inicial)
        self.taxa_juros = taxa_juros

    @property
    def taxa_juros(self):
        """Taxa de juros mensal (entre 0 e 5%)."""
        return self._taxa_juros

    @taxa_juros.setter
    def taxa_juros(self, valor):
        if not 0 <= valor <= 0.05:
            raise ValueError("A taxa de juros deve estar entre 0% e 5% ao mês.")
        self._taxa_juros = valor

    def tipo(self):
        return "Conta Poupança"

    def calcular_rendimento_mensal(self):
        return self.saldo * self.taxa_juros

    def __str__(self):
        return f"{super().__str__()} | Juros: {self.taxa_juros:.2%} a.m."


class ContaInvestimento(Conta):
    """Conta de investimento com perfil de risco e saque mínimo."""

    RENTABILIDADE = {"conservador": 0.008, "moderado": 0.012, "arrojado": 0.018}
    SAQUE_MINIMO = 100.0

    def __init__(self, titular, saldo_inicial=0.0, perfil="conservador"):
        super().__init__(titular, saldo_inicial)
        self.perfil = perfil

    @property
    def perfil(self):
        """Perfil de risco: conservador, moderado ou arrojado."""
        return self._perfil

    @perfil.setter
    def perfil(self, valor):
        valor = valor.lower()
        if valor not in self.RENTABILIDADE:
            raise ValueError(f"Perfil inválido: '{valor}'. Use: {', '.join(self.RENTABILIDADE)}.")
        self._perfil = valor

    def sacar(self, valor):
        if valor < self.SAQUE_MINIMO:
            raise ValueError(f"O saque mínimo em investimentos é R$ {self.SAQUE_MINIMO:.2f}.")
        super().sacar(valor)

    def tipo(self):
        return "Conta Investimento"

    def calcular_rendimento_mensal(self):
        return self.saldo * self.RENTABILIDADE[self.perfil]

    def __str__(self):
        return f"{super().__str__()} | Perfil: {self.perfil}"


class Banco:
    """Agrega clientes e contas (composição: o banco TEM contas)."""

    def __init__(self, nome, contas=None):
        self.nome = nome
        self._contas = [] if contas is None else list(contas)

    @property
    def contas(self):
        """Cópia defensiva da lista de contas."""
        return list(self._contas)

    def abrir_conta(self, conta):
        """Adiciona uma conta ao banco."""
        if not isinstance(conta, Conta):
            raise TypeError("Somente objetos do tipo Conta podem ser adicionados.")
        self._contas.append(conta)
        return conta

    def total_depositos(self):
        """Soma dos saldos de todas as contas."""
        return sum(conta.saldo for conta in self._contas)

    def __len__(self):
        return len(self._contas)

    def __str__(self):
        return f"Banco {self.nome} | {len(self)} contas | Total: R$ {self.total_depositos():,.2f}"

    def __repr__(self):
        return f"Banco(nome={self.nome!r}, contas={len(self)})"
