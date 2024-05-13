import data.page_data
import data.links
import pages
from pages import locators
from pages import sign_in
from selene import browser, be, have, by
from selene.support.shared.jquery_style import s


def compare_items_values():
    browser.open(pages.locators.LoginLocators.LINK_LOGIN)
    sign_in.login(data.page_data.SignInData.email, data.page_data.SignInData.password)
    browser.element(pages.locators.SalePageLocators.SALE_TAP).click()
    browser.should(have.url(data.links.SALE_SECTION_LINK))
    if not s(by.text("You have no items to compare.")).should(be.visible):
        browser.element(pages.locators.SaleWomenDealsLocators.JACKETS).click()
        s(pages.locators.SaleWomenDealsLocators.ELEMENT_ONE).hover()
        s(pages.locators.SaleWomenDealsLocators.ADD_TO_COMPARE_BTN_ONE).hover().click()
        s(pages.locators.SaleWomenDealsLocators.ELEMENT_TWO).wait_until(be.present)
        s(pages.locators.SaleWomenDealsLocators.ELEMENT_TWO).hover()
        s(pages.locators.SaleWomenDealsLocators.ADD_TO_COMPARE_BTN_ONE_TWO).wait_until(be.present)
        s(pages.locators.SaleWomenDealsLocators.ADD_TO_COMPARE_BTN_ONE_TWO).hover().click()
        s(pages.locators.SaleWomenDealsLocators.QUANTITY_ITEMS).should(have.text("2 items"))
        s(by.id("compare-clear-all")).click()
        s(by.css("button[class='action-primary action-accept']")).wait_until(be.present)
        s(by.css("button[class='action-primary action-accept']")).click()
        s(by.text("You cleared the comparison list.")).wait_until(be.present)
        s(by.text("You cleared the comparison list.")).should(have.text("You cleared the comparison list."))
    elif s(by.text("You have no items to compare.")).should(be.visible):
        browser.element(pages.locators.SaleWomenDealsLocators.JACKETS).click()
        s(pages.locators.SaleWomenDealsLocators.ELEMENT_ONE).hover()
        s(pages.locators.SaleWomenDealsLocators.ADD_TO_COMPARE_BTN_ONE).hover().click()
        s(pages.locators.SaleWomenDealsLocators.ELEMENT_TWO).wait_until(be.present)
        s(pages.locators.SaleWomenDealsLocators.ELEMENT_TWO).hover()
        s(pages.locators.SaleWomenDealsLocators.ADD_TO_COMPARE_BTN_ONE_TWO).wait_until(be.present)
        s(pages.locators.SaleWomenDealsLocators.ADD_TO_COMPARE_BTN_ONE_TWO).hover().click()
        s(pages.locators.SaleWomenDealsLocators.QUANTITY_ITEMS).should(have.text("2 items"))
        s(by.id("compare-clear-all")).click()
        s(by.css("button[class='action-primary action-accept']")).wait_until(be.present)
        s(by.css("button[class='action-primary action-accept']")).click()
        s(by.text("You cleared the comparison list.")).wait_until(be.present)
        s(by.text("You cleared the comparison list.")).should(have.text("You cleared the comparison list."))