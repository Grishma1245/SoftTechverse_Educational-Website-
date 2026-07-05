from behave import given, when, then
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import VALID_USER, INVALID_USER


@given('I am on the login page')
def step_open_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when('I enter valid credentials')
def step_enter_valid(context):
    context.login_page.login(VALID_USER["email"], VALID_USER["password"])

@when('I enter invalid credentials')
def step_enter_invalid(context):
    context.login_page.login(INVALID_USER["email"], INVALID_USER["password"])

@then('I should be redirected to the dashboard')
def step_on_dashboard(context):
    dashboard = DashboardPage(context.driver)
    assert dashboard.is_dashboard_loaded(), \
        f"Expected dashboard URL, got: {context.driver.current_url}"

@then('I should remain on the login page')
def step_stay_on_login(context):
    login = LoginPage(context.driver)
    assert login.is_on_login_page(), \
        f"Expected login page, got: {context.driver.current_url}"
