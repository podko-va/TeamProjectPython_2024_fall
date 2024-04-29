from pages.locators import SearchTermsLocators as ST
from pages.locators import BaseLocators as Base
from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss
import allure


@allure.link('https://trello.com/c/tnpU7rqU')
def test_015_001_001_search_terms_title_is_visible():
    browser.open(ST.LINK_SEARCH_TERMS)
    s(Base.PAGE_TITLE).should(have.text("Popular Search Terms"))



