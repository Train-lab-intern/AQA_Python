import pytest
import requests
import allure
import json


domain = 'https://test.app.it-roast.com'
register_user = '/api/v1/users/register'
complete_registration = '/api/v1/users/complete-registration'


def post_request_create_user(email, username, password):
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        "username": f"{username}",
        "email": f"{email}",
        "password": f"{password}"
    })
    request = requests.request('POST', domain + register_user, headers=headers,
                               data=data)
    return request


def get_request_confirm_registration(email):
    params = {
        'userEmail': f'{email}'
    }
    request = requests.request('GET', domain + complete_registration, params=params)
    return request


@allure.feature('Registration')
@allure.story('Send a request with a valid email')
@pytest.mark.parametrize('email', [
    'test.trainlab@gmail.com', 'TEST.TRAINLAB@GMAIL.COM', 'test.trainlab+1234567890@gmail.com',
    'test.trainlab@gmail1234567890.com', 'test-trainlab@gmail.com', 'test.trainlab@gmail-mail.com',
    'test.trainlab@gmail.com', 'test_trainlab@gmail.com', 'test.trainlab@gmail.com.com',
    'test$trainlab@gmail.com', 'test#trainlab@gmail.com', 'test%trainlab@gmail.com',
    'test&trainlab@gmail.com', 'test*trainlab@gmail.com',
    'test/trainlab@gmail.com', 'test=trainlab@gmail.com', 'test^trainlab@gmail.com',
    'test?trainlab@gmail.com', 'test`trainlab@gmail.com', 'test{trainlab}@gmail.com',
    'test|trainlab@gmail.com', 'test~trainlab@gmail.com', 'b@gmail.com', 'ab@gmail.com'
])
def test_check_valid_emails(connect_db, email, check_existence_and_delete_email):
    with allure.step('Send request to create user'):
        request = post_request_create_user(f'{email}', 'Vasia', '123456qW')
    with allure.step('Check status code'):
        assert request.status_code == 200


@allure.feature('Registration')
@allure.story('Send a request with an invalid email address')
@pytest.mark.parametrize('email', [
    'test.trainlabgmail.com', 'test.trainlab@gmailcom', 'тест.траинлаб@gmailcom', '', '     ',
    '.test.trainlab@gmail.com', 'test.trainlab@gmail.com.', 'test..trainlab@gmail.com',
    'test trainlab@gmail.com', 'test.trainlab@gm ail.com', '@gmailcom'
])
def test_check_invalid_emails(connect_db, email, check_existence_and_delete_email):
    with allure.step('Send request to create user'):
        request = post_request_create_user(f'{email}', 'Vasia', '123456qW')
    with allure.step('Check status code'):
        assert request.status_code == 400


@allure.feature('Registration')
@allure.story('Check username')
@pytest.mark.parametrize('username', ['VASIA', 'vasia', '1vasia', 'Vasia,./<>?:;|{}[]~`!@#$%^&*()_+=-',
                                      '', '   '])
@pytest.mark.parametrize('email', ['test.trainlab@gmail.com'])
def test_username(connect_db, username, check_existence_and_delete_email, email):
    with allure.step('Send request to create user'):
        request = post_request_create_user(f'{email}', f'{username}', '123456qW')
    with allure.step('Check status code'):
        assert request.status_code == 200


@allure.feature('Registration')
@allure.story('Send a request with an valid password')
@pytest.mark.parametrize('password', ['Qaz1234567890123456789012345678901234567890123456789xexexcefcrgv'
                                      'thc1234567890123556790qertyooasdfghkozxvbnmqeryoadfhjkzxcvbnmasdfgh'
                                      'kqetyuiizsdfghjjkjzxcderfvtgbyhnqazwsx1234567890qwertyuioasdgghjklz'
                                      'xcvbnmmececfvrvtgbhbybcedxwsxwdcefvrgtbrcexwxexrgvtvhbrcfe',
                                      'Qaz12345', '12345azQ', '123Q45we'])
@pytest.mark.parametrize('email', ['test.trainlab@gmail.com'])
def test_valid_password(connect_db, password, email, check_existence_and_delete_email):
    with allure.step('Send request to create user'):
        request = post_request_create_user(f'{email}', 'Vasia', f'{password}')
    with allure.step('Check status code'):
        assert request.status_code == 200


@allure.feature('Registration')
@allure.story('Send a request with an invalid password')
@pytest.mark.parametrize('password', ['', '        ', '1 ', '   1234567    Q a ', '12345678',
                                      'qazwsxedc', 'QWERASDFZ', 'Aqazwsxedc', 'Фйц123456',
                                      'Qaz1234', 'Qaz12345678901234567890123456789012345678'
                                                 '90123456789xexexcefcrgvthc12345678901235567'
                                                 '90qertyooasdfghkozxvbnmqeryoadfhjkzxcvbnmasdfghk'
                                                 'qetyuiizsdfghjjkjzxcderfvtgbyhnqazwsx1234567890qw'
                                                 'ertyuioasdgghjklzxcvbnmmececfvrvtgbhbybcedxwsxwdce'
                                                 'fvrgtbrcexwxexrgvtvhbrcfed', 'QAZ12345', 'Qaz12345`',
                                      'Qaz12345,<.>/?;:~!@#$%^&*()_-+=|'])
@pytest.mark.parametrize('email', ['test.trainlab@gmail.com'])
def test_invalid_password(connect_db, password, email, check_existence_and_delete_email):
    with allure.step('Send request to create user'):
        request = post_request_create_user(f'{email}', 'Vasia', f'{password}')
    with allure.step('Check status code'):
        assert request.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request with empty fields')
def test_registration_with_empty_fields(connect_db):
    with allure.step('Send request to create user'):
        request = post_request_create_user('', '', '')
    with allure.step('Check status code'):
        assert request.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request with empty username and password')
def test_registration_with_empty_username_and_password(connect_db):
    with allure.step('Send request to create user'):
        request = post_request_create_user('test.trainlab@gmail.com', '', '')
    with allure.step('Check status code'):
        assert request.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request with empty email and password')
def test_registration_with_empty_email_and_password(connect_db):
    with allure.step('Send request to create user'):
        request = post_request_create_user('', 'Vasia', '')
    with allure.step('Check status code'):
        assert request.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request with empty username and email')
def test_registration_with_empty_username_and_email(connect_db):
    with allure.step('Send request to create user'):
        request = post_request_create_user('', '', 'Qaz12345')
    with allure.step('Check status code'):
        assert request.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request with data existing user')
@pytest.mark.parametrize('email', ['test.trainlab@gmail.com'])
def test_registration_with_existing_user(connect_db, check_existence_and_delete_email, email):
    with allure.step('Send request to create user'):
        post_request_create_user(f'{email}', 'Vasia', f'Qaz12345')
    with allure.step('Send a request with existing data'):
        request = post_request_create_user(f'{email}', 'Vasia', f'Qaz12345')
    with allure.step('Check status code'):
        assert request.status_code == 400


@allure.feature('Registration')
@allure.story('Send a request confirm registration')
@pytest.mark.parametrize('email', ['test.trainlab@gmail.com'])
def test_confirm_registration(connect_db, check_existence_and_delete_email, email):
    with allure.step('Send request to create user'):
        post_request_create_user(f'{email}', 'Vasia', f'Qaz12345')
    with allure.step('Send request confirm registration'):
        request = get_request_confirm_registration(f'{email}')
    with allure.step('Check status code'):
        assert request.status_code == 200
