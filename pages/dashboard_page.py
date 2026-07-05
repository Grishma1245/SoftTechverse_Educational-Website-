from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.config import BASE_URL


class DashboardPage(BasePage):
    URL = f"{BASE_URL}/dashboard"

    # Locators — confirmed from saved dashboard.html
    SIDEBAR        = (By.CSS_SELECTOR, "aside.sidebar-left")
    LOGOUT_LINK    = (By.XPATH, "//a[contains(@href,'logout') or contains(text(),'Logout') or contains(text(),'Sign Out')]")

    def is_dashboard_loaded(self):
        """Wait explicitly for the URL to contain 'dashboard'."""
        try:
            self.wait.until(EC.url_contains("dashboard"))
            return True
        except Exception:
            return False

    def get_page_title(self):
        return self.driver.title

    def is_sidebar_visible(self):
        return self.is_visible(self.SIDEBAR)

    def logout(self):
        self.click(self.LOGOUT_LINK)
