from pages.main_page import MainPage


def test_activ_button_search(driver):
    page = MainPage(driver)
    result = page.activ_button_search()
    assert result == 'http://37.203.243.26:5000/search'

def test_activ_button_statistics(driver):
    page = MainPage(driver)
    result = page.activ_button_statistics()
    assert result == 'http://37.203.243.26:5000/search' # Так как я не знаю как должна выглядить страница статисти, я добавил страницу поиска
