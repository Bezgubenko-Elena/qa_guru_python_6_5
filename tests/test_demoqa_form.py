import os
from selene import browser
from selene import have


def test_success_registration(browser_open):
    # fill form
    browser.element('[id="firstName"]').type('Helen')
    browser.element('[id="lastName"]').type('Bezgubenko')
    browser.element('[id="userEmail"]').type('eb@e.ru')
    browser.all('#genterWrapper .custom-control').element_by(have.exact_text('Female')).click()
    browser.element('[id="userNumber"]').type('9011111111')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1993"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="10"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--001"]').click()
    browser.element('[id="subjectsInput"]').type('a')
    browser.element('[id="react-select-2-option-3"]').click()
    browser.all('#hobbiesWrapper .custom-control').element_by(have.exact_text('Music')).click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('resources\h.jpg'))
    browser.element('[id="currentAddress"]').type('NN')
    browser.element('[id="state"]').click()
    browser.element('[id="react-select-3-option-0"]').click()
    browser.element('[id="city"]').click()
    browser.element('[id="react-select-4-option-0"]').click()
    browser.element('[id="submit"]').click()

    # check form
    browser.element('[class="modal-title h4"]').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive .table thead tr th')[0].should(have.text('Label'))
    browser.all('.table-responsive .table thead tr th')[1].should(have.text('Values'))
    browser.all('.table-responsive .table tbody tr')[0].should(have.text('Helen Bezgubenko'))
    browser.all('.table-responsive .table tbody tr')[1].should(have.text('eb@e.ru'))
    browser.all('.table-responsive .table tbody tr')[2].should(have.text('Female'))
    browser.all('.table-responsive .table tbody tr')[3].should(have.text('9011111111'))
    browser.all('.table-responsive .table tbody tr')[4].should(have.text('01 November,1993'))
    browser.all('.table-responsive .table tbody tr')[5].should(have.text('Social Studies'))
    browser.all('.table-responsive .table tbody tr')[6].should(have.text('Music'))
    browser.all('.table-responsive .table tbody tr')[7].should(have.text('h.jpg'))
    browser.all('.table-responsive .table tbody tr')[8].should(have.text('NN'))
    browser.all('.table-responsive .table tbody tr')[9].should(have.text('NCR Delhi'))
