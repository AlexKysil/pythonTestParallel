import pytest
from selenium import webdriver

from chromedriver_py import binary_path as chrome_path


@pytest.fixture(scope='module')
def driver_session():
    """
    Init chromedriver session
    :return:
    """

    driver_session = webdriver.Chrome(executable_path=chrome_path)
    driver_session.implicitly_wait(5)

    yield driver_session

    driver_session.quit()


@pytest.fixture(scope='function')
def data_storage():
    """
    Hold data during test
    :return:
    """

    data_storage = {}
    yield data_storage
