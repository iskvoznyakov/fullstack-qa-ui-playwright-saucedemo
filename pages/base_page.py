from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError
from utils.logger import logger


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        logger.info(f"Переход на страницу: {url}")
        self.page.goto(url)

    def find(self, locator: str):
        logger.info(f"Поиск элемента: {locator}")
        return self.page.locator(locator)

    def click(self, locator: str):
        logger.info(f"Клик по элементу: {locator}")
        self.find(locator).click()

    def enter_text(self, locator: str, text: str):
        logger.info(f"Ввод '{text}' в: {locator}")
        element = self.find(locator)
        element.fill(text)

    def is_visible(self, locator: str) -> bool:
        logger.info(f"Проверка видимости {locator}")
        try:
            expect(self.find(locator)).to_be_visible(timeout=5000)  # 5 секунд
            return True
        except PlaywrightTimeoutError:
            return False

    def get_text(self, locator: str) -> str:
        logger.info(f"Получение текста из {locator}")
        return self.find(locator).inner_text()
