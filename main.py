"""Demonstração do sistema bancário: instâncias, polimorfismo e exceções."""

from modelos import Banco, Cliente, Conta, ContaCorrente, ContaInvestimento, ContaPoupanca


def titulo(texto):
    """Imprime um título de seção."""
    print(f"\n{'=' * 70}\n{texto}\n{'=' * 70}")


def main():
    """Executa a demonstração completa."""
    titulo("1. CRIAÇÃO DE INSTÂNCIAS")
    ana = Cliente("Ana Souza", "123.456.789-00", "ana@email.com")
    bruno = Cliente("Bruno Lima", "987.654.321-11", "bruno@email.com")
    carla = Cliente("Carla Mendes", "111.222.333-44", "carla@email.com")
    diego = Cliente("Diego Rocha", "222.333.444-55", "diego@email.com")

    banco = Banco("PyBank")
    banco.abrir_conta(ContaCorrente(ana, 1500, limite_cheque_especial=1000))
    banco.abrir_conta(ContaPoupanca(ana, 8000))
    banco.abrir_conta(ContaCorrente(bruno, 300))
    banco.abrir_conta(ContaInvestimento(bruno, 20000, perfil="arrojado"))
    banco.abrir_conta(ContaPoupanca(carla, 2500, taxa_juros=0.007))
    banco.abrir_conta(ContaInvestimento(diego, 5000, perfil="moderado"))

    for cliente in (ana, bruno, carla, diego):
        print(cliente)
    for conta in banco.contas:
        print(conta)
    print(banco)
    print(f"Total de instâncias criadas: {4 + len(banco) + 1}")

    titulo("2. POLIMORFISMO - mesma chamada, comportamentos diferentes")
    for conta in banco.contas:
        rendimento = conta.calcular_rendimento_mensal()
        print(f"{conta.tipo():<20} {conta.titular.nome:<15} rendimento mensal: R$ {rendimento:>9.2f}")

    titulo("3. OPERAÇÕES E HERANÇA")
    corrente_ana = banco.contas[0]
    corrente_ana.sacar(2000)
    print(f"Ana sacou R$ 2000 (com tarifa) usando o cheque especial: {corrente_ana}")
    poupanca_carla = banco.contas[4]
    poupanca_carla.depositar(500)
    print(f"Carla depositou R$ 500: {poupanca_carla}")

    titulo("4. MÉTODOS ESPECIAIS (__repr__, __eq__, __lt__, __len__)")
    print(repr(ana))
    print(repr(banco.contas[1]))
    print(f"ana == Cliente com mesmo CPF? {ana == Cliente('Ana S.', '123.456.789-00', 'outro@email.com')}")
    print("Contas ordenadas por saldo (usa __lt__):")
    for conta in sorted(banco.contas):
        print(f"  R$ {conta.saldo:>10,.2f}  {conta.tipo()} - {conta.titular.nome}")
    print(f"len(banco) = {len(banco)}")

    titulo("5. TRATAMENTO DE EXCEÇÕES (validações com @property)")
    testes = [
        ("E-mail inválido", lambda: Cliente("Eva", "333.444.555-66", "eva.email.com")),
        ("CPF inválido", lambda: Cliente("Eva", "33344455566", "eva@email.com")),
        ("Nome vazio", lambda: Cliente("   ", "333.444.555-66", "eva@email.com")),
        ("Alterar CPF", lambda: setattr(ana, "cpf", "000.000.000-00")),
        ("Saldo inicial negativo na poupança", lambda: ContaPoupanca(carla, -100)),
        ("Saque acima do saldo na poupança", lambda: poupanca_carla.sacar(100000)),
        ("Saque acima do cheque especial", lambda: banco.contas[2].sacar(5000)),
        ("Depósito negativo", lambda: corrente_ana.depositar(-50)),
        ("Perfil de investimento inválido", lambda: ContaInvestimento(diego, 1000, perfil="agressivo")),
        ("Saque abaixo do mínimo em investimento", lambda: banco.contas[3].sacar(50)),
        ("Taxa de juros fora do limite", lambda: setattr(poupanca_carla, "taxa_juros", 0.2)),
        ("Instanciar classe abstrata", lambda: Conta(ana)),
    ]
    for descricao, acao in testes:
        try:
            acao()
        except (ValueError, TypeError, AttributeError) as erro:
            print(f"✘ {descricao:<40} -> {type(erro).__name__}: {erro}")
        else:
            print(f"✔ {descricao:<40} -> nenhuma exceção (inesperado)")

    titulo("6. ESTADO FINAL")
    print(banco)


if __name__ == "__main__":
    main()
