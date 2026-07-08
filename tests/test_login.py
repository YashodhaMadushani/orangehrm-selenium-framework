from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_valid_login():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    login = LoginPage(driver)

    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()

    assert "dashboard" in driver.current_url

    driver.quit()