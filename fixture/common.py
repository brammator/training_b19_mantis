# -*- coding: utf-8 -*-
import random
import string

from selenium.webdriver.support.select import Select


class Helper:
    def __init__(self, app):
        self.app = app
        self.cache = None


class WebDriverHelper(Helper):
    def fill_field(self, field, value, scope=None):
        if value is None:
            return
        if scope is None:
            scope = self.app.wd
        e = scope.find_element_by_name(field)
        if e.tag_name == "input" and e.get_attribute("type") in ("text", "password"):
            e.clear()
            e.send_keys(value)
        elif e.tag_name == "select":
            Select(e).select_by_visible_text(value)
        elif e.tag_name == "textarea":
            e.clear()
            e.send_keys(value)
        else:
            raise KeyError(f"Unsupported field: {e.tag_name} / {e.get_attribute('type')}")

    def select_first(self):
        self.select_nth(0)

    def select_nth(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_byid(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector(f"input[value='{id}']").click()


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])