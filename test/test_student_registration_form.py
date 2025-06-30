from selene import browser, have
from pathlib import Path

import test


def test_student_registration(configuration_browser):
    browser.open('/automation-practice-form')

    #WHEN
    browser.element('[id=firstName]').type(text='Marcus')
    browser.element('[id=lastName]').type(text='Findle')

    browser.element('[id=userEmail]').type(text='marcus@ya.ru')

    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()

    browser.element('[id=userNumber]').send_keys('8949898494')

    browser.element('[id=dateOfBirthInput]').click()

    browser.element('[class*=year-select] > option[value="1988"]').click()
    browser.element('[class*=month-select] > option[value="5"]').click()
    browser.element('[class*=day--023]').click()

    browser.element('[id=subjectsInput]').type('Computer Science').press_enter()

    browser.element('[id=hobbies-checkbox-3]').element('..').click()

    browser.element('[id=uploadPicture]').set_value(str(Path(test.__file__).parent.joinpath('resources/cbr600rr.jpeg')))

    browser.element('[id=currentAddress]').type('Auyor')

    browser.element('[id=state]').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Haryana')).click()
    browser.element('[id=city]').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Panipat')).click()

    browser.element('[id=submit]').click()



    #THEN
    browser.element('[id^=example-modal][id*=title]').should(have.text('submitting the form'))
    browser.element('.table').all('td').should(have.texts(
        'Student Name', 'Marcus Findle',
        'Student Email', 'marcus@ya.ru',
        'Gender', 'Male',
        'Mobile', '8949898494',
        'Date of Birth', '23 June,1988',
        'Subjects', 'Computer Science',
        'Hobbies', 'Music',
        'Picture', 'cbr600rr.jpeg',
        'Address', 'Auyor',
        'State and City', 'Haryana Panipat'
    ))
