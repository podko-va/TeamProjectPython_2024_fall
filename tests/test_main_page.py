# test/test_main_page.py
import allure
from playwright.sync_api import sync_playwright
from pages.main_page import open_main_page, check_footer_visibility

@allure.feature("Main Page")
@allure.story("Open main page and check if footer is visible")
def test_main_page_has_footer():
    """Тест для проверки открытия главной страницы и наличия футера."""
    with allure.step('Launch browser and create context'):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)  # Установите headless=True для безголового режима
            context = browser.new_context()
            page = context.new_page()

            # Открытие главной страницы
            open_main_page(page)

            # Проверка наличия футера
            check_footer_visibility(page)

            # Закрытие браузера
            with allure.step('Close browser'):
                browser.close()
