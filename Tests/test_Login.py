import pytest

from Pages.Homepage import Homepage
from Pages.Loginpage import LoginPage
from Tests.Basetest import BaseTest
from utils.ReadExcel import ReadExcel


class TestLogin(BaseTest):

    @pytest.mark.order(3)
    def test_vertify_open_login_page(self):
        hp = Homepage(self.page)
        lp=LoginPage(self.page)
        hp.clickaccount()
        hp.clicklogin()
        assert "Login or Create an Account " in lp.get_login_title()
        print(lp.get_login_title())

    @staticmethod
    def login_data():
        return ReadExcel.read_sheet("login")

    @pytest.mark.order(4)
    @pytest.mark.parametrize("username,password", login_data())
    def test_vertify_login_page(self,username,password):
        hp = Homepage(self.page)
        lp=LoginPage(self.page)
        hp.clickaccount()
        hp.clicklogin()
        lp.enter_email(username)
        lp.enter_password(password)
        lp.click_login()
        hp.clickaccount()
        hp.clicklogout()

    @pytest.mark.order(5)
    def test_vertify_invalid_email(self):
        hp = Homepage(self.page)
        hp.clickaccount()
        hp.clicklogin()
        lp=LoginPage(self.page)
        lp.enter_email("invalid_email")
        lp.click_login()
        assert "Please include an '@' in the email address. 'invalid_email' is missing an '@'." in lp.get_email_validtied()
        print(lp.get_email_validtied())


