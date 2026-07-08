from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.employee_page import EmployeePage



def test_add_employee():

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )

    driver.maximize_window()


    # Login

    login = LoginPage(driver)

    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()


    # Add employee

    employee = EmployeePage(driver)

    employee.click_pim()

    employee.click_add_employee()

    employee.enter_employee_details(
        "Yashodha",
        "M",
        "Madushani"
    )

    employee.save_employee()


    # Verification

    assert employee.verify_employee_added()


    driver.quit()