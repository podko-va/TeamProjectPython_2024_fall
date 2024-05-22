import allure
from pages import breadcrumbs

@allure.link('https://trello.com/c/s9FJicG5')
@allure.feature('Breadcrumbs')
@allure.title('Verify that the breadcrumbs displayed and clickable')

def test_breadcrumbs(chromium):
    breadcrumbs.open_page(chromium)
    breadcrumbs.select_item(chromium)
    breadcrumbs.is_clickable(chromium)
    breadcrumbs.is_visible(chromium)