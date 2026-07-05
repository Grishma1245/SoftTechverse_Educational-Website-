from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class StudentPage(BasePage):

    # Locators
    STUDENT_DETAILS_MENU = (By.XPATH, "//span[text()='Student Details']/parent::a")
    STUDENT_LIST_LINK    = (By.XPATH, "//a[@href='https://education.softtechverse.com/student/view']")

    def expand_student_details_menu(self):
        """Click the Student Details menu to expand it."""
        self.click(self.STUDENT_DETAILS_MENU)

    def is_student_list_link_visible(self):
        """Verify the Student List sub-link is visible."""
        return self.is_visible(self.STUDENT_LIST_LINK)

