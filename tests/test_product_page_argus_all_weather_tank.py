import allure
from selene import browser

import data.links as DL
from pages.base_page import BasePage
from pages.locators import ProductLocators as PL


@allure.suite('US_002.001 | Page of any product')
class TestArgusAllWeatherTankPage:
    @allure.link('https://trello.com/c/dzrER7dp')
    @allure.title('TC_002.001.012 I Argus All-Weather Tank> Check whether the product name, its price and photo are displayed')
    def test_argus_allweather_tank_page_visibility_of_product_name_price_photo(self, login):
        page = BasePage(browser=browser)
        page.visit(DL.ARGUS_ALL_WEATHER_TANK_URL)
        page.assert_text_of_element(PL.PRODUCT_TITLE, PL.ARGUS_ALL_WEATHER_TANK_PRODUCT_NAME_TEXT)
        page.assert_present_of_element(PL.PRODUCT_PRICE_BASE)
        page.assert_present_of_element(PL.PRODUCT_IMAGE_BASE)
