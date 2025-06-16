from selenium.webdriver.common.by import By

class MainPageLocators:
        search_button = (By.CSS_SELECTOR, '.btn-primary')
        statistics_button = (By.CSS_SELECTOR, '.btn-outline-secondary')

#query
class SearchPageLocators:
        search = (By.CSS_SELECTOR, '#query')

        sorting_name = (By.XPATH, '//option[@value="name"]')
        sorting_credit = (By.XPATH, '//option[@value="credit_amount"]')
        sorting_credit_status = (By.XPATH, '//option[@value="credit_status"]')
        sorting_delete_all = (By.XPATH, '//option[@value="delete_all"]')

        checkbox_active = (By.CSS_SELECTOR, '#active')
        checkbox_overdue = (By.CSS_SELECTOR, '#overdue')

        min_loan_amount = (By.CSS_SELECTOR, '#min_amount')

        search_button = (By.CSS_SELECTOR, '.btn-danger')
        clear_button = (By.CSS_SELECTOR, '.btn-secondary')
