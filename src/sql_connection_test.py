import mysql.connector
import os 
from dotenv import load_dotenv
load_dotenv()

host = os.getenv('MYSQL_HOST')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
database = os.getenv('MYSQL_DATABASE')

try:
    connection = mysql.connector.connect(host=host, user=user, password=password, database=database)
    print('Connection successful')
except Exception as e:
    print('Connection failed', e)
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print('Connection is closed')