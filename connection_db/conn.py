import psycopg2
from sshtunnel import SSHTunnelForwarder


ssh_host = '165.22.78.188'
ssh_port = 22
ssh_username = 'amikulich'
ssh_password = '/Users/artemmikulich/.ssh/id_ed25519'

db_host = 'tldb-postgresql-fra1-81116-do-user-14346310-0.b.db.ondigitalocean.com'
db_port = 25060
db_username = 'trainlab'
db_password = 'AVNS_yXtS-TsJq6YJmCAe19y'
db_name = 'trainlab'
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