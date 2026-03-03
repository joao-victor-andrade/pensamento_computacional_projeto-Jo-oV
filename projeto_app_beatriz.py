'''
CRUD

HAMBURGUERIA





'''



print('\n === Sistema De Hamburgueria === \n')


print("1. Cadastro")
print("2. Cardapio")
print("3. Solicitar pedido")
print("4. Pagamento")
print("5. Acompanhar entrega")
print('6. Cancelar pedido')
print("7. Sair")



while True:

    escolha_menu = input("\n escolha uma opção: ")
    if escolha_menu == '1':
        print("cadastro...")
        nome_do_cliente = input("Digite o nome do cliente")
        telefone_cliente = input("digite o telefone do cliente")

    elif escolha_menu == '0':

        print("Saindo do sistema, até logo!")
        break

    else:
        print("opção invalida. Por favor, tente novamente.")


