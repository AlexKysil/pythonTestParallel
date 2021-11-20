import time

import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(scope='module')
def open_google(driver_session):
    driver_session.get("https://www.google.com/")
    return driver_session


def test_google_search_field(open_google):
    searchField = open_google.find_element(By.XPATH, "//input[@name='q']")
    searchField.click()
    searchField.send_keys("duck duck go" + "\n")
    time.sleep(3)
    assert (open_google.find_element(
        By.XPATH, "//h3[text()='DuckDuckGo — Privacy, simplified.']").text == "DuckDuckGo — Privacy, simplified."
            )

def test_opend_from_search(open_google):
    open_google.find_element(
        By.XPATH, "//h3[text()='DuckDuckGo — Privacy, simplified.']").click()
    time.sleep(3)
    assert open_google.find_element(By.XPATH, "//a[@id='logo_homepage_link']").is_displayed()
