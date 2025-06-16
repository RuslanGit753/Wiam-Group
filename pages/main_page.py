from utils.config import Config
from pages.base_page import BasePage
from utils.locators import MainPageLocators


class MainPage(BasePage):
    def activ_button_search(self):
        self.open(Config.BASE_URL)
        button = self.find(MainPageLocators.search_button)
        activ_button = not button.get_attribute('disabled')

        if activ_button == True:
            self.find(MainPageLocators.search_button).click()
            self.wait_for_url(Config.search_page)
            return self.driver.current_url
        else:
            print('Кнопка поиска не активна!')


    def activ_button_statistics(self):
        self.open(Config.BASE_URL)
        button = self.find(MainPageLocators.statistics_button)
        activ_button = not button.get_attribute('disabled')

        if activ_button == True:
            self.find(MainPageLocators.statistics_button).click()
            self.wait_for_url(Config.search_page)
            return self.driver.current_url
        else:
            print('Кнопка статистики не активна!')
