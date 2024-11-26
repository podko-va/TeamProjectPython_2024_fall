# test/test_page_elements.py
import allure
from playwright.sync_api import sync_playwright

product_url = 'http://195.133.27.184'

def open_product_url(page):
    """Открывает указанный URL."""
    with allure.step('Open product URL'):
        page.goto(product_url)

@allure.feature('Page elements')
def test_text_on_page():
    """Тест на проверку текста на странице."""
    with allure.step('Launch browser and create context'):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)  # Вы можете установить headless=True для безголового режима
            context = browser.new_context()
            page = context.new_page()

            # Открытие страницы
            open_product_url(page)

            # Проверка текста на странице
            with allure.step('Check if specific text is present on the page'):
                text_locator = page.locator('text=Your expected text here')  # Замените на реальный текст
                assert text_locator.is_visible(), "Text is not visible on the page"

            # Закрытие браузера
            with allure.step('Close browser'):
                browser.close()
