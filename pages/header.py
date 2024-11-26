import allure
from playwright.sync_api import sync_playwright

product_url = 'http://195.133.27.184'

def open_product_url():
    browser.open(product_url)


