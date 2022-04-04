import connection

if __name__ == "__main__":
    path = os.getcwd()
    path_query = path + '/sql/'
    conn = connection.db_connect()
    query = 