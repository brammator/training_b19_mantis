# -*- coding: utf-8 -*-
import importlib
import json
import os.path
import jsonpickle
import pytest

from fixture.application import Application
from fixture.orm import ORMFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file, "r", encoding="utf-8") as fp:
            target = json.load(fp)
    return target


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture
def app(request):
    global fixture

    browser = request.config.getoption("--browser")
    config = load_config(request.config.getoption("--target"))
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, config=config)
    # fixture.session.ensure_logged(username=config['webadmin']["username"], password=config['webadmin']["password"])
    return fixture


@pytest.fixture(scope="session")
def db(config):
    db_config = config["db"]
    dbfixture = ORMFixture(host=db_config["host"], database=db_config["database"], user=db_config["user"], password=db_config["password"])
    return dbfixture


@pytest.fixture
def logged(app, config):
    app.session.ensure_logged(config["webadmin"]["username"], config["webadmin"]["password"])
    yield logged


@pytest.fixture
def loggedout(app, config):
    app.session.ensure_logged(None)
    yield logged


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logged(None)
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_form_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_form_module(module):
    return importlib.import_module(f"data.{module}").testdata


def load_from_json(filename):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{filename}.json"), "r",
              encoding="utf-8") as fp:
        return jsonpickle.decode(fp.read())


@pytest.fixture
def x():
    """пустая фикстура, чтобы закомментированная параметризация не ломала ран"""
    return 0
