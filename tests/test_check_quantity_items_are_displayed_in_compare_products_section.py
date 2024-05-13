from pages import compare_items_page
import allure


@allure.title("check value of selected items to compare products section")
def test_check_quantity_value_in_compare_product_section(browser_management):
    compare_items_page.compare_items_values()
