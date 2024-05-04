from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss

url = "https://magento.softwaretestingboard.com/wishlist/"
__product_url = "https://magento.softwaretestingboard.com/aether-gym-pant.html?qty=1#143=&93="

__ADD_TO_WISHLIST = "a[class='action towishlist']"
__SUCCESS_MSG = "div[class='message-success success message']"
__ITEM_CARD = "(//div[@class='product-item-info'])[1]"
__REMOVE_ITEM = "//div[@class='product-item-actions']/a[@class='btn-remove action delete']"


def visit(url=url):
    browser.open(url)


def click_update():
    s(".update").click()


def should_be_clickable():
    s(".update").should(be.clickable)


def url_should_contain(param):
    browser.should(have.url_containing(param))

def remove_item():
    s(__REMOVE_ITEM).should(be.visible).click()

def add_item_to_wish_list():
    visit(__product_url)
    s(__ADD_TO_WISHLIST).should(be.clickable).click()
    s(__SUCCESS_MSG).should(be.visible)

def hover_over_item():
    s(__ITEM_CARD).should(be.present).hover()

def is_item_removed():
    s(__SUCCESS_MSG).should(have.text("has been removed from your Wish List."))
