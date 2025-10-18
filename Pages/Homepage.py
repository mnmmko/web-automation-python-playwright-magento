import time

from Pages.BasePage import BasePage


class Homepage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    title = "h2"
    subcribe = "//button[@title='Subscribe']"
    email = "//input[@type='email']"
    account = "//a//span[text()='Account']"
    login = "//a[@title='Log In']"
    logout = "//a[text()='Log Out']"
    register = "//a[text()='Register']"
    sendaway = "//button[text()='Send anyway']"
    msg_success = "//li[@class='success-msg']//ul//li//span"

    def get_name_of_title(self):
        return self.get_text(self.title)

    def add_email(self,emails):
        self.type(self.email,emails)

    def subcribe_click(self):
        self.clickbtn(self.subcribe)

    def get_success_sub(self):
        return self.get_text(self.msg_success)


    def clickaccount(self):
            self.clickbtn(self.account)


    def clicklogin(self):
            self.clickbtn(self.login)

    def clicklogout(self):
            self.clickbtn(self.logout)

    def clickregister(self):
            self.clickbtn(self.register)

    def clicksendaway(self):
        time.sleep(5)
        self.double_click_element(self.sendaway)
