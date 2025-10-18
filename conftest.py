import pytest
from common.DriveManeger import DriverManager


@pytest.fixture(scope="session", autouse=True)
def browser():
    page = DriverManager.start_browser()
    url = "http://live.techpanda.org/index.php/"
    page.goto(url)
    yield page
    DriverManager.close_browser()

@pytest.fixture
def page():
    return DriverManager.get_page()