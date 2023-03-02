from utils.helper import format_float_str_br_currency

class Product:
    count: int = 1

    def __init__(self: object, name: str, price: float) -> None:
        self.__code: int = Product.count
        self.__name: str = name
        self.__price: float = price
        Product.count += 1

    @property
    def code(self: object) -> int:
        return self.__code

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def price(self: object) -> float:
        return self.__price

    def __str__(self) -> str:
        return f'Código: {self.code} \nNome: {self.name} \nPreço: {format_float_str_br_currency(self.price)}'
    