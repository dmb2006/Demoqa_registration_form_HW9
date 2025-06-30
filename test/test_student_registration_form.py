from selene import browser, have
from demoga_test import resource
from demoga_test.pages.registration_page import RegistrationPage


def test_student_registration(configuration_browser):
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.type_first_name('Marcus')
    registration_page.type_last_name('Findle')
    registration_page.type_email_adress('marcus@ya.ru')

    registration_page.gender('Male')
    registration_page.number('4565464646')

    registration_page.date_of_birth('1986', 'August', '26')

    registration_page.type_subjects('Computer Science')
    registration_page.hobbies()

    registration_page.upload_picture()

    registration_page.type_current_address('Ayuor')

    registration_page.state_and_city('Haryana', 'Panipat')

    registration_page.submit()

    # THEN
    registration_page.should_greeting_registration_form('submitting the form')
    registration_page.should_registration_info(
        'Marcus',
        'Findle',
        'marcus@ya.ru',
        'Male',
        '4565464646',
        '26 August,1986',
        'Computer Science',
        'Music',
        'cbr600rr.jpeg',
        'Ayuor',
        'Haryana',
        'Panipat'
    )


