import selenium
import pytest
import time
from selenium import webdriver
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = None

# Include screenshot for failed TC's in the report
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path='C:\\Users\\153841\\appdata\\local\\programs\\python\\python38\\lib\\site-packages\\chromedriver\\'
                            'chromedriver.exe', options=chrome_options)
    driver.get_screenshot_as_file(name)


# Add a hook for command prompt to ask at run time for browser inputs
def pytest_addoption(parser):
    parser.addoption("--browserName", action="store", default="chrome")


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    global driver
    browser_name = request.config.getoption("--browserName")  # give input for browser as py.test --browserName firefox
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(
            executable_path='C:\\Users\\153841\\appdata\\local\\programs\\python\\python38\\lib\\site-packages\\chromedriver\\'
                            'chromedriver.exe', options=chrome_options)
        driver.implicitly_wait(10)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            executable_path='C:\\Users\\153841\\appdata\\local\\programs\\python\\python38\\lib\\site-packages\\geckodriver\\geckodriver.exe')
        driver.implicitly_wait(10)
    
    elif browser_name == "None":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(
            executable_path='C:\\Users\\153841\\appdata\\local\\programs\\python\\python38\\lib\\site-packages\\chromedriver\\'
                            'chromedriver.exe', options=chrome_options)
        driver.implicitly_wait(10)

    elif browser_name == "None":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(
            executable_path='C:\\Users\\153841\\appdata\\local\\programs\\python\\python38\\lib\\site-packages\\geckodriver\\geckodriver.exe')
        driver.implicitly_wait(10)

    # Invoke the browser and maximize
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()
    request.cls.driver = driver
    return driver
    
    yield
    driver.close()




