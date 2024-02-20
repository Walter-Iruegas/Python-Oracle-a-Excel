import cx_Oracle

def conectar_oracle():
    try:
        connection = cx_Oracle.connect(
            user='ADMIN',
            password='123',
            dsn='localhost:1521/ORCL',
            encoding='UTF-8'
        )
        print(connection.version)
        return connection
    except Exception as ex:
        print("Error al conectar a Oracle:", ex)
        return None
