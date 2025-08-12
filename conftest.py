import pytest
from config.config import BASE_URL
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright
from utils import allure_helpers


@pytest.fixture(scope="function")
def page():
    """Фикстура, создающая браузер и вкладку Playwright."""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--incognito"]
        )
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080}
        )
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture
def logged_in_page(page):
    """Фикстура с уже залогиненным пользователем."""
    login_page = LoginPage(page)
    login_page.open(BASE_URL)
    login_page.login("standard_user", "secret_sauce")
    yield page


# Хук для автоматического добавления скрина и HTML в Allure при падении теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("page")
        if page:
            allure_helpers.attach_screenshot(page, name="Failure Screenshot")
            allure_helpers.attach_page_source(page, name="Failure Page Source")
