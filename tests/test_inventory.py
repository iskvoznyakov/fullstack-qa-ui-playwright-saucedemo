import pytest
from pages.inventory_page import InventoryPage
import allure


@allure.feature("Список товаров")
@allure.story("Отображение товаров")
@allure.title("Проверка отображения товаров")
@allure.description("Тест проверяет, что после входа пользователю отображаются товары и корзина")
def test_inventory_items_visible_after_login(logged_in_page):
    with allure.step("Инициализируем InventoryPage"):
        inventory_page = InventoryPage(logged_in_page)
    with allure.step("Проверяем отображение иконки корзины после успешной авторизации"):
        assert inventory_page.cart_icon_is_visible(), f'Иконка корзины не отображается'
    with allure.step("Проверяем количество отображаемых товаров после успешной авторизации"):
        assert inventory_page.get_number_of_inventory_items() > 0, f'Не найдено товаров'


@allure.feature("Список товаров")
@allure.story("Сортировка товаров")
@allure.title("Проверка сортировки товаров")
@allure.description("Тест проверяет корректную сортировку товаров в зависимости от выбранной опции")
@pytest.mark.parametrize("sorting_option, expected_order", [
    ("Name (A to Z)", sorted),
    ("Name (Z to A)", lambda items: sorted(items, reverse=True))
], ids=[
    "Sorting 'Name (A to Z)'",
    "Sorting 'Name (Z to A)'"
])
def test_sorting_by_name(logged_in_page, sorting_option, expected_order):
    with allure.step("Инициализируем InventoryPage"):
        inventory_page = InventoryPage(logged_in_page)
    with allure.step(f"Применяем сортировку {sorting_option}"):
        inventory_page.apply_sorting(visible_text=sorting_option)
    with allure.step("Проверяем корректность сортировки"):
        items_names = inventory_page.get_all_item_names()
        assert items_names == expected_order(items_names), f"Сортировка {sorting_option} работает некорректно"


@allure.feature("Список товаров")
@allure.story("Добавление товаров")
@allure.title("Проверка добавления товара")
@allure.description("Тест проверяет корректное добавление товара в корзину")
def test_add_one_item_to_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    item_name = inventory_page.get_information_about_item_by_order(1)["Name"]
    inventory_page.click_add_to_cart_for(item_name)
    assert inventory_page.get_number_of_items_in_cart() == 1, f"Товар '{item_name}' не добавлен в корзину"
