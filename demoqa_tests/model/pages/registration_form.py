from typing import Tuple
from selene import have, command, by
from selene.support.shared import browser
from demoqa_tests.model.controls import modal
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.controls.dropdown import DropDown
from demoqa_tests.model.apps import google
from tests.test_data.users import Subject, Hobby
from demoqa_tests.utils import path

state = browser.element('#state')


class RegistrationForm:
    def __init__(self):
        self.birthday = DatePicker(browser.element('#dateOfBirthInput'))

    def given_opened(self):
        browser.open('/automation-practice-form')
        google.remove_ads(amount=3, timeout=3)
        google.remove_ads(amount=1, timeout=3)

        return self

    def set_full_name(self, first_name: str, last_name: str):
        browser.element('#firstName').type(first_name)
        browser.element('#lastName').type(last_name)
        return self

    def set_email(self, email: str):
        browser.element('#userEmail').type(email)
        return self

    def set_gender(self, gender):
        browser.all('[for^=gender-radio]').by(
            have.exact_text(gender.value)
        ).first.click()
        return self

    def set_phone_number(self, mobile: str):
        browser.element('#userNumber').type(mobile)
        return self

    def set_birth_date(self, birth_year, birth_month, birth_day):
        self.birthday.select_date(birth_year, birth_month, birth_day)
        return self

    def add_subjects(self, values: Tuple[Subject]):
        for subject in values:
            browser.element('#subjectsInput').type(subject.value).press_enter()
        return self

    @staticmethod
    def get_subject_list(values: Tuple[Subject]):
        subjects = ''

        for subject in values:
            subjects = subjects + str(subject.value) + ', '

        subjects = subjects.rstrip(', ')

        return subjects

    def add_hobbies(self, values: Tuple[Hobby]):
        for hobby in values:
            hobby_xpath = "//label[contains(.,'" + str(hobby.value) + "')]"
            browser.element(by.xpath(hobby_xpath)).click()
        return self

    @staticmethod
    def get_hobby_list(values: Tuple[Subject]):
        hobbies = ''

        for hobby in values:
            hobbies = hobbies + str(hobby.value) + ', '

        hobbies = hobbies.rstrip(', ')

        return hobbies

    def upload_picture(self, picture_file: str):
        browser.element('[id="uploadPicture"]').send_keys(
            path.to_resource(picture_file)
        )
        return self

    def set_current_address(self, current_address: str):
        browser.element('#currentAddress').type(current_address)
        return self

    def set_state(self, value: str):
        DropDown.select(self, state, value)
        return self

    def set_city(self, value: str):
        DropDown.select(self, browser.element('#city'), value)
        return self

    def scroll_to_bottom(self):
        state.perform(command.js.scroll_into_view)
        return self

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)
        return self

    def should_have_submitted(self, data):
        rows = modal.dialog.all('tbody tr')
        for row, value in data:
            rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
        return self
