import allure
from selene import browser, by, be, have, support
from selene.support.shared.jquery_style import s


def open_page_with_navigate_block(url):
    browser.open(url)


def move_to_elements(text_data):
    elements = []
    for i in text_data:
        element = s(by.link_text(i))
        element.hover()
        element.should(be.existing)
        elements.append(element)
    return elements
