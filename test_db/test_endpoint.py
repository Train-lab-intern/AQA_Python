import requests
from test_db.query_from_db import *

def test_response():
    url = 'https://back-test-4zwpv.ondigitalocean.app/front/pages/1'
    response = requests.get(url)
    assert response.status_code == 200, f'Expected status code 200, but was given {response.status_code}'


# with invalid url
def test_response_negative():
    url = 'https://back-test-4zwpv.ondigitalocean.app/front/pages/11'
    response = requests.get(url)
    assert response.status_code != 200, f'Expected status code not 200, but was given {response.status_code}'


@ssh_tunnel_and_db_connection
def test_text_id_1_1(connection):
    url = 'https://back-test-4zwpv.ondigitalocean.app/front/pages/1'
    response = requests.get(url)
    response_json = response.json()
    text_from_db = check_text_where_id_1(connection)
    text_from_api = response_json['1.1']
    assert text_from_api == text_from_db, f'Expected text {text_from_db} but was {text_from_api()}'


@ssh_tunnel_and_db_connection
def test_text_id_1_2(connection):
    url = 'https://back-test-4zwpv.ondigitalocean.app/front/pages/1'
    response = requests.get(url)
    response_json = response.json()
    text_from_db = check_text_where_id_2(connection)
    text_from_api = response_json['1.2']
    assert text_from_api == text_from_db, f'Expected text {text_from_db} but was {text_from_api()}'


@ssh_tunnel_and_db_connection
def test_text_id_1_3(connection):
    url = 'https://back-test-4zwpv.ondigitalocean.app/front/pages/1'
    response = requests.get(url)
    response_json = response.json()
    text_from_db = check_text_where_id_3(connection)
    text_from_api = response_json['1.3']
    assert text_from_api == text_from_db, f'Expected text {text_from_db} but was {text_from_api()}'


@ssh_tunnel_and_db_connection
def test_text_id_1_4(connection):
    url = 'https://back-test-4zwpv.ondigitalocean.app/front/pages/1'
    response = requests.get(url)
    response_json = response.json()
    text_from_db = check_text_where_id_4(connection)
    text_from_api = response_json['1.4']
    assert text_from_api == text_from_db, f'Expected text {text_from_db} but was {text_from_api()}'

@ssh_tunnel_and_db_connection
def test_text_id_1_5(connection):
    url = 'https://back-test-4zwpv.ondigitalocean.app/front/pages/1'
    response = requests.get(url)
    response_json = response.json()
    text_from_db = check_text_where_id_5(connection)
    text_from_api = response_json['1.5']
    assert text_from_api == text_from_db, f'Expected text {text_from_db} but was {text_from_api()}'

@ssh_tunnel_and_db_connection
def test_text_id_1_6(connection):
    url = 'https://back-test-4zwpv.ondigitalocean.app/front/pages/1'
    response = requests.get(url)
    response_json = response.json()
    text_from_db = check_text_where_id_6(connection)
    text_from_api = response_json['1.6']
    assert text_from_api == text_from_db, f'Expected text {text_from_db} but was {text_from_api()}'

@ssh_tunnel_and_db_connection
def test_text_id_1_7(connection):
    url = 'https://back-test-4zwpv.ondigitalocean.app/front/pages/1'
    response = requests.get(url)
    response_json = response.json()
    text_from_db = check_text_where_id_7(connection)
    text_from_api = response_json['1.7']
    assert text_from_api == text_from_db, f'Expected text {text_from_db} but was {text_from_api()}'

@ssh_tunnel_and_db_connection
def test_text_id_1_8(connection):
    url = 'https://back-test-4zwpv.ondigitalocean.app/front/pages/1'
    response = requests.get(url)
    response_json = response.json()
    text_from_db = check_text_where_id_8(connection)
    text_from_api = response_json['1.8']
    assert text_from_api == text_from_db, f'Expected text {text_from_db} but was {text_from_api()}'

@ssh_tunnel_and_db_connection
def test_text_id_1_9(connection):
    url = 'https://back-test-4zwpv.ondigitalocean.app/front/pages/1'
    response = requests.get(url)
    response_json = response.json()
    text_from_db = check_text_where_id_9(connection)
    text_from_api = response_json['1.9']
    assert text_from_api == text_from_db, f'Expected text {text_from_db} but was {text_from_api()}'