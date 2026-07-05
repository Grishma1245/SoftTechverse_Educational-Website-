from behave import when, then
from pages.student_page import StudentPage


@when('I click the Student Details menu')
def step_click_student_menu(context):
    context.student_page = StudentPage(context.driver)
    context.student_page.expand_student_details_menu()


@then('the Student List option should be visible')
def step_student_list_link_visible(context):
    assert context.student_page.is_student_list_link_visible(), \
        "Student List sub-menu link is not visible after expanding Student Details"

