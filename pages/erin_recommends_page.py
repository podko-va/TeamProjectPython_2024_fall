from selene import browser, command
from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s
from pages.locators import ErinRecommendLocators as ERL
from data.links import *


class ErinRecommendsPage:
    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        self.browser.open(ERIN_RECOMMENDS_URL)

    def move_to_erin_page(self):
        s(ERL.HOME_ERIN_BLOCK).click()

    def check_current_url(self):
        return browser.driver.current_url

    def is_header_present(self):
        return s(ERL.PAGE_HEADER).should(be.present)

    def is_element_text_correct(self, element, text):
        return element.should(have.text(text))

    def scroll_to_footer(self):
        s(ERL.FOOTER).perform(command.js.scroll_into_view)

    def is_pagination_visible(self):
        return s(ERL.PAGINATION_CONTROL).should(be.visible)

    def click_next(self):
        return s(ERL.PAGE_NEXT).click()

    def verify_minimum_page_numbers(self, minimum_count):
        return browser.all(ERL.PAGINATION_CONTROL).should(have.size_greater_than_or_equal(minimum_count))

    def is_next_button_visible(self):
        return s(ERL.PAGE_NEXT).should(be.visible)


