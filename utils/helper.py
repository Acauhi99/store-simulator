from time import sleep


def format_float_str_br_currency(value: float) -> str:
    return f'R$ {value:,.2f}'

def verify_value():
    a = float(input('Digite o preço do produto: '))
    if a < 0:
        print('Digite um valor maior!')
        sleep(2)
        verify_value()
    if a > 100:
        print('Digite um valor menor!')
        sleep(2)
        verify_value()
    return a
