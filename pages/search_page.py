from utils.config import Config
from pages.base_page import BasePage
from utils.locators import SearchPageLocators



class SearchPage(BasePage):
    def customer_search(self):
        self.open(Config.search_page)
        self.find(SearchPageLocators.search).send_keys('Иван')
        self.find(SearchPageLocators.clear_button).click()
        customers = self.find_all(SearchPageLocators.customers)
        return len(customers)
