import psycopg2
from sshtunnel import SSHTunnelForwarder
from settings import *

try:
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

                # Передаем соединение в декорируемую функцию
                result = func(conn)

                # Закрываем соединение после выполнения функции
                conn.close()

                return result

        return wrapper

except BaseException as e:
    print(f'connection failed. {e}')
