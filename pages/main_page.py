from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss
from data.links import MAIN_PAGE_LINK
from data.page_data import MainPageData
from pages.base_page import BasePage
from pages.locators import BaseLocators as BL, HomeLocators
from pages.locators import NavigatorLocators as Nav
from pages.locators import HomeLocators as HL
from pages.locators import ErinRecommendLocators as ERL


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def open_page(self):
        self.visit(MAIN_PAGE_LINK)

    @property
    def privacy_cookie_policy_link(self):
        return s(BL.PRIVACY_COOKIE_POLICY_LOCATOR)

    @property
    def new_luma_yoga_collection_block(self):
        return s(BL.NEW_LUMA_YOGA_COLLECTION_BLOCK_LOCATOR)

    @property
    def new_luma_yoga_collection_block_info_text(self):
        return s(BL.NEW_LUMA_YOGA_COLLECTION_BLOCK_INFO_TEXT_LOCATOR)

    def scroll_to_privacy_cookie_policy_link(self):
        self.browser.driver.execute_script("arguments[0].scrollIntoView(true);", self.privacy_cookie_policy_link())

    def click_privacy_cookie_policy_link(self):
        self.privacy_cookie_policy_link.click()

    def is_menu_present(self):
        return s(Nav.NAV_MENU).should(be.present)

    def is_whats_new_link_present(self):
        return s(Nav.NAV_NEW).should(be.present)

    def find_whats_new_link(self):
        return s(Nav.NAV_NEW)

    def is_loaded(self):
        assert self.get_current_url() == MAIN_PAGE_LINK, MainPageData.error_message

    def find_cart_icon(self):
        return s(HL.CART_ICON)

    def is_cart_icon_present(self):
        return self.find_cart_icon().should(be.present)

    def find_counter_number(self):
        return s(HL.MINICART_COUNTER)

    def is_counter_number_present(self):
        return self.find_counter_number().should(be.present)

    def find_minicart(self):
        return s(HL.MINICART)

    def is_minicart_present(self):
        return self.find_minicart().should(be.present)

    def is_minicart_visible(self):
        return self.find_minicart().should(be.visible)

    def find_minicart_view(self):
        return s(HL.MINICART_VIEW)

    @property
    def is_minicart_view_present(self):
        return self.find_minicart_view().should(be.present)

    def is_minicart_view_enable(self):
        return self.find_minicart_view().should(be.enabled)

    def is_minicart_view_visible(self):
        return self.find_minicart_view().should(be.visible)

    def is_minicart_have_link(self):
        return self.find_minicart_view().should(
            have.attribute('href').value('https://magento.softwaretestingboard.com/checkout/cart/'))

    def is_erin_block_present(self):
        return s(ERL.HOME_ERIN_BLOCK).should(be.present)

    @staticmethod
    def handle_cookies_popup():
        if ss(HomeLocators.COOKIES_MSG):
            s(HomeLocators.CONSENT_COOKIES_BTN).click()

    def add_item_to_cart(self, size, color, add_to_cart_button):
        s(size).click()
        s(color).click()
        s(add_to_cart_button).click()
