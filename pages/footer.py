from playwright.sync_api import sync_playwright

# Локаторы для футера
class FooterLocators:
    FOOTER_TEXT = 'footer'  # CSS-селектор футера, где ищем текст

# Класс для работы с футером
class Footer:
    def __init__(self, page):
        self.page = page

    def open_base_page(self):
        self.page.goto('http://195.133.27.184/')  # Открыть сайт

    def scroll_to_footer(self):
        footer_element = self.page.locator(FooterLocators.FOOTER_TEXT)
        footer_element.scroll_into_view_if_needed()  # Скроллим к футеру

    def move_to_element(self):
        footer_element = self.page.locator(FooterLocators.FOOTER_TEXT)
        footer_element.hover()  # Наводим курсор на футер

    def is_visible_footer(self):
        footer_element = self.page.locator(FooterLocators.FOOTER_TEXT)
        assert footer_element.is_visible(), "Footer is not visible"  # Проверяем видимость футера

    def is_footer_text_correct(self):
        footer_element = self.page.locator(FooterLocators.FOOTER_TEXT)
        footer_text = footer_element.inner_text()
        assert "© 2024 Мыслеплав. Все права защищены." in footer_text, "Footer text is incorrect"  # Проверка текста

# Пример использования
def test_footer():
    with sync_playwright() as p:
        # Запуск браузера
        browser = p.chromium.launch(headless=False)  # Установите headless=True для безголового режима
        page = browser.new_page()

        # Создаем объект футера
        footer = Footer(page)

        # Открываем страницу
        footer.open_base_page()

        # Скроллим к футеру
        footer.scroll_to_footer()

        # Проверяем, что футер виден
        footer.is_visible_footer()

        # Проверяем, что текст в футере верный
        footer.is_footer_text_correct()

        # Закрываем браузер
        browser.close()
