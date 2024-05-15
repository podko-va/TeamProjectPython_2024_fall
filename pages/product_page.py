from pages.base_page import BasePage
from pages.locators import ProductLocators as PL, HomeLocators as HL


class ProductPage(BasePage):

    def open_radiant_tee_page(self):
        self.visit(PL.RADIANT_TEE_URL)
        return self

    def is_radiant_tee_title_visible(self):
        self.assert_visible_of_element(PL.RADIANT_TEE_TITLE)

    def is_radiant_tee_img_visible(self):
        self.assert_visible_of_element(PL.RADIANT_TEE_IMG)

    def is_radiant_tee_price_is_visible(self):
        self.assert_visible_of_element(PL.RADIANT_TEE_PRICE)

    def is_radiant_tee_name_visible_in_minicart(self):
        self.assert_visible_of_element(HL.MINICART_RADIANT_TEE_NAME)

