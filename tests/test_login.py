import allure
import pytest
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


@allure.feature("Авторизация пользователя")
@allure.story("Авторизация пользователя с некорректными данными")
@allure.title("Авторизация пользователя с некорректными username и password")
@allure.description(
    "Тест проверяет, что при попытке входа с невалидными данными отображаются соответствующие сообщения об ошибке"
)
@pytest.mark.parametrize("username, password, error_message", [
    ("", "", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("not_standard_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", "not_secret_sauce", "Epic sadface: Username and password do not match any user in this service")
], ids=[
    "Username and password are empty",
    "Valid username and empty password",
    "Empty username and valid password",
    "Invalid username and valid password",
    "Valid username and invalid password"
])
def test_failed_login(page, username, password, error_message):
    with allure.step("Инициализируем LoginPage"):
        login_page = LoginPage(page)
    with allure.step("Переходим на страницу авторизации"):
        login_page.open(BASE_URL)
    with allure.step(f"Пытаемся залогиниться с username={username} и password={password}"):
        login_page.login(username=username, password=password)
    with allure.step("Проверяем, что отображается сообщение об ошибке"):
        assert login_page.is_error_displayed(), "Ожидалось сообщение об ошибке, но оно не появилось"
    with allure.step("Проверяем, корректность текста в сообщении об ошибке"):
        actual_error_message = login_page.get_error_text()
        assert actual_error_message == error_message, \
            f"Сообщение об ошибке не совпадает. Отображается {actual_error_message}"
