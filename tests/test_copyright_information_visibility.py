import pytest
import data.links as l
from pages.copyright_info import scroll_to, is_copyright_info_visible
from selene import browser


links = [l.BASE_URL, 
         l.GEAR_BAGS_URL,
         l.SALE_PAGE_URL, 
         l.WHATS_NEW_PAGE_LINK, 
         l.TRAINING_PAGE_URL, 
         ]

FOOTER = "small[class='copyright']"

@pytest.mark.parametrize('links', links)
def test_copyright_information_visibility(links):
    browser.open(links)
    scroll_to(browser)
    is_copyright_info_visible(FOOTER)

