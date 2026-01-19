from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import BASE_URL, USERNAME, PASSWORD
import time

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.maximize_window()

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    time.sleep(2)
    assert "You logged into a secure area!" in login.get_message()

    driver.quit()


def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login("wronguser", "wrongpass")

    time.sleep(2)
    assert "Your username is invalid!" in login.get_message()

    driver.quit()
