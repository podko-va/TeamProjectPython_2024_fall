# test/test_header_component.py
import allure
from playwright.sync_api import sync_playwright
from pages.header import open_product_url, test_header_component

@allure.feature('Header')
def test_open_page_and_check_header():
    """Тест на открытие страницы и проверку хедера."""
    with allure.step('Launch browser and create context'):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)  # Вы можете установить headless=True для безголового режима
            context = browser.new_context()
            page = context.new_page()

            # Открытие страницы
            open_product_url(page)

            # Тест на проверку хедера
            test_header_component(page)

            # Закрытие браузера
            with allure.step('Close browser'):
                browser.close()
