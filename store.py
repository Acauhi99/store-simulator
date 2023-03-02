from typing import List,Dict
from time import sleep
from models.product import Product
from utils.helper import *


products: List[Product] = []
shopping_cart: List[Dict[Product, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('==============================')
    print('======== ACAUHI STORE ========')
    print('==============================\n')

    print("Selecione uma opção abaixo")
    print('1 - Cadastrar Produto')
    print('2 - Listar Produtos')
    print('3 - Comprar Produto')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Finalizar Sistema')

    option = input('Digite a opção desejada: ')
    
    if option == '1':
        register_product()
    elif option == '2':
        list_products()
    elif option == '3':
        buy_products()
    elif option == '4':
        view_cart()
    elif option == '5':
        close_order()
    elif option == '6':
        print('Sistema finalizado!')
        sleep(2)
        exit(0)
    print('Opção inválida. Tente novamente.')
    sleep(1)
    menu()


    
def register_product() -> None:
    print('Cadastro de Produto.\n')
    try:
        name: str = input('Digite o nome do produto: ')
        price: float = float(verify_value())
        product: Product = Product(name, price)
        products.append(product)

        print(f"Produto '{product.name}' cadastrado com sucesso!")
        sleep(2)
        menu()
    except:
        print('Valor invalido!')
        sleep(2)
        menu()
    

def list_products() -> None:
    if not products:
        print("Não há produtos cadastrados.")
    print("Produtos disponíveis: \n")
    print('------------------------')

    for product in products:
        print(product)
        print('------------------------')
        sleep(1)
    sleep(2)
    menu()    

def buy_products() -> None:
    if not products:
        print("Não há produtos cadastrados.")
    print('===================== Produtos Disponíveis =====================\n')

    for product in products:
        print(product)
        print('------------\n')
        sleep(1)
    print('Informe o código do produto que deseja adicionar ao carrinho: ')
    code: int = int(input())

    product: Product = select_product_by_code(code)

    if product:
        if len(shopping_cart) > 0:
            there_is_on_cart: bool = False
            for item in shopping_cart:
                quantity: int = item.get(product)
                if quantity:
                    item[product] = quantity + 1
                    print(f'Possuem {quantity + 1} unidade(s) do produto {product.name} no carrinho!')
                    there_is_on_cart = True
                    sleep(2)
            if not there_is_on_cart:
                dict_product = {product: 1}
                shopping_cart.append(dict_product)
                print(f'O produto {product.name} foi adicionado ao carrinho!')
                sleep(2)
        else:
            item = {product: 1}
            shopping_cart.append(item)
            print(f'O produto {product.name} foi adicionado ao carrinho!')
            sleep(2)
    else:    
        print(f'O produto com o código {code} não foi encontrado.')
        sleep(2)
    menu()

def view_cart() -> None:
    if not shopping_cart:
        print("O carrinho está vazio.")
    print('Carrinho de compras: ')
    for item in shopping_cart:
        for datas in item.items():
            print(datas[0])
            print(f'Quantidade: {datas[1]}\n')
            sleep(1)
    sleep(2)
    menu()    

def close_order() -> None:
    if not shopping_cart:
        print("O carrinho está vazio.")
    else:
        total: float = 0

        print("Carrinho de compras:")
        for item in shopping_cart:
            for datas in item.items():
                print(datas[0])
                print(f'Quantidade: {datas[1]}\n')
                total += datas[0].price * datas[1]
            sleep(1)
        print(f'Seu total é {format_float_str_br_currency(total)}')

        confirmation = input("Deseja confirmar o pedido? (s/n)").strip().lower()

        if confirmation == "s":
            print("Pedido confirmado. Obrigado pela compra!")
            shopping_cart.clear()
            sleep(5)
        else:
            print("Pedido cancelado.")
    sleep(2)
    menu()

def select_product_by_code(code: int) -> Product:    
    select_product: Product = None

    for product in products:
        if product.code == code:
            select_product = product
    return select_product

if __name__ == '__main__':
    main()
