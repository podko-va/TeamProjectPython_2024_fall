from selene import query, have, be, browser
from selene.support.shared.jquery_style import ss

LIST_OF_SEARCH_TERMS = '[class="item"] a'
url = 'https://magento.softwaretestingboard.com/search/term/popular/'


def open():
    browser.open(url)


def order_search_terms():
    keyword_elements = ss(LIST_OF_SEARCH_TERMS)
    keyword_texts = [k.get(query.attribute("text")).replace('\n', '') for k in keyword_elements]
    keyword_elements.should(have.exact_texts(sorted(keyword_texts)))


def visibility_of_the_list():
    list_items = ss(LIST_OF_SEARCH_TERMS)
    for item in list_items:
        item.should(be.visible)
