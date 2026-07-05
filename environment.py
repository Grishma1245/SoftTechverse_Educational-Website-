import os
from utils.driver_factory import get_driver


def before_scenario(context, scenario):
    """Launch a fresh browser before each scenario."""
    context.driver = get_driver()


def after_scenario(context, scenario):
    """Take screenshot on failure, then close browser."""
    driver = getattr(context, 'driver', None)
    if driver is None:
        return
    if scenario.status == "failed":
        try:
            os.makedirs("reports/screenshots", exist_ok=True)
            safe_name = scenario.name.replace(" ", "_").replace("/", "-")
            path = f"reports/screenshots/FAIL_{safe_name}.png"
            driver.save_screenshot(path)
            print(f"\n[SCREENSHOT] Saved: {path}")
        except Exception:
            pass  # Browser may already be closed
    try:
        driver.quit()
    except Exception:
        pass  # Ignore if session already invalid
