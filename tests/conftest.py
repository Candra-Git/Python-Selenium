import pytest
from selenium import webdriver
driver = None
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#buat setting jalan di beda browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Edge"
    )


@pytest.fixture()
def setup(request):
        global driver
        browser_name=request.config.getoption("browser_name")
        if browser_name == "Edge":
                driver = webdriver.Edge()
        elif browser_name == "Chrome":
                driver = webdriver.Chrome()
        elif browser_name == "Firefox":
                driver = webdriver.Firefox()
        else:
                raise ValueError(f"Browser '{browser_name}' tidak didukung. Gunakan 'edge', 'chrome', atau 'firefox'.")

        driver.get("https://qaclickacademy.github.io/protocommerce/")
        request.cls.driver = driver
        driver.maximize_window()
        yield
        driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
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
        driver.get_screenshot_as_file(name)