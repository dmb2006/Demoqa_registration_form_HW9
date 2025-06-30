from selene import browser, have, command

from demoga_test import resource

class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def type_first_name(self, value):
        browser.element('[id=firstName]').type(value)

    def type_last_name(self, value):
        browser.element('[id=lastName]').type(value)

    def type_email_adress(self, value):
        browser.element('[id=userEmail]').type(value)

    def gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def number(self, value):
        browser.element('[id=userNumber]').send_keys(value)

    def date_of_birth(self, year, month, day):
        browser.element('[id=dateOfBirthInput]').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def type_subjects(self, value):
        browser.element('[id=subjectsInput]').type(value).press_enter()

    def hobbies(self):
        browser.all('.custom-checkbox').element_by(have.exact_text('Music')).click()

    def upload_picture(self):
        browser.element('[id=uploadPicture]').set_value(resource.path('cbr600rr.jpeg'))

    def type_current_address(self, value):
        browser.element('[id=currentAddress]').type(value)

    def state_and_city(self, state, city):
        browser.element('[id=state]').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()
        browser.element('[id=city]').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).click()

    def submit(self):
        browser.element('[id=submit]').perform(command.js.scroll_into_view).click()

    def should_greeting_registration_form(self, value):
        browser.element('[id^=example-modal][id*=title]').should(have.text(value))

    def should_registration_info(self, first_name, last_name, email, gender, mobile, date_of_birth, subject, hobbies,
                                 picture, address, state, city):
        browser.element('.table-responsive').all('td').even.should(
            have.exact_texts(
                f'{first_name} {last_name}', email, gender,
                mobile, date_of_birth, subject, hobbies, picture,
                address, f'{state} {city}'

            ))


    # def should_registration_user_with(self, student_name, student_email, gender, mobile, date_of_birth, subjects,
    #                                   hobbies,
    #                                   picture, address, state_and_city):
    #     browser.element('.table').all('td').should(have.exact_texts(
    #         student_name, student_email, gender, mobile,
    #         date_of_birth, subjects,
    #         hobbies, picture, address, state_and_city
    # def should_registration_info(self, Student_Name, param1, param2, param3, param4, param5, param6, param7, param8, param9,
    #                              param10, param11, param12, param13, param14, param15, param16, param17, param18,
    #                              param19):
    #     browser.element('.table').all('td').should(
    #         have.texts(
    #             f'{Student_Name}', 'Marcus Findle',
    #             'Student Email', 'marcus@ya.ru',
    #             'Gender', 'Male',
    #             'Mobile', '4565464646',
    #             'Date of Birth', '26 August,1986',
    #             'Subjects', 'Computer Science',
    #             'Hobbies', 'Music',
    #             'Picture', 'cbr600rr.jpeg',
    #             'Address', 'Ayuor',
    #             'State and City', 'Haryana Panipat'
    #         ))