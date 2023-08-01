import psycopg2
import pytest
from sshtunnel import SSHTunnelForwarder
from settings import (
    ssh_host, ssh_port, ssh_username, ssh_password,
    db_host, db_port, db_username, db_password, db_name
)
import api_response
import query_from_db


@pytest.fixture()
def connection():
    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_username,
            ssh_password=ssh_password,
            remote_bind_address=(db_host, db_port)) as tunnel:
        print('Connected to server')
        conn = psycopg2.connect(
            host='localhost',
            port=tunnel.local_bind_port,
            user=db_username,
            password=db_password,
            database=db_name
        )
        yield conn
        conn.close()


@pytest.fixture()
def get_data_from_api():
    return {
        'id_1_1': api_response.text_from_from_id_1_1(),
        'id_1_2': api_response.text_from_from_id_1_2(),
        'id_1_3': api_response.text_from_from_id_1_3(),
        'id_1_4': api_response.text_from_from_id_1_4(),
        'id_1_5': api_response.text_from_from_id_1_5(),
        'id_1_6': api_response.text_from_from_id_1_6(),
        'id_1_7': api_response.text_from_from_id_1_7(),
        'id_1_8': api_response.text_from_from_id_1_8(),
        'id_1_9': api_response.text_from_from_id_1_9()
    }


@pytest.fixture()
def get_data_from_db(connection):
    return {
        'id_1_1': query_from_db.check_text_where_front_id_1_1(connection),
        'id_1_2': query_from_db.check_text_where_front_id_1_2(connection),
        'id_1_3': query_from_db.check_text_where_front_id_1_3(connection),
        'id_1_4': query_from_db.check_text_where_front_id_1_4(connection),
        'id_1_5': query_from_db.check_text_where_front_id_1_5(connection),
        'id_1_6': query_from_db.check_text_where_front_id_1_6(connection),
        'id_1_7': query_from_db.check_text_where_front_id_1_7(connection),
        'id_1_8': query_from_db.check_text_where_front_id_1_8(connection),
        'id_1_9': query_from_db.check_text_where_front_id_1_9(connection)
    }
