# Semana 05 – Sistema de Análise de Dados (Desafio Sprint 5)

Lê um arquivo CSV com cadastros (nome, e-mail, CPF, telefone, data de nascimento e idade), valida cada campo com **expressões regulares**, trata **exceções** e gera um **relatório formatado** (no terminal e em `relatorio.txt`).

## Estrutura

| Arquivo | Função |
|---|---|
| `analisador.py` | Script principal: leitura do CSV, análise e relatório |
| `validadores.py` | Padrões regex e funções de validação |
| `excecoes.py` | Exceções personalizadas (`FormatoInvalidoError`, `IdadeInvalidaError`) |
| `dados.csv` | Arquivo de entrada de exemplo (10 registros, 6 com erro proposital) |
| `dados_sem_coluna.csv` | Exemplo para demonstrar o `KeyError` (coluna ausente) |
| `relatorio.txt` | Relatório gerado na última execução |

## Como executar

```bash
python3 analisador.py                       # analisa dados.csv
python3 analisador.py outro_arquivo.csv     # analisa outro arquivo
```

## Validações aplicadas (regex)

| Campo | Padrão | Justificativa |
|---|---|---|
| E-mail | `^[\w.+-]+@[\w-]+(\.[\w-]+)+$` | Exige usuário, `@`, domínio e ao menos uma extensão (`.com`, `.com.br`) |
| CPF | `^\d{3}\.\d{3}\.\d{3}-\d{2}$` | Formato oficial com pontos e hífen: `000.000.000-00` |
| Telefone | `^\(\d{2}\)\s?9?\d{4}-\d{4}$` | DDD entre parênteses; aceita fixo (8 dígitos) e celular (9 dígitos) |
| Data | `^(0[1-9]\|[12]\d\|3[01])/(0[1-9]\|1[0-2])/\d{4}$` | `dd/mm/aaaa` com dia 01–31 e mês 01–12 (rejeita mês 13) |

`^` e `$` garantem que o campo inteiro corresponda ao padrão, não só um trecho. Todos os padrões usam raw strings (`r"..."`).

## Exceções tratadas

| Exceção | Onde | Tratamento |
|---|---|---|
| `FileNotFoundError` | abertura do arquivo | mensagem amigável, o programa não quebra |
| `KeyError` | coluna obrigatória ausente no CSV | informa qual coluna está faltando |
| `ValueError` | `int()` da idade com texto (ex.: `vinte`) | registro marcado como inválido |
| `FormatoInvalidoError` (personalizada) | campo fora do padrão regex | registro marcado como inválido com o motivo |
| `IdadeInvalidaError` (personalizada) | idade fora de 0–120 | registro marcado como inválido |

O fluxo principal usa `try / except / else / finally`: o `else` só gera o relatório se a leitura deu certo e o `finally` sempre imprime "Análise finalizada.". Os arquivos são abertos com `with open(..., encoding="utf-8")`.

## Exemplo de entrada (`dados.csv`)

```csv
nome,email,cpf,telefone,data_nascimento,idade
Ana Souza,ana.souza@email.com,123.456.789-00,(81) 98765-4321,15/03/1998,28
Bruno Lima,bruno@empresa.com.br,987.654.321-11,(11) 3456-7890,02/11/1985,40
Carla Mendes,carla.mendes@,111.222.333-44,(21) 99876-5432,20/07/2000,26
Diego Rocha,diego.rocha@email.com,12345678900,(31) 91234-5678,10/01/1995,31
Eduarda Alves,eduarda@email.com,222.333.444-55,81 987654321,05/05/1990,36
Felipe Costa,felipe.costa@gmail.com,333.444.555-66,(85) 98888-7777,31/13/1992,34
Gabriela Nunes,gabi.nunes@outlook.com,444.555.666-77,(41) 97777-6666,22/09/2001,vinte
Henrique Dias,henrique@email.com,555.666.777-88,(51) 96666-5555,18/12/1880,145
Isabela Martins,isa.martins@email.com,666.777.888-99,(61) 95555-4444,29/02/1996,30
João Pereira,joao.pereira@email.com,777.888.999-00,(71) 94444-3333,08/08/1988,38
```

## Exemplo de saída

```
============================================================
               RELATÓRIO DE ANÁLISE DE DADOS                
============================================================

REGISTROS VÁLIDOS (4):
  ✔ Ana Souza            ana.souza@email.com          123.456.789-00
  ✔ Bruno Lima           bruno@empresa.com.br         987.654.321-11
  ✔ Isabela Martins      isa.martins@email.com        666.777.888-99
  ✔ João Pereira         joao.pereira@email.com       777.888.999-00

REGISTROS INVÁLIDOS (6):
  ✘ Linha 4 - Carla Mendes
      • email em formato inválido: 'carla.mendes@'
  ✘ Linha 5 - Diego Rocha
      • cpf em formato inválido: '12345678900'
  ✘ Linha 6 - Eduarda Alves
      • telefone em formato inválido: '81 987654321'
  ✘ Linha 7 - Felipe Costa
      • data_nascimento em formato inválido: '31/13/1992'
  ✘ Linha 8 - Gabriela Nunes
      • idade não numérica: 'vinte'
  ✘ Linha 9 - Henrique Dias
      • idade fora do intervalo permitido (0-120): 145

ESTATÍSTICAS:
  Total de registros:  10
  Registros válidos:   4
  Registros inválidos: 6
  Taxa de aprovação:   40.0%
============================================================
```
