import data.page_data
import data.links
import pages
from pages import locators
from pages import sign_in
import allure
from selene import browser, be, have


@allure.title("check value of selected items to compare products section")
def test_check_quantity_value_in_compare_product_section():
    browser.open(pages.locators.LoginLocators.LINK_LOGIN)
    sign_in.login(data.page_data.SignInData.email, data.page_data.SignInData.password)
    browser.element(pages.locators.SalePageLocators.SALE_TAP).click()
    browser.should(have.url(data.links.SALE_SECTION_LINK))
    browser.element(pages.locators.SaleWomenDealsLocators.JACKETS).click()
    browser.should((have.url(data.links.WOMEN_JACKET_LINK)))
    browser.element(pages.locators.SaleWomenDealsLocators.ITEM_ONE).click()
    browser.element(pages.locators.SaleWomenDealsLocators.ITEM_TWO).click()
    browser.element(pages.locators.SaleWomenDealsLocators.QUANTITY_ITEMS).should(have.text("2 items"))
