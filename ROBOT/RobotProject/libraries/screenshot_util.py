import datetime
import os

from libraries.logger import LogGen

logger = LogGen.loggern()

class ScreenshotUtil:

    @staticmethod
    def capture_screenshot(driver, screenshot_name = "screenshot"):
        screenshot_dir = "reports/screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        timestamp = datetime.now().strftime("%Y%n%d_%H%M%S")
        clean_name = screenshot_name.replace(" ", " ")
        screenshot_path = (
            f"{screenshot_dir}/"
            f"{clean_name}_{timestamp}.png"
        )

        driver.save_screenshot(screenshot_path)
        logger.info(f"Screenshot saved at: {screenshot_path}")

        return screenshot_path