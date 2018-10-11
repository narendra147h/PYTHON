import json
import uuid
import sqlite3
from flask import Flask, request, g
from utils.uitils import json_response, JSON_MIME_TYPE, onsuccess_response, onerror_response, is_data_not_exist, \
    is_data_exist

# fetch all user details
def user():
    try:
        cursor = g.db.execute('SELECT id, name, fcm_token FROM user;')
    except:
        if request.content_type != JSON_MIME_TYPE:
            return onerror_response('No data available')

    user = [{
        'id': row[0],
        'name': row[1],
        'fcm_token': row[2]
    } for row in cursor.fetchall()]

    return onsuccess_response(user)

# store new user
def store_user():
    print(request)
    print(request.content_type)
    if request.content_type != JSON_MIME_TYPE:
        return onerror_response('Invalid Content Type')

    data = request.json
    if not all([data.get('name')]):
        return onerror_response('Missing field/s (name) (fcm_token)')

    query = ('INSERT INTO user ("name", "fcm_token") ' 'VALUES (:name, :fcm_token);')

    params = {
        'name': data['name'],
        'fcm_token': ''
    }
    g.db.execute(query, params)
    g.db.commit()

    return user_details_resp()

# returns user details
def user_details_resp():
    try:
        cursor = g.db.execute('SELECT * FROM user ORDER BY id DESC LIMIT 1;')
    except:
        if request.content_type != JSON_MIME_TYPE:
            return onerror_response('No data available')

    user = [{
        'id': row[0],
        'name': row[1],
        'fcm_token': row[2]
    } for row in cursor.fetchall()]

    return onsuccess_response(user)

# update fcm token
def update_token(user_id):
    if request.content_type != JSON_MIME_TYPE:
        return onerror_response('Invalid Content Type')

    data = request.json
    if not all([data.get('fcm_token')]):
        return onerror_response('Missing field/s (fcm_token)')

    params = {'id': user_id}
    query = 'SELECT * FROM user WHERE user.id = :id'

    cursor = g.db.execute(query, params)
    if is_data_not_exist(cursor):
        return onerror_response("No User exist")

    # Update it
    token = data.get('fcm_token')
    g.db.execute('''UPDATE user SET fcm_token = ? WHERE id = ?''', (token, user_id))
    g.db.commit()

    params = {'id': user_id}
    query = 'SELECT * FROM user WHERE user.id = :id'
    cursor = g.db.execute(query, params)

    user = [{
        'id': row[0],
        'name': row[1],
        'fcm_token': row[2]
    } for row in cursor.fetchall()]

    return onsuccess_response(user)

# returns registered user to collect fcm token
def get_users():
    try:
        cursor = g.db.execute('SELECT fcm_token FROM user;')
    except:
        if request.content_type != JSON_MIME_TYPE:
            return onerror_response('No data available')

    user = [{
        'fcm_token': row[0]
    } for row in cursor.fetchall()]

    fcm_reg_list = []
    for chunks in user:
        for attribute, value in chunks.items():
            fcm_reg_list.append('device '+ value)
    return fcm_reg_list
