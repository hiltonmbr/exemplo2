# Entrada de dados

valor = input("Informe o valor da compra: ")

pagamento = input("""
              Informe o meio de pagamento: \n
              1 - Pix,  \n
              2 - Dinheiro, \n
              3 - Débito e  \n
              4 - Crédito:""")

# Estrutura de controle para erros
try:
    valor = float(valor)

    pagamento = int(pagamento)

    # Controlar para violação de regra de negócio
    if valor < 0:
        raise Exception("Informe um valor não negativo")

    if pagamento < 1 or pagamento > 4: 
        raise Exception("Informe 1, 2, 3 ou 4") 

    # Controlar para meio de pagamento
    if pagamento == 1:
        desconto = 0.10 
    elif pagamento == 2:
        desconto = 0.08
    elif pagamento == 3:
        desconto = 0.05
    else:
        desconto = 0

    valor_final = valor - valor * desconto # valor * (1  - desconto)
    print(f"O valor da sua compra foi R$ {valor:.2f}")
    print(f"O desconto total foi de {desconto * 100} %")
    print(f"O valor final é R$ {valor_final:.2f}")
except ValueError:
    print("Informe um número")
except Exception as error:
    print(error)
