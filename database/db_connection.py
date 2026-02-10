import mysql.connector
def ma_connexion():
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='boutique'
    )
    return conn
