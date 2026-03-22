from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from models.user import User


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> "RegistrationPage":
        self.driver.get("https://demoqa.com/automation-practice-form")
        wrapper = self.driver.find_element(By.CSS_SELECTOR, ".practice-form-wrapper")
        assert "Student Registration Form" in wrapper.text
        return self

    def fill(self, user: User) -> "RegistrationPage":
        self._fill_name(user.first_name, user.last_name)
        self._fill_email(user.email)
        self._select_gender(user.gender)
        self._fill_mobile(user.mobile)
        self._fill_subjects(user.subjects)
        self._select_hobbies(user.hobbies)
        self._fill_address(user.address)
        self._select_state(user.state)
        self._select_city(user.city)
        return self

    def submit(self) -> "RegistrationPage":
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        return self

    def should_have_success_modal(self) -> bool:
        title = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#example-modal-sizes-title-lg"))
        )
        assert "Thanks for submitting the form" in title.text
        return True

    def _fill_name(self, first: str, last: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "#firstName").send_keys(first)
        self.driver.find_element(By.CSS_SELECTOR, "#lastName").send_keys(last)

    def _fill_email(self, email: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys(email)

    def _select_gender(self, gender: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "#genterWrapper").find_element(
            By.XPATH, f".//*[text()='{gender}']"
        ).click()

    def _fill_mobile(self, mobile: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "#userNumber").send_keys(mobile)

    def _fill_subjects(self, subjects: list) -> None:
        subject_input = self.driver.find_element(By.CSS_SELECTOR, "#subjectsInput")
        for subject in subjects:
            subject_input.send_keys(subject)
            subject_input.send_keys(Keys.ENTER)

    def _select_hobbies(self, hobbies: list) -> None:
        wrapper = self.driver.find_element(By.CSS_SELECTOR, "#hobbiesWrapper")
        for hobby in hobbies:
            element = wrapper.find_element(By.XPATH, f".//*[text()='{hobby}']")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            clickable = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//*[@id='hobbiesWrapper']//*[text()='{hobby}']"))
            )
            self.driver.execute_script("arguments[0].click();", clickable)

    def _fill_address(self, address: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys(address)

    def _select_state(self, state: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "#state").click()
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//*[@id='stateCity-wrapper']//*[text()='{state}']"))
        )
        self.driver.execute_script("arguments[0].click();", element)

    def _select_city(self, city: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "#city").click()
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//*[@id='stateCity-wrapper']//*[text()='{city}']"))
        )
        self.driver.execute_script("arguments[0].click();", element)