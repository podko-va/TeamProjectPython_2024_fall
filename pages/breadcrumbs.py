from selene import browser, be, have
from selene.support.shared.jquery_style import s

URL = 'https://magento.softwaretestingboard.com'
NAV_WOMEN = '//*[@id="ui-id-4"]'
NAV_TOPS = '//*[@id="ui-id-9"]'
NAV_JACKETS = '//*[@id="ui-id-11"]'
WOMEN_CRUMB = '/html/body/div[2]/div[2]/ul/li[2]'
BREADCRUMBS = '/html/body/div[2]/div[2]/ul'
CURRENT_ITEM = '//li[@class = "item category20"]'

def open_page():
    browser.open(URL)

def nav_women_tops_jackets():
    s(NAV_WOMEN).hover()
    s(NAV_TOPS).hover()
    s(NAV_JACKETS).hover().click()

def click_to_women_crumb():
    s(WOMEN_CRUMB).click()

def is_visible():
    s(BREADCRUMBS).should(be.visible)
    s(CURRENT_ITEM).should(have.text('Women'))
