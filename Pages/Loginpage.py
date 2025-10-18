from Pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    login_title = "h1"
    emails = "#email"
    password = "#pass"
    login = "//button[@title='Login']"


    def get_login_title(self):
        return self.get_text(self.login_title)

    def enter_email(self,email):
        self.type(self.emails, email)



    def enter_password(self,passwords):
        self.type(self.password,passwords)



    def click_login(self):
        self.clickbtn(self.login)

    def get_email_validtied(self):
        return self.get_attribute(self.emails)




