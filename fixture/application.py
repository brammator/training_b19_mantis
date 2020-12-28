# -*- coding: utf-8 -*-
from selenium import webdriver

from fixture.project import ProjectHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self, browser, config):
        self.DEFAULT_WAIT_TIME = 5
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        self.config = config
        self.base_url = config['web']['base_url']
        self.wd.implicitly_wait(self.DEFAULT_WAIT_TIME)
        self.session = SessionHelper(app=self)
        self.project = ProjectHelper(app=self)

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/mantisbt-1.2.20/my_view_page.php") and
                len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.get(self.base_url)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


