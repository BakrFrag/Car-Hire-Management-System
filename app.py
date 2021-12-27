from flask import Flask
from flask_mysqldb import MySQL
from .config import *
"""
define app variable
"""

app = Flask(__name__);
mysql=MySQL(app)
app.config['MYSQL_HOST'] = DB_HOST
app.config['MYSQL_USER'] = DB_USER
app.config['MYSQL_PASSWORD'] = DB_PASSWORD
app.config['MYSQL_DB'] = DB_NAME
cursor = mysql.connection.cursor()
 
mysql = MySQL(app)

app.run(host=HOST, port=PORT)