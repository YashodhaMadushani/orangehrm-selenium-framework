from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)


    # Locators

    pim_menu = (By.XPATH, "//span[text()='PIM']")
    add_employee_button = (By.XPATH, "//a[text()='Add Employee']")

    first_name = (By.NAME, "firstName")
    middle_name = (By.NAME, "middleName")
    last_name = (By.NAME, "lastName")

    save_button = (
        By.XPATH,
        "//button[@type='submit']"
    )

    employee_name = (
        By.XPATH,
        "//h6[contains(normalize-space(),'Personal Details')]"
    )


    # Actions

    def click_pim(self):
        self.wait.until(
            EC.element_to_be_clickable(self.pim_menu)
        ).click()


    def click_add_employee(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.add_employee_button
            )
        ).click()


    def enter_employee_details(
            self,
            firstname,
            middlename,
            lastname):

        self.wait.until(
            EC.visibility_of_element_located(
                self.first_name
            )
        ).send_keys(firstname)


        self.driver.find_element(
            *self.middle_name
        ).send_keys(middlename)


        self.driver.find_element(
            *self.last_name
        ).send_keys(lastname)


    def save_employee(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.save_button
            )
        ).click()


    def verify_employee_added(self):

        self.wait.until(
            lambda driver: "viewPersonalDetails" in driver.current_url
        )
        return "viewPersonalDetails" in self.driver.current_url