import psycopg2
import pytest
from sshtunnel import SSHTunnelForwarder
import settings
import api_response
import query_from_db


@pytest.fixture()
def connection():
    with SSHTunnelForwarder(
            (settings.ssh_host, settings.ssh_port),
            ssh_username=settings.ssh_username,
            ssh_password=settings.ssh_password,
            remote_bind_address=(settings.db_host, settings.db_port)) as tunnel:
        print('Connected to server')
        conn = psycopg2.connect(
            host='localhost',
            port=tunnel.local_bind_port,
            user=settings.db_username,
            password=settings.db_password,
            database=settings.db_name
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
