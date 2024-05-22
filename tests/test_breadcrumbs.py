import allure
from pages import breadcrumbs

@allure.link('https://trello.com/c/s9FJicG5')
@allure.feature('Breadcrumbs')
@allure.title('Verify that the breadcrumbs displayed and clickable')

def test_breadcrumbs(driver):
    breadcrumbs.open_page(driver)
    breadcrumbs.select_item(driver)
    breadcrumbs.is_clickable(driver)
    breadcrumbs.is_visible(driver)