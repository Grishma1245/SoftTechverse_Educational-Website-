from behave import given, when, then
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import BASE_URL


@given('I am not logged in')
def step_not_logged_in(context):
    # Clear cookies to ensure logged-out state
    context.driver.delete_all_cookies()

@when('I try to access the dashboard directly')
def step_access_dashboard_direct(context):
    context.driver.get(f"{BASE_URL}/dashboard")

@then('I should be redirected to the login page')
def step_redirected_to_login(context):
    login = LoginPage(context.driver)
    assert login.is_on_login_page(), \
        f"Expected login page after redirect, got: {context.driver.current_url}"
