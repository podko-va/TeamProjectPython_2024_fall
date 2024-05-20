import allure
from selene import browser
from pages.header import Header


class TestHeader:
    @allure.link('https://trello.com/c/76HixPum')
    @allure.title('TC_003.003.004 | Header > Cart> Verify counter number')
    def test_003_003_004_verify_cart_counter_number(self):
        page = Header(browser=browser)
        page.visit_desire_fitness_tee_page()
        page.add_product_to_cart_with_qty('M', 'Orange', '1')
        page.is_cart_counter_shows_correct_number('1')
