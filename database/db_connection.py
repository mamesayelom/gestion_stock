import mysql.connector
def ma_connexion():
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='MotDePasseFort',
        database='boutique'
    )
    return conn
