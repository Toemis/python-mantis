from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper


class Application:
    def __init__(self, browser, config):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser: %s" % browser)
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.project = ProjectHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)
        self.base_url = config['web']['baseUrl']
        self.config = config

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
    #
    # def return_home_page(self):
    #     wd = self.wd
    #     if not self.is_home_page():
    #         wd.find_element_by_link_text("home page").click()

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url + "my_view_page.php")

    def destroy(self):
        self.wd.quit()

    # def is_home_page(self):
    #     wd = self.wd
    #     return wd.current_url.endswith("/addressbook/") or wd.current_url.endswith("/addressbook/index.php")
