from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss
from pages.locators import SalePageLocators, BaseLocators
import allure


@allure.link('https://trello.com/c/RF0vkTGW')
def test_011_001_001_sale_breadcrumbs_is_correct():
    browser.open(SalePageLocators.LINK_SALE)
    ss(BaseLocators.BREADCRUMBS_LIST).should(have.texts('Home', 'Sale'))

