from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--select_browser", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def invoke_browser(request):
    select_browser = request.config.getoption("--select_browser")
    '''if select_browser == "chrome":
        driver = webdriver.Chrome()
    #elif select_browser == "firefox":
        print("Firefox invoked")
    else:
        print("Invalid Selection")'''
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()
