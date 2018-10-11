#!/usr/bin/python

import sqlite3
from flaskr.db import DATABASE_PATH

conn = sqlite3.connect(DATABASE_PATH)

print ("Opened database successfully");

conn.execute('DELETE FROM user;')
conn.execute('DELETE FROM notifications;')

conn.close()
print ("Closed database successfully");