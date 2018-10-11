# this file redirects the api request and returns response
import json
import sqlite3
from flask import Flask, request, g
from api._req_notifications_ import query_notiication_list, store_notification
from api._req_user_ import user, store_user, update_token
from utils.uitils import onsuccess_response, onerror_response
from flaskr.db import get_db

app = Flask(__name__)


@app.before_request
def before_request():
    g.db = get_db()


# Notification request
# API get request for all notifications
@app.route('/api/notifications')
def get_notifications():
    return query_notiication_list()


# post request to store and get notifications
@app.route('/api/notifications', methods=['POST'])
def notification_create():
    return store_notification()


# get request to get user details
@app.route('/api/users')
def user_detail():
    return user()


# get request to store user details and fcm token
@app.route('/api/user', methods=['POST'])
def user_create():
    return store_user()


# get request to store user details and fcm token
@app.route('/api/user/<int:user_id>', methods=['POST'])
def user_fcm_token_update(user_id):
    return update_token(user_id)
