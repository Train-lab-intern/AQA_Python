import psycopg2
from sshtunnel import SSHTunnelForwarder
import bd_data as bd


def change_text_in_database_by_front_id(front_id_bd, text_to_change):
    try:
        with SSHTunnelForwarder(
                (f"{bd.bd_ip}", 22),
                ssh_username=f"{bd.ssh_username}",
                ssh_private_key=f"{bd.ssh_private_key}",
                remote_bind_address=(f"{bd.remote_bind_address}", 25060)) as server:

            server.start()

            params = {
                'database': f"{bd.database}",
                'user': f"{bd.user}",
                'password': f"{bd.password}",
                'host': f"{bd.host}",
                'port': server.local_bind_port
            }

            conn = psycopg2.connect(**params)
            curs = conn.cursor()
            curs.execute(f"update frontend_data SET text='{text_to_change}' WHERE front_id='{front_id_bd}';")
            conn.commit()
            conn.close()
            return True

    except:
        print("Connection Failed")


def take_text_from_database_by_front_id(front_id_bd):
    try:
        with SSHTunnelForwarder(
                (f"{bd.bd_ip}", 22),
                ssh_username=f"{bd.ssh_username}",
                ssh_private_key=f"{bd.ssh_private_key}",
                remote_bind_address=(f"{bd.remote_bind_address}", 25060)) as server:

            server.start()

            params = {
                'database': f"{bd.database}",
                'user': f"{bd.user}",
                'password': f"{bd.password}",
                'host': f"{bd.host}",
                'port': server.local_bind_port
            }

            conn = psycopg2.connect(**params)
            curs = conn.cursor()
            curs.execute(f"SELECT text FROM frontend_data WHERE front_id='{front_id_bd}';")
            text = curs.fetchall()
            text_by_id = text[0][0]
            conn.close()
            return text_by_id

    except:
        print("Connection Failed")
