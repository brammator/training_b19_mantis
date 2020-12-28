# -*- coding: utf-8 -*-
from fixture.common import WebDriverHelper


class SessionHelper(WebDriverHelper):
    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        self.fill_field("username", username)
        self.fill_field("password", password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_css_selector("td.login-info-left span")

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("username")

    def ensure_logged(self, username=None, password=None):
        current_user = self.logged_username
        if username is None and current_user is not None:
            self.logout()
        elif username is not None and current_user is None:
            self.login(username, password)
        elif username is not None and username != current_user:
            self.logout()
            self.login(username, password)
        else:
            pass  # (user, current == None) || (user == current)

    @property
    def logged_username(self):
        wd = self.app.wd
        try:
            wd.implicitly_wait(1)
            username = wd.find_element_by_css_selector("td.login-info-left span").text
            wd.implicitly_wait(self.app.DEFAULT_WAIT_TIME)
            return username
        except:
            wd.implicitly_wait(self.app.DEFAULT_WAIT_TIME)
            return None
