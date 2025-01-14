from colorama import init, Fore
import re
import csv
from datetime import datetime
from playwright.sync_api import Page, TimeoutError

# Initialize colorama for colored terminal output
init(autoreset=True)

ERROR_REGEX = r"Не удалось|Ошибка"
ERROR_REPORT = []


ERROR_TOAST = "toast"
ERROR_TIMEOUT = "timeout"
ERROR_EXCEPTION = "except"


class ErrorHandler:
    def __init__(self):
        self.error_list = []
        self.error_report = ERROR_REPORT

    def handle_error_toasts(self, page: Page):
        """Checks for error toasts and logs them."""
        toasts = page.locator("div.big3-toast__title")
        count = toasts.count()

        for i in range(count):
            toast = toasts.nth(i)
            toast_text = toast.text_content()

            if toast_text not in self.error_list:
                if re.search(ERROR_REGEX, toast_text, re.IGNORECASE):
                    self.error_list.append(toast_text)
                    self.add_error_to_report(page.url, toast_text, ERROR_TOAST)

    def add_error_to_report(self, url: str, msg: str, type: str):
        """Logs error and prints it to the terminal."""

        # Clean up the message by removing extra whitespace
        msg = re.sub(r"\s+", " ", msg)

        # Append the error to the list
        self.error_report.append([url, type, msg])

        # Get the index of the appended element
        index = len(self.error_report) - 1

        # Print the error with its index
        print(Fore.RED + f"* ERROR {index}: {url}\t{type}\t'{msg}'")

    def handle_page_load_error(self, page: Page, timeout: int = 5):
        """Handles page load timeouts."""
        try:
            page.wait_for_load_state("networkidle", timeout=timeout * 1000)
        except TimeoutError:
            self.add_error_to_report(
                page.url, f"Page did not load within {timeout} seconds.", ERROR_TIMEOUT
            )
        page.wait_for_timeout(1000)

    def save_report_to_csv(self, url: str, test: str):
        """Saves the error report to a CSV file."""
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        count = len(self.error_report)
        domain = url.split("//")[1].split("/")[0]
        filename = f"errors_{count}_{domain}_{test}_{now}.csv"

        if count:
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["url", "type", "error"])
                writer.writerows(self.error_report)
            print(Fore.RED + f"\nError report saved: {filename}\n")
        else:
            print(Fore.GREEN + f"\nNo errors detected\n")


class UIInteractions:

    def zoom_out(self, page: Page, target_zoom: float = 0.25):
        """Zoom out the page to the specified zoom level."""
        current_zoom = 1.0  # Default zoom level (100%)

        # Calculate the number of times to zoom out by 10%
        while current_zoom > target_zoom:
            current_zoom -= 0.1  # Decrease zoom by 10%
            page.evaluate(f'document.body.style.zoom = "{current_zoom * 100}%"')  # Set new zoom level
            

        print(f"Zoomed out to {current_zoom * 100}%")
        page.wait_for_timeout(500)  # Wait for 2 seconds to observe the change

    def move_mouse_to_element(self, page: Page, element):
        """Moves the mouse to the center of the element."""
        box = element.bounding_box()
        if box:
            page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
            page.wait_for_timeout(500)  # Short wait for smooth transitions

    def make_button_visible(self, button):
        """Scrolls a button into view."""
        button.evaluate(
            "element => element.scrollIntoView({block: 'center', inline: 'center'})"
        )

    def login(
        self, page: Page, username: str, password: str, error_handler: ErrorHandler
    ):
        """Handles the login process and checks for errors."""
        page.fill('input[formcontrolname="username"]', username)
        page.fill('input[formcontrolname="password"]', password)
        page.click('button[type="submit"]')

        # page.wait_for_timeout(2000)

        error_handler.handle_error_toasts(page)

        try:

            page.get_by_text("Уведомления", exact=True).wait_for(timeout=5000)
            return True
        except Exception as e:
            error_handler.add_error_to_report(page.url, str(e), ERROR_EXCEPTION)
            return False

    def handle_popups(self, page: Page):
        """Skips various popups on the page."""
        self._skip_popup_tz(page)
        self._skip_popup_fx_ext(page)

    def _skip_popup_tz(self, page: Page):
        """Skips the time zone confirmation popup."""
        if page.locator('h2:has-text("Проверка часового пояса")').is_visible(
            timeout=2000
        ):
            btn = page.locator('button:has-text("Да")')
            if btn.is_visible(timeout=2000):
                btn.click()
                print("Skipped time zone confirmation popup")
                page.wait_for_timeout(2000)

    def _skip_popup_fx_ext(self, page: Page):
        """Skips Firefox extension installation popup."""
        btn = page.locator("button#cadesplugin_close_install")
        if btn and btn.is_visible(timeout=2000):
            btn.click()
            print("Skipped Firefox extension installation popup")
            page.wait_for_timeout(2000)
