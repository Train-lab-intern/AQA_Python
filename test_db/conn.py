import psycopg2
from sshtunnel import SSHTunnelForwarder
from settings import (
    ssh_host, ssh_port, ssh_username, ssh_password,
    db_host, db_port, db_username, db_password, db_name
)


def ssh_tunnel_and_db_connection(func):
    def wrapper(*args, **kwargs):
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

            result = func(conn, *args, **kwargs)

            conn.close()

            return result

    return wrapper
