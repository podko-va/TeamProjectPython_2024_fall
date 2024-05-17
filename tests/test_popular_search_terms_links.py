import allure
from selene import browser, be, have, by
from selene.support.shared.jquery_style import s
from data.links import POPULAR_SEARCH_TERMS_URL
from pages.locators import SearchTermsLocators

@allure.link('https://trello.com/c/Q7ZoeJxT/286-tc015003001-popular-search-terms-search-results-check-after-clicking-the-popular-search-terms-links')
@allure.title('TC_015.003.001 | Popular Search Terms > Search results check after clicking the "Popular Search Terms" links')
def test_popular_search_terms_links_results():
    browser.open(POPULAR_SEARCH_TERMS_URL)
    s('//*[@id="maincontent"]/div[3]/div/ul/li[32]/a').click()
    assert browser.element(SearchTermsLocators.PRODUCT_ITEM_NAMES).matching(have.text('Jacket'))







