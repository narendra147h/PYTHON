#!/usr/bin/python

import sqlite3
import flaskr.db
from flaskr.db import DATABASE_DIR,DATABASE_PATH
import os

if not os.path.exists(DATABASE_DIR):
    os.makedirs(DATABASE_DIR)

conn = sqlite3.connect(DATABASE_PATH)

print("Opened database successfully");

conn.execute('DROP TABLE IF EXISTS user;')
conn.execute('DROP TABLE IF EXISTS notifications;')

conn.execute('''CREATE TABLE notifications
         (id INTEGER PRIMARY KEY AUTOINCREMENT    NOT NULL,
         notification_id            INT     NOT NULL,
         name           TEXT    NOT NULL,
         priority           TEXT    NOT NULL,
         count           INT    NOT NULL);''')

conn.execute('''CREATE TABLE user
         (id INTEGER PRIMARY KEY AUTOINCREMENT    NOT NULL,
         name           TEXT    NOT NULL,
         fcm_token           TEXT);''')

conn.close()
print("Closed database successfully");
