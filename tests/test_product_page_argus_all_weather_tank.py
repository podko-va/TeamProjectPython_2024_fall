import allure
from selene import browser, have, be
from selene.support.shared.jquery_style import s

import data.links as DL
from pages.locators import ProductLocators as PL


@allure.suite('US_002.001 | Page of any product')
class TestArgusAllWeatherTankPage:
    @allure.link('https://trello.com/c/dzrER7dp')
    @allure.title('TC_002.001.012 I Argus All-Weather Tank> Check whether the product name, its price and photo are displayed')
    def test_argus_allweather_tank_page_visibility_of_product_name_price_photo(self, login):
        browser.open(DL.ARGUS_ALL_WEATHER_TANK_URL)
        s(PL.PRODUCT_TITLE).should(have.text(PL.ARGUS_ALL_WEATHER_TANK_PRODUCT_NAME_TEXT))
        s(PL.PRODUCT_PRICE_BASE).should(be.present)
        s(PL.PRODUCT_IMAGE_BASE).should(be.present)
