from Pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    fname = "#firstname"
    mname = "#middlename"
    lname = "#lastname"
    email = "#email_address"
    password = "#password"
    confirmpassword = "#confirmation"
    check_is_registered = "#is_subscribed"
    register = "//button[@title='Register']"
    back = "//a[@class='back-link']"


    def addfname(self,firstname):
        self.type(self.fname, firstname)



    def addmiddlename(self,middlename):
        self.type(self.mname, middlename)



    def addlname(self,lastname):
        self.type(self.lname, lastname)


    def addemail(self,emails):
        self.type(self.email, emails)

    def addpassword(self,passwords):
        self.type(self.password, passwords)


    def addconfirmation(self, confirmation):
        self.type(self.confirmpassword, confirmation)


    def clickcheck_is_registered(self):
        self.clickbtn(self.check_is_registered)

    def clickregister(self):
        self.scroll_to_element(self.register)
        self.clickbtn(self.register)

    def clickback(self):
        self.scroll_to_element(self.back)
        self.clickbtn(self.back)
