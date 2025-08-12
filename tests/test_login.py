import allure
from config.config import BASE_URL
from pages.login_page import LoginPage


@allure.feature("Авторизация пользователя")
@allure.story("Авторизация пользователя с корректными данными")
@allure.title("Успешная авторизация с валидными данными")
@allure.description("Тест проверяет успешную авторизацию пользователя с валидными username и password")
def test_successful_login(page):
    username = "standard_user"
    password = "secret_sauce"

    with allure.step("Инициализируем LoginPage"):
        login_page = LoginPage(page)
    with allure.step("Переходим на страницу авторизации"):
        login_page.open(BASE_URL)
    with allure.step(f"Пытаемся залогиниться с username={username} и password={password}"):
        login_page.login(username=username, password=password)
    with allure.step("Проверяем корректность url после авторизации"):
        assert page.url == "https://www.saucedemo.com/inventory.html", \
            f"После попытки залогиниться - url страницы: {page.url}"
