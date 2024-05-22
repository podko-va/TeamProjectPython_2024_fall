from selene import browser, be, have
from selene.support.shared.jquery_style import s

url = 'https://magento.softwaretestingboard.com'
nav_women = '//*[@id="ui-id-4"]'
nav_tops = '//*[@id="ui-id-9"]'
nav_jackets = '//*[@id="ui-id-11"]'
women_crumb = '/html/body/div[2]/div[2]/ul/li[2]'
breadcrumbs = '/html/body/div[2]/div[2]/ul'
current_item = '//li[@class = "item category20"]'

def open_page():
    browser.open(url)

def nav_women_tops_jackets():
    s(nav_women).hover()
    s(nav_tops).hover()
    s(nav_jackets).hover().click()

def click_to_women_crumb():
    s(women_crumb).click()

def is_visible():
    s(breadcrumbs).should(be.visible)
    s(current_item).should(have.text('Women'))
