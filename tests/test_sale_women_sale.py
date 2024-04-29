import pytest
from pages.locators import SalePageLocators, BaseLocators
from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss
import allure

@pytest.mark.xfail
@allure.link('TC_011.011.001 | Sale > Women Sale > Breadcrumbs are visible and correct')
def test_011_011_001_women_sale_breadcrumbs_is_correct():
    # assert error !!! 'Sale' is missing
    browser.open(SalePageLocators.LINK_WOMEN_SALE)
    ss(BaseLocators.BREADCRUMBS_LIST).should(have.texts('Home', 'Sale', 'Women Sale'))

