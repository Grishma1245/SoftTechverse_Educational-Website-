from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import BASE_URL


class NavigationPage(BasePage):

    # Sidebar nav link locators
    DASHBOARD_LINK = (By.XPATH, "//a[contains(@href,'dashboard')]")
    STUDENT_LINK   = (By.XPATH, "//a[contains(@href,'student/view')]")

    def click_dashboard(self):
        self.click(self.DASHBOARD_LINK)

    def click_student_menu(self):
        self.click(self.STUDENT_LINK)

    def is_on_page(self, keyword):
        return keyword in self.current_url()
