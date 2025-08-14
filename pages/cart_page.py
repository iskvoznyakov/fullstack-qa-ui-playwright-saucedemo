from pages.base_page import BasePage
from utils.decorators import log_action


class CartPage(BasePage):
    CONTINUE_SHOPPING_BUTTON = "#continue-shopping"
    CHECKOUT_BUTTON = "#checkout"
    REMOVE_BUTTON = "button[id*='remove']"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"

    @log_action
    def get_cart_items(self):
        return self.find(self.ITEM_NAME).all_text_contents()

    @log_action
    def get_number_of_cart_items(self):
        return self.find(self.ITEM_NAME).count()

    @log_action
    def get_cart_prices(self):
        return self.find(self.ITEM_PRICE).all_text_contents()

    @log_action
    def proceed_to_checkout(self):
        return self.click(self.CHECKOUT_BUTTON)

    @log_action
    def continue_shopping(self):
        return self.click(self.CONTINUE_SHOPPING_BUTTON)

    @log_action
    def remove_item_from_cart_by_name(self, item_name: str):
        item = self.page.locator(".cart_item", has_text=item_name)
        if item.count() == 0:
            raise ValueError(f"Item '{item_name}' not found in cart")
        item.locator("button").first.click()
