from test_db.conn import ssh_tunnel_and_db_connection


@ssh_tunnel_and_db_connection
def check_text_where_id_1(connection):
    cursor = connection.cursor()
    new_query = """SELECT front_id FROM frontend_data WHERE id=1"""
    cursor.execute(new_query)
    front_id_result = cursor.fetchone()[0]
    query = "SELECT text FROM frontend_data WHERE front_id=%s"
    cursor.execute(query, (str(front_id_result),))
    result = cursor.fetchone()[0]
    cursor.close()
    return result


@ssh_tunnel_and_db_connection
def check_text_where_id_2(connection):
    cursor = connection.cursor()
    new_query = """SELECT front_id FROM frontend_data WHERE id=2"""
    cursor.execute(new_query)
    front_id_result = cursor.fetchone()[0]
    query = "SELECT text FROM frontend_data WHERE front_id=%s"
    cursor.execute(query, (str(front_id_result),))
    result = cursor.fetchone()[0]
    cursor.close()
    return result


@ssh_tunnel_and_db_connection
def check_text_where_id_3(connection):
    cursor = connection.cursor()
    new_query = """SELECT front_id FROM frontend_data WHERE id=3"""
    cursor.execute(new_query)
    front_id_result = cursor.fetchone()[0]
    query = "SELECT text FROM frontend_data WHERE front_id=%s"
    cursor.execute(query, (str(front_id_result),))
    result = cursor.fetchone()[0]
    cursor.close()
    return result


@ssh_tunnel_and_db_connection
def check_text_where_id_4(connection):
    cursor = connection.cursor()
    new_query = """SELECT front_id FROM frontend_data WHERE id=4"""
    cursor.execute(new_query)
    front_id_result = cursor.fetchone()[0]
    query = "SELECT text FROM frontend_data WHERE front_id=%s"
    cursor.execute(query, (str(front_id_result),))
    result = cursor.fetchone()[0]
    cursor.close()
    return result


@ssh_tunnel_and_db_connection
def check_text_where_id_5(connection):
    cursor = connection.cursor()
    new_query = """SELECT front_id FROM frontend_data WHERE id=5"""
    cursor.execute(new_query)
    front_id_result = cursor.fetchone()[0]
    query = "SELECT text FROM frontend_data WHERE front_id=%s"
    cursor.execute(query, (str(front_id_result),))
    result = cursor.fetchone()[0]
    cursor.close()
    return result


@ssh_tunnel_and_db_connection
def check_text_where_id_6(connection):
    cursor = connection.cursor()
    new_query = """SELECT front_id FROM frontend_data WHERE id=6"""
    cursor.execute(new_query)
    front_id_result = cursor.fetchone()[0]
    query = "SELECT text FROM frontend_data WHERE front_id=%s"
    cursor.execute(query, (str(front_id_result),))
    result = cursor.fetchone()[0]
    cursor.close()
    return result


@ssh_tunnel_and_db_connection
def check_text_where_id_7(connection):
    cursor = connection.cursor()
    new_query = """SELECT front_id FROM frontend_data WHERE id=7"""
    cursor.execute(new_query)
    front_id_result = cursor.fetchone()[0]
    query = "SELECT text FROM frontend_data WHERE front_id=%s"
    cursor.execute(query, (str(front_id_result),))
    result = cursor.fetchone()[0]
    cursor.close()
    return result


@ssh_tunnel_and_db_connection
def check_text_where_id_8(connection):
    cursor = connection.cursor()
    new_query = """SELECT front_id FROM frontend_data WHERE id=8"""
    cursor.execute(new_query)
    front_id_result = cursor.fetchone()[0]
    query = "SELECT text FROM frontend_data WHERE front_id=%s"
    cursor.execute(query, (str(front_id_result),))
    result = cursor.fetchone()[0]
    cursor.close()
    return result


@ssh_tunnel_and_db_connection
def check_text_where_id_9(connection):
    cursor = connection.cursor()
    new_query = """SELECT front_id FROM frontend_data WHERE id=9"""
    cursor.execute(new_query)
    front_id_result = cursor.fetchone()[0]
    query = "SELECT text FROM frontend_data WHERE front_id=%s"
    cursor.execute(query, (str(front_id_result),))
    result = cursor.fetchone()[0]
    cursor.close()
    return result

