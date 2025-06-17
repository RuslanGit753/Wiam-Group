from pages.search_page import SearchPage


def test_customer_search(driver):
    page = SearchPage(driver)
    result = page.customer_search()
    assert result > 0
