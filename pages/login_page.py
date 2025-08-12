from pages.base_page import BasePage
from utils.decorators import log_action


class LoginPage(BasePage):
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = ".error-message-container"

    @log_action
    def login(self, username: str, password: str):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    @log_action
    def is_error_displayed(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)

    @log_action
    def get_error_text(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)
