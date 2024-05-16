from pages import tees_page


def test_four_tees_discount_for_similar_tees(browser_management):
    tees_page.check_four_similar_tees_discount_is_applies()
