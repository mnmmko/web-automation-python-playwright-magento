import pytest
from Pages.Homepage import Homepage
from Tests.Basetest import BaseTest


class Test1(BaseTest):

    @pytest.mark.order(1)
    def test_veritfy_page_title(self):
        hp = Homepage(self.page)
        assert "This is demo site for" in hp.get_name_of_title()
        print(hp.get_name_of_title())

    @pytest.mark.order(2)
    def test_vertitfy_subcribe_email(self):
        hp = Homepage(self.page)
        hp.add_email(self.generate_random_email())
        hp.subcribe_click()
        print(hp.msg_success)
