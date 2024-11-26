import os
import allure
import pytest
from time import time
from faker import Faker
from playwright.sync_api import sync_playwright


# Configure the Allure report directory
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    cwd_report = os.path.join(os.path.dirname(os.path.abspath(__file__)), "allure-results")
    allure_dir = getattr(config.option, "allure_report_dir", None)
    if not allure_dir:
        setattr(config.option, "allure_report_dir", cwd_report)


# Fixture for managing Playwright browser instance
@pytest.fixture(autouse=True)
def browser_management(request):
    with sync_playwright() as p:
        # Configure the browser options
        browser = p.chromium.launch(
            headless=True if os.environ.get("CI_RUN") else False
        )  # Launch browser in headless mode if CI_RUN environment variable is set
        page = browser.new_page()

        # Attach some custom configuration to page or browser if needed
        page.set_default_timeout(25000)  # Set a default timeout for actions (e.g., waits)
        
        # Yielding browser and page for tests
        yield page

        # Capture screenshot if test fails
        if request.session.testsfailed > 0:
            screenshot = page.screenshot()
            allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)

        # Close browser after test
        browser.close()


# Fixtures for Faker data generation
@pytest.fixture
def first_name():
    return Faker().first_name()


@pytest.fixture
def last_name():
    return Faker().last_name()


@pytest.fixture
def user_email():
    lst = Faker().email().split("@")
    return "".join([lst[0], str(int(time())), "@", lst[1]])


@pytest.fixture
def password():
    return Faker().password()


@pytest.fixture
def state():
    return Faker().state()


@pytest.fixture
def postcode():
    return Faker().postcode()


@pytest.fixture
def phone_number():
    return Faker().phone_number()


@pytest.fixture
def street_address():
    return Faker().street_address()


@pytest.fixture
def city():
    return Faker().city()


# Fixture to log in using predefined credentials
@pytest.fixture
def login():
    from pages import sign_in
    sign_in.visit()
    sign_in.login("pamela341714226113@example.com", "@8j%Yltt(E)")


# Fixture to visit any page using Playwright's open method
@pytest.fixture
def visit_page():
    def visit(url, page):
        page.goto(url)

    return visit


# Optional custom page fixture for direct Playwright manipulation
@pytest.fixture(scope="function")
def page_fixture():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()
