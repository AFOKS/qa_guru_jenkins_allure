import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    URL = "https://demoqa.com/automation-practice-form"

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")

    GENDER_MALE = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_FEMALE = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    GENDER_OTHER = (By.CSS_SELECTOR, "label[for='gender-radio-3']")

    MOBILE = (By.ID, "userNumber")
    DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
    SUBJECTS = (By.ID, "subjectsInput")

    HOBBIES_SPORTS = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    HOBBIES_READING = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    HOBBIES_MUSIC = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")

    CURRENT_ADDRESS = (By.ID, "currentAddress")

    STATE = (By.ID, "state")
    CITY = (By.ID, "city")

    SUBMIT_BUTTON = (By.ID, "submit")

    SUCCESS_TITLE = (By.ID, "example-modal-sizes-title-lg")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Open url /automation-practice-form")
    def open(self):
        self.driver.get(self.URL)

        wrapper = self.driver.find_element(
            By.CSS_SELECTOR,
            ".practice-form-wrapper"
        )

        assert "Student Registration Form" in wrapper.text

        self.driver.execute_script("""
            document.querySelector('footer')?.remove();
            document.querySelector('#fixedban')?.remove();
        """)

    @allure.step("Fill first name field with {first_name}")
    def fill_first_name(self, first_name):
        element = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )
        element.clear()
        element.send_keys(first_name)

    @allure.step("Fill last name field with {last_name}")
    def fill_last_name(self, last_name):
        element = self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        )
        element.clear()
        element.send_keys(last_name)

    @allure.step("Fill email field with {email}")
    def fill_email(self, email):
        element = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        )
        element.clear()
        element.send_keys(email)

    @allure.step("Select gender: {gender}")
    def select_gender(self, gender):
        gender_locators = {
            "Male": self.GENDER_MALE,
            "Female": self.GENDER_FEMALE,
            "Other": self.GENDER_OTHER,
        }

        locator = gender_locators[gender]

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    @allure.step("Fill mobile number with {mobile}")
    def fill_mobile_number(self, mobile):
        element = self.wait.until(
            EC.visibility_of_element_located(self.MOBILE)
        )
        element.clear()
        element.send_keys(mobile)

    @allure.step("Add subject: {subject}")
    def add_subject(self, subject):
        element = self.wait.until(
            EC.visibility_of_element_located(self.SUBJECTS)
        )
        element.send_keys(subject)
        element.send_keys("\ue007")  # ENTER

    @allure.step("Select hobby: {hobby}")
    def select_hobby(self, hobby):
        hobby_locators = {
            "Sports": self.HOBBIES_SPORTS,
            "Reading": self.HOBBIES_READING,
            "Music": self.HOBBIES_MUSIC,
        }

        locator = hobby_locators[hobby]

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    @allure.step("Fill current address with {address}")
    def fill_current_address(self, address):
        element = self.wait.until(
            EC.visibility_of_element_located(self.CURRENT_ADDRESS)
        )
        element.clear()
        element.send_keys(address)

    @allure.step("Select state: {state}")
    def select_state(self, state):
        self.wait.until(
            EC.element_to_be_clickable(self.STATE)
        ).click()

        state_locator = (
            By.XPATH,
            f"//*[@id='stateCity-wrapper']//*[text()='{state}']"
        )

        element = self.wait.until(
            EC.element_to_be_clickable(state_locator)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    @allure.step("Select city: {city}")
    def select_city(self, city):
        self.wait.until(
            EC.element_to_be_clickable(self.CITY)
        ).click()

        city_locator = (
            By.XPATH,
            f"//*[@id='stateCity-wrapper']//*[text()='{city}']"
        )

        element = self.wait.until(
            EC.element_to_be_clickable(city_locator)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    @allure.step("Submit registration form")
    def submit(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    @allure.step("Check successful submission")
    def check_success_message(self):
        title = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_TITLE)
        )

        assert "Thanks for submitting the form" in title.text