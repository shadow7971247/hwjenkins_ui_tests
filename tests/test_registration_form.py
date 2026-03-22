import allure
from pages.registration_page import RegistrationPage
from models.user import User


@allure.title("Successful fill form")
def test_successful(fill_registration_form):
    driver = fill_registration_form

    user = User(
        first_name="Jane",
        last_name="Doe",
        email="JaneD@example.com",
        gender="Other",
        mobile="1231231230",
        subjects=["Physics"],
        hobbies=["Sports"],
        address="Ulitsa Pushkina 1",
        state="NCR",
        city="Delhi"
    )

    page = RegistrationPage(driver)

    (page
     .open()
     .fill(user)
     .submit()
     .should_have_success_modal())