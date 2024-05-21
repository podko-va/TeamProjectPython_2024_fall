import allure
from selene import browser

from data.links import POPULAR_SEARCH_TERMS
from data.page_data import PopularSearchTermsData as PSTD
from pages.locators import PopularSearchTermsLocators as PSTL
from pages.popular_search_terms_page import PopularSearchTerms


@allure.suite("US_015.003 | Popular Search Terms > Redirection")
class TestPopularSearchTerms:
    @allure.link("https://trello.com/c/YgMgvvIu")
    @allure.title("TC_015.003.002 | Popular Search Terms > Redirection > The page title contains "
                  "Search results for: and the keyword")
    def test_title_search_results_for(self):
        page = PopularSearchTerms(browser)
        page.visit(POPULAR_SEARCH_TERMS)
        page.click_on_link(PSTL.HOODIE_LINK)

        page.assert_text_of_element(PSTL.SEARCH_RESULTS_HEADER, PSTD.result_page_header)

    @allure.link('https://trello.com/c/Q7ZoeJxT')
    @allure.title('TC_015.003.001 | Popular Search Terms > Search results check after clicking the'
                  '"Popular Search Terms" links')
    def test_popular_search_terms_links_results(self):
        page = PopularSearchTerms(browser)
        page.visit(POPULAR_SEARCH_TERMS)
        page.click_on_link(PSTL.JACKET_LINK)

        page.assert_text_of_element(PSTL.PRODUCT_ITEM_NAMES, PSTD.jacket_item_results)

