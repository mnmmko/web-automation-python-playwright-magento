from playwright.sync_api import sync_playwright

class DriverManager:
    _playwright = None
    _browser = None
    _context = None
    _page = None

    @classmethod
    def start_browser(cls, headless=False):
        if cls._browser is None:
            cls._playwright = sync_playwright().start()
            cls._browser = cls._playwright.chromium.launch(headless=True)
            cls._context = cls._browser.new_context(
                ignore_https_errors=True,
                viewport={"width": 1920, "height": 1080}  # maximize
            )
            cls._page = cls._context.new_page()
            cls._page.set_default_timeout(10000)
        return cls._page

    @classmethod
    def get_page(cls):
        if cls._page is None:
            return cls.start_browser()
        return cls._page

    @classmethod
    def close_browser(cls):
        if cls._browser:
            cls._context.close()
            cls._browser.close()
            cls._playwright.stop()
            cls._browser = None
            cls._context = None
            cls._page = None
