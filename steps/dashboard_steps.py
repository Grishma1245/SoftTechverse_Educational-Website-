from behave import given, then
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import VALID_USER


@given('I am logged in as a valid user')
def step_logged_in(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    context.login_page.login(VALID_USER["email"], VALID_USER["password"])
    context.dashboard_page = DashboardPage(context.driver)
    assert context.dashboard_page.is_dashboard_loaded(), \
        f"Login failed — current URL: {context.driver.current_url}"

@then('the dashboard page should be displayed')
def step_dashboard_displayed(context):
    assert context.dashboard_page.is_dashboard_loaded(), \
        f"Dashboard not loaded. URL: {context.driver.current_url}"

@then('the sidebar should be visible')
def step_sidebar_visible(context):
    assert context.dashboard_page.is_sidebar_visible(), \
        "Sidebar not visible on dashboard"
