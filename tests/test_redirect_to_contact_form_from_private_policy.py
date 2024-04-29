from selenium.webdriver.common.by import By
from datetime import datetime
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

base_url = "https://magento.softwaretestingboard.com/privacy-policy-cookie-restriction-mode"
contact_us_url = "https://magento.softwaretestingboard.com/contact/"


@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    chrome_options.add_argument("--window-size=1440,1080")
    yield browser
    attach = browser.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today}", attachment_type=allure.attachment_type.PNG)
    browser.quit()


@allure.title("Verify redirect from Privacy Policy to Contact Us link")
def test_redirect_to_contact_form_from_private_policy(browser):
    browser.get(base_url)
    browser.find_element(By.LINK_TEXT, "Questions for Luma?").click()
    browser.find_element(By.LINK_TEXT, "Contact Us").click()
    assert browser.current_url == contact_us_url
    page_under_construction = browser.find_element(By.CSS_SELECTOR, "span[class='base']").text
    assert page_under_construction == "Whoops, our bad...", "Yes contact form is ready"
