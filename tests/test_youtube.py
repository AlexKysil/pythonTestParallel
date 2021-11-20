import time

import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(scope='module')
def open_youtube(driver_session):
    driver_session.get("https://www.youtube.com/")
    return driver_session


def test_youtube_search_field(open_youtube):
    time.sleep(5)
    searchField = open_youtube.find_element(By.XPATH, "//input[@id='search']")
    searchField.click()
    searchField.send_keys("Котики" + "\n")
    cats = open_youtube.find_elements(By.XPATH, "//*[contains(text(), 'КОТЫ')]")
    assert len(cats) != 0

def test_youtube_home_btn(open_youtube):
    time.sleep(5)
    homeBtn = open_youtube.find_element(By.XPATH, "//a[@id='endpoint']//*[text()='Home'or text()='Главная']")
    homeBtn.click()
    assert homeBtn.is_displayed()