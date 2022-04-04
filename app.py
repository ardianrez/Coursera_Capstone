import connection

if __name__ == "__main__":
    path = os.getcwd()
    path_query = path + '/sql/'
    file_query = 'dml_query_1.sql'
    conn = connection.db_connect()
    cur=conn.sursor()

    with open(path_query + file_query,'r') as file:
        query = file.read()

    cur.execute(query)
    cur.fetchall()
