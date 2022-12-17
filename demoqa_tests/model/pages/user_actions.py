from demoqa_tests.model.pages.registration_form import RegistrationForm
from tests.test_data.users import user


class UserActions:

    def __init__(self):
        self.registration_form = RegistrationForm()

    def registration(self):
        (
            self.registration_form.given_opened()
            .set_full_name(user.name, user.last_name)
            .set_email(user.email)
            .set_gender(user.gender)
            .set_phone_number(user.mobile)
            .set_birth_date(user.birth_year, user.birth_month, user.birth_day)
            .add_subjects(user.subjects)
            .add_hobbies(user.hobbies)
            .upload_picture(user.picture_file)
            .set_current_address(user.current_address)
            .scroll_to_bottom()
            .set_state(user.state)
            .set_city(user.city)
            .submit_form()
            .should_have_submitted(
                [
                    ('Student Name', f'{user.name} {user.last_name}'),
                    ('Student Email', user.email),
                    ('Gender', user.gender.value),
                    ('Mobile', user.mobile),
                    ('Date of Birth', f'{user.birth_day} {user.birth_month},{user.birth_year}'),
                    ('Subjects', self.registration_form.get_subject_list(user.subjects)),
                    ('Hobbies', self.registration_form.get_hobby_list(user.hobbies)),
                    ('Picture', user.picture_file),
                    ('Address', user.current_address),
                    ('State and City', f'{user.state} {user.city}')
                ],
            )
        )
