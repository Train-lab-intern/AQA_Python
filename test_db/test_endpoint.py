import requests


def test_response():
    url = 'https://back-test-4zwpv.ondigitalocean.app/front/pages/1'
    response = requests.get(url, timeout=6)
    assert response.status_code == 200, \
        f'Expected status code 200, but was given {response.status_code}'


# with invalid url
def test_response_negative():
    url = 'https://back-test-4zwpv.ondigitalocean.app/front/pages/11'
    response = requests.get(url, timeout=6)
    assert response.status_code != 200, \
        f'Expected status code not 200, but was given {response.status_code}'


def test_text_front_id_1_1(get_data_from_db, get_data_from_api):
    assert get_data_from_api['id_1_1'] == get_data_from_db['id_1_1'], \
        f'Expected {get_data_from_db["id_1_1"]} ' \
        f'but was {get_data_from_api["id_1_1"]}'


def test_text_front_id_1_2(get_data_from_db, get_data_from_api):
    assert get_data_from_api['id_1_2'] == get_data_from_db['id_1_2'], \
        f'Expected {get_data_from_db["id_1_2"]} ' \
        f'but was {get_data_from_api["id_1_2"]}'


def test_text_front_id_1_3(get_data_from_db, get_data_from_api):
    assert get_data_from_api['id_1_3'] == get_data_from_db['id_1_3'], \
        f'Expected {get_data_from_db["id_1_3"]} ' \
        f'but was {get_data_from_api["id_1_3"]}'


def test_text_front_id_1_4(get_data_from_db, get_data_from_api):
    assert get_data_from_api['id_1_4'] == get_data_from_db['id_1_4'], \
        f'Expected {get_data_from_db["id_1_4"]} ' \
        f'but was {get_data_from_api["id_1_4"]}'


def test_text_front_id_1_5(get_data_from_db, get_data_from_api):
    assert get_data_from_api['id_1_5'] == get_data_from_db['id_1_5'], \
        f'Expected {get_data_from_db["id_1_5"]} ' \
        f'but was {get_data_from_api["id_1_5"]}'


def test_text_front_id_1_6(get_data_from_db, get_data_from_api):
    assert get_data_from_api['id_1_6'] == get_data_from_db['id_1_6'], \
        f'Expected {get_data_from_db["id_1_6"]} ' \
        f'but was {get_data_from_api["id_1_6"]}'


def test_text_front_id_1_7(get_data_from_db, get_data_from_api):
    assert get_data_from_api['id_1_7'] == get_data_from_db['id_1_7'], \
        f'Expected {get_data_from_db["id_1_7"]} ' \
        f'but was {get_data_from_api["id_1_7"]}'


def test_text_front_id_1_8(get_data_from_db, get_data_from_api):
    assert get_data_from_api['id_1_8'] == get_data_from_db['id_1_8'], \
        f'Expected {get_data_from_db["id_1_8"]} ' \
        f'but was {get_data_from_api["id_1_8"]}'


def test_text_front_id_1_9(get_data_from_db, get_data_from_api):
    assert get_data_from_api['id_1_9'] == get_data_from_db['id_1_9'], \
        f'Expected {get_data_from_db["id_1_9"]} ' \
        f'but was {get_data_from_api["id_1_9"]}'
