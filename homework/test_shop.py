"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def product_2():
    return Product("phone", 1477, "This is device for phone calls", 500)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity) == True
        assert product.check_quantity(product.quantity - 1) == True
        assert product.check_quantity(product.quantity + 1) == False

    def test_product_buy_full_quantity(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(product.quantity) is None

    def test_product_buy_one_product(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(1) is None

    def test_border_product_buy_quantity_minus_one_product(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(product.quantity - 1) is None

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError) as error_info:
            product.buy(1001)
        assert str(error_info.value) == "Товаров не хватает"


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_in_cart(self, cart, product):
        cart.add_product(product)
        assert product.name in cart.get_cart_info()

    def test_add_some_product_in_cart(self, cart, product, product_2):
        cart.add_product(product)
        cart.add_product(product_2)
        assert (f"Товар: {product.name} - {1} шт\n"
                f"Товар: {product_2.name} - {1} шт\n") == cart.get_cart_info()

    def test_add_by_count_product_in_cart_(self, cart, product):
        cart.add_product(product, 2)
        assert f"Товар: {product.name} - {2} шт\n" == cart.get_cart_info()

    def test_increase_count_product_in_cart_(self, cart, product):
        cart.add_product(product, 2)
        assert f"Товар: {product.name} - {2} шт\n" == cart.get_cart_info()
        cart.add_product(product)
        assert f"Товар: {product.name} - {3} шт\n" == cart.get_cart_info()

    def test_remove_product_position_from_cart(self, cart, product, product_2):
        cart.add_product(product, 2)
        cart.add_product(product_2)
        cart.remove_product(product)
        assert f"Товар: {product_2.name} - {1} шт\n" == cart.get_cart_info()

    def test_remove_one_product_from_cart(self, cart, product):
        cart.add_product(product, 2)
        cart.remove_product(product, 1)
        assert f"Товар: {product.name} - {1} шт\n" == cart.get_cart_info()

    def test_clear_cart(self, cart, product, product_2):
        cart.add_product(product, 3)
        cart.add_product(product_2, 1)
        cart.clear()
        assert cart.get_cart_info() == ""

    def test_cart_total_price(self, cart, product, product_2):
        cart.add_product(product, 1)
        cart.add_product(product_2, 1)
        assert cart.get_total_price() == float(product.price) + float(product_2.price)

    def test_buy_cart(self, cart, product):
        cart.add_product(product, 1)
        result = cart.buy()
        print(result)
        assert result == f"Товар {product.name} в кол-ве {1} шт куплен успешно\n"

    def test_buy_cart_with_some_products(self, cart, product, product_2):
        cart.add_product(product, 2)
        cart.add_product(product_2, 3)
        result = cart.buy()
        print(result)
        assert result == (f"Товар {product.name} в кол-ве {2} шт куплен успешно\n"
                          f"Товар {product_2.name} в кол-ве {3} шт куплен успешно\n")

    def test_buy_cart_more_than_have_quantity_of_product(self, cart, product):
        cart.add_product(product, product.quantity + 1)
        with pytest.raises(ValueError) as error_info:
            cart.buy()
        assert str(error_info.value) == f"Товара {product.name} не хватает на складе"
