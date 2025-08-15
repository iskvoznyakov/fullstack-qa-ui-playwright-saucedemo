from pages.base_page import BasePage
from utils.decorators import log_action


class InventoryPage(BasePage):
    SHOPPING_CART_ICON = "#shopping_cart_container"
    SHOPPING_CART_BADGE = ".shopping_cart_badge"
    FILTER_DROPDOWN_LIST = "//select[@data-test='product-sort-container']"
    INVENTORY_ITEM = ".inventory_item"
    INVENTORY_ITEM_NAME = ".inventory_item_name"
    INVENTORY_ITEM_DESCRIPTION = ".inventory_item_desc"
    INVENTORY_ITEM_PRICE = ".inventory_item_price"

    @log_action
    def get_number_of_inventory_items(self):
        return self.page.locator(self.INVENTORY_ITEM).count()

    @log_action
    def _get_all_the_inventory_items(self):
        return self.page.locator(self.INVENTORY_ITEM)

    @log_action
    def cart_icon_is_visible(self):
        return self.page.locator(self.SHOPPING_CART_ICON).is_visible()

    @log_action
    def click_add_to_cart_for(self, item_name: str):
        items = self._get_all_the_inventory_items()
        count = items.count()
        for i in range(count):
            name = items.nth(i).locator(self.INVENTORY_ITEM_NAME).inner_text().strip()
            if name == item_name.strip():
                items.nth(i).locator("button").click()
                return
        raise ValueError(f"Товар с именем '{item_name}' не найден на странице")

    @log_action
    def get_number_of_items_in_cart(self):
        badge = self.page.locator(self.SHOPPING_CART_BADGE)
        return int(badge.inner_text()) if badge.is_visible() else 0

    @log_action
    def get_information_about_item_by_order(self, order: int):
        item = self._get_all_the_inventory_items().nth(order - 1)
        return {
            "Name": item.locator(self.INVENTORY_ITEM_NAME).inner_text(),
            "Description": item.locator(self.INVENTORY_ITEM_DESCRIPTION).inner_text(),
            "Price": item.locator(self.INVENTORY_ITEM_PRICE).inner_text()
        }

    @log_action
    def apply_sorting(self, visible_text: str):
        self.page.select_option(self.FILTER_DROPDOWN_LIST, label=visible_text)

    @log_action
    def get_all_item_names(self) -> list[str]:
        return [self._get_all_the_inventory_items().nth(i).locator(self.INVENTORY_ITEM_NAME).inner_text()
                for i in range(self._get_all_the_inventory_items().count())]

    @log_action
    def open_cart(self):
        self.page.locator(self.SHOPPING_CART_ICON).click()
