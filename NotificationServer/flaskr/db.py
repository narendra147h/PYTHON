import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

DATABASE_DIR = "C:\sqlite\db\\"
DATABASE_NAME = "NOTIFICATIONS.db"
DATABASE_PATH = DATABASE_DIR + DATABASE_NAME

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE_PATH,
                               detect_types=sqlite3.PARSE_DECLTYPES
                               )
        g.db.row_factory = sqlite3.Row

    return g.db
