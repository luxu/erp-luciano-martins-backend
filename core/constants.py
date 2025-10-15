INATIVO, ATIVO = False, True
STATUS = (
    (ATIVO, "Ativa"),
    (INATIVO, "Inativa"),
)

CREDITO, DEBITO, TRANSFERENCIA = "C", "D", "T"
CARTAO = (
    (CREDITO, "Crédito"),
    (DEBITO, "Débito"),
    (TRANSFERENCIA, "Transferência"),
)

FIXA, VARIAVEL = "F", "V"
EXPENSETYPE = (
    (FIXA, 'Fixa'),
    (VARIAVEL, 'Variável')
)