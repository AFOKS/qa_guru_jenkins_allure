import allure

from pages.registration_page import RegistrationPage


@allure.title("Successful fill form")
def test_successful(setup_browser):
    registration_page = RegistrationPage(setup_browser)

    first_name = "Alex"
    last_name = "Egorov"

    with allure.step("Open registration form"):
        registration_page.open()

    with allure.step("Fill personal information"):
        registration_page.fill_first_name(first_name)
        registration_page.fill_last_name(last_name)
        registration_page.fill_email("alex@egorov.com")

    with allure.step("Select gender"):
        registration_page.select_gender("Other")

    with allure.step("Fill mobile number"):
        registration_page.fill_mobile_number("1231231230")

    with allure.step("Add subject"):
        registration_page.add_subject("Maths")

    with allure.step("Select hobby"):
        registration_page.select_hobby("Sports")

    with allure.step("Fill current address"):
        registration_page.fill_current_address("Some street 1")

    with allure.step("Select state"):
        registration_page.select_state("NCR")

    with allure.step("Select city"):
        registration_page.select_city("Delhi")

    with allure.step("Submit form"):
        registration_page.submit()

    with allure.step("Check form results"):
        registration_page.check_success_message()