from playwright.sync_api import Page, expect
import time
class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def clickbtn(self, locator: str):
        elem = self.fluent_wait(locator, 10, 0.5)
        elem.click()

    def type(self, locator: str, text: str):
        field = self.fluent_wait(locator,10,0.5)
        field.fill("")  # clear before typing
        field.type(text)

    def get_text(self, locator: str) -> str:
        elem = self.fluent_wait(locator, 10, 0.5)
        return elem.text_content()

    def is_visible(self, locator: str) -> bool:
        elem = self.fluent_wait(locator, 10, 0.5)
        return elem.is_visible()

    def double_click_element(self, locator: str):
        elem = self.fluent_wait(locator, 10, 0.5)
        elem.dblclick()

    def select_all_text(self, locator: str):
        elem=self.fluent_wait(locator,10,0.5)
        elem.click()
        elem.press("Control+A")


    def get_attribute(self, locator):
        elem = self.page.locator(locator)
        elem.wait_for(state="attached")
        handle = elem.element_handle()  # get actual DOM node handle
        if not handle:
            raise Exception(f"Element not found for locator: {locator}")
        return self.page.evaluate("(el) => el.validationMessage", handle)

    def scroll_to_bottom(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_element(self, locator: str):
        elem=self.fluent_wait(locator,10,0.5)
        elem.scroll_into_view_if_needed()
        return elem

    def fluent_wait(self, locator: str, timeout, poll_frequency):
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                el = self.page.locator(locator)
                if el.is_visible():
                    return el
            except TimeoutError:
                pass
            time.sleep(poll_frequency)
        raise TimeoutError(f"Element {locator} not visible after {timeout} seconds")
