from selene import query
from selene.support.shared.jquery_style import s
from selenium.webdriver import Keys

from pages.locators import ProductLocators as PL, HomeLocators as HL
from selene.support.conditions import be


def select_product_size(size):
    s(f'[option-label={size}]').click()


def select_product_color(color):
    s(f'[option-label={color}]').click()


def check_radiant_tee_name_in_minicart_is_visible():
    s(HL.MINICART_RADIANT_TEE_NAME).should(be.visible)


def select_product_quantity(qty):
    s(PL.RADIANT_TEE_QTY).click()
    s(PL.RADIANT_TEE_QTY).type(Keys.DELETE)
    s(PL.RADIANT_TEE_QTY).type(qty)


def add_product_to_cart():
    s(PL.ADD_TO_CART_BUTTON).click()
    s(PL.ADDING_TO_CART_SUCCESSFULL_MSG).wait_until(be.visible)


def check_minicart_subtotal(qty):
    product_price = float(s(PL.PRODUCT_PRICE).get(query.text).strip('$'))
    subtotal = float(s(HL.MINICART_SUBTOTAL).get(query.text).strip('$'))
    assert subtotal == round(product_price * int(qty), 2)


def check_minicart_quantity(qty):
    minicart_qty = s(HL.MINICART_PRODUCT_QTY).get(query.attribute("data-item-qty"))
    assert minicart_qty == qty


def check_cart_icon_shows_correct_number(qty):
    cart_icon_qty = s(HL.CART_COUNTER).get(query.text)
    assert cart_icon_qty == qty
