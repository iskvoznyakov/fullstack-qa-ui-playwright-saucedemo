from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
import allure


@allure.feature("Корзина товаров")
@allure.story("Добавление товаров в корзину")
@allure.title("Проверка добавления товаров в корзину")
@allure.description("Тест проверяет, что в корзине отображается добавленный товар")
def test_item_is_added_to_cart(logged_in_page):
    with allure.step("Инициализируем InventoryPage"):
        inventory_page = InventoryPage(logged_in_page)
    with allure.step("Добавляем 1 товар в корзину"):
        item_name = inventory_page.get_information_about_item_by_order(1)["Name"]
        inventory_page.click_add_to_cart_for(item_name)
    with allure.step("Открываем корзину"):
        inventory_page.open_cart()
    with allure.step("Инициализируем CartPage"):
        cart_page = CartPage(logged_in_page)
    with allure.step("Проверяем количество товаров в корзине"):
        number_of_cart_items = cart_page.get_number_of_cart_items()
        assert number_of_cart_items == 1, f'Количество товаров в корзине не 1, а {number_of_cart_items}'


@allure.feature("Корзина товаров")
@allure.story("Удаление товаров из корзины")
@allure.title("Проверка удаления товаров из корзины")
@allure.description("Тест проверяет, что в корзине не отображается удалённый товар")
def test_item_is_removed_from_cart(logged_in_page):
    with allure.step("Инициализируем InventoryPage"):
        inventory_page = InventoryPage(logged_in_page)
    with allure.step("Добавляем 1 товар в корзину"):
        item_name = inventory_page.get_information_about_item_by_order(1)["Name"]
        inventory_page.click_add_to_cart_for(item_name)
    with allure.step("Открываем корзину"):
        inventory_page.open_cart()
    with allure.step("Инициализируем CartPage"):
        cart_page = CartPage(logged_in_page)
    with allure.step("Проверяем количество товаров в корзине"):
        number_of_cart_items = cart_page.get_number_of_cart_items()
        assert number_of_cart_items == 1, f'Количество товаров в корзине не 1, а {number_of_cart_items}'
    with allure.step("Удаляем добавленный товар из корзины"):
        cart_page.remove_item_from_cart_by_name(item_name)
    with allure.step("Проверяем количество товаров в корзине"):
        number_of_cart_items = cart_page.get_number_of_cart_items()
        assert number_of_cart_items == 0, f'Количество товаров в корзине не 0, а {number_of_cart_items}'
