# -*- coding: utf-8 -*-


def test_login(app, loggedout):
    app.session.login("administrator", "root")
    assert app.session.logged_username == "administrator"
