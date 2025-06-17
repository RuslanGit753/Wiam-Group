from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def wait_for_url(self, pattern: str, timeout=10) -> None:
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(pattern))

    def find_all(self, locator, timeout=5):
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_any_elements_located(locator))
