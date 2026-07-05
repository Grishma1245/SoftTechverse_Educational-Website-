import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utils.config import BROWSER


def _resolve_chromedriver_path():
    """
    webdriver_manager sometimes returns a non-executable file (e.g.
    THIRD_PARTY_NOTICES.chromedriver). This helper finds the actual
    chromedriver.exe in the same directory.
    """
    raw_path = ChromeDriverManager().install()
    driver_dir = Path(raw_path).parent

    # Walk the directory to find chromedriver.exe
    for candidate in driver_dir.rglob("chromedriver.exe"):
        return str(candidate)

    # Fallback: return whatever WDM gave us
    return raw_path


def get_driver():
    if BROWSER == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver_path = _resolve_chromedriver_path()
        print(f"[INFO] Using chromedriver: {driver_path}")
        service = ChromeService(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=options)

    elif BROWSER == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
        driver.maximize_window()

    elif BROWSER == "edge":
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install())
        )
        driver.maximize_window()
    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")

    driver.implicitly_wait(10)
    return driver
