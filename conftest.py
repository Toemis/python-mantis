from fixture.application import Application
import pytest
import json
import os.path
import importlib


fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["web"]["baseUrl"])
    fixture.session.ensure_login(username=web_config["webadmin"]["username"], password=web_config["webadmin"]["password"])
    return fixture

# @pytest.fixture
# def check_ui(request):
#     return request.config.getoption("--check_ui")


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")  # true if exist


# def load_from_module(module):
#     return importlib.import_module("data.%s" % module).testdata


