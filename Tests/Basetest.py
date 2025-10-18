import pytest

import random
import string

from common.DriveManeger import DriverManager


@pytest.mark.usefixtures("browser")
class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.page = DriverManager.get_page()

    @staticmethod
    def generate_random_email():
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        domain = random.choice(["gmail.com", "yahoo.com", "outlook.com"])
        return f"{username}@{domain}"