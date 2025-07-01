from selene import browser, have
from pathlib import Path

import test
from demoga_test.data.users import User
from demoga_test.enum.enum import Gender, Hobbies, State
from demoga_test.page.registaration_page import RegistrationPage


def test_student_registration_form(configuration_browser):
    registration_page = RegistrationPage()

    student = User(
        first_name='Alex',
        last_name='Potapov',
        email='potap@ya.ru',
        gender=Gender.MALE.value,
        mobile='0123456789',
        year='1986',
        month='August',
        day='12',
        subject='Computer Science',
        hobbies=Hobbies.MUSIC.value,
        picture_name='cbr600rr.jpeg',
        address='Saint-Petersburg Nevskiy street',
        state=State.NCR.value,
        city='Noida'
    )


    registration_page.full_fill_registration_form(student)

    registration_page.should_registration_fill_form(student)

# def test_student_registration(configuration_browser):
#     browser.open('/automation-practice-form')
#
#     #WHEN
#     browser.element('[id=firstName]').type(text='Marcus')
#     browser.element('[id=lastName]').type(text='Findle')
#
#     browser.element('[id=userEmail]').type(text='marcus@ya.ru')
#
#     browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
#
#     browser.element('[id=userNumber]').send_keys('8949898494')
#
#     browser.element('[id=dateOfBirthInput]').click()
#
#     browser.element('.react-datepicker__year-select').type('1986').click()
#     browser.element('.react-datepicker__month-select').type('August').click()
#     browser.element(f'.react-datepicker__day--0{21}').click()
#
#     browser.element('#subjectsInput').type('Computer Science').press_enter()
#
#     browser.element('[id=hobbies-checkbox-3]').element('..').click()
#
#     browser.element('[id=uploadPicture]').set_value(str(Path(test.__file__).parent.joinpath('resources/cbr600rr.jpeg')))
#
#     browser.element('[id=currentAddress]').type('Auyor')
#
#     browser.element('[id=state]').click()
#     browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Haryana')).click()
#     browser.element('[id=city]').click()
#     browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Panipat')).click()
#
#     browser.element('[id=submit]').click()
#
#
#
#     #THEN
#     browser.element('[id^=example-modal][id*=title]').should(have.text('Thanks for submitting the form'))
#     browser.element('.table').all('td').should(have.texts(
#         'Student Name', 'Marcus Findle',
#         'Student Email', 'marcus@ya.ru',
#         'Gender', 'Male',
#         'Mobile', '8949898494',
#         'Date of Birth', '23 June,1988',
#         'Subjects', 'Computer Science',
#         'Hobbies', 'Music',
#         'Picture', 'cbr600rr.jpeg',
#         'Address', 'Auyor',
#         'State and City', 'Haryana Panipat'
#     ))
