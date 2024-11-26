import allure
import pytest


# Тест для проверки открытия главной страницы и наличия футера
@allure.feature("Main Page")
@allure.story("Open main page and check if footer is visible")
def test_main_page_has_footer(browser_management, visit_page):
    # Открываем главную страницу
    url = "http://195.133.27.184/"
    
    with allure.step("Open the main page"):
        visit_page(url, browser_management)
    
    # Проверяем наличие футера
    with allure.step("Check if the footer is visible"):
        footer_selector = "footer"  # предполагаем, что футер - это HTML тег <footer>
        
        # Проверка, что футер видим
        footer = browser_management.locator(footer_selector)
        assert footer.is_visible(), "Footer is not visible"