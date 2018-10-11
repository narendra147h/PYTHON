# implementation for notification API
import json
import sqlite3
from flask import Flask, request, g
from utils.uitils import json_response, JSON_MIME_TYPE,onerror_response, onsuccess_response
from fcm._fcm_utils_ import forward_push
from api._req_user_ import get_users

# Returns notifications list
def query_notiication_list():
    try:
        cursor = g.db.execute('SELECT id, notification_id, name, priority, count FROM notifications;')
    except:
        if request.content_type != JSON_MIME_TYPE:
            return onerror_response('No data available')

    notifications = [{
        'id': row[0],
        'notification_id': row[1],
        'name': row[2],
        'priority': row[3],
        'count': row[4]
    } for row in cursor.fetchall()]

    return onsuccess_response(notifications)
# Stores notifications data
def store_notification():
    print(request)
    print(request.content_type)
    # if request.content_type != JSON_MIME_TYPE:
    #     return onerror_response('Invalid Content Type')

    data = request.json
    if not all([data.get('notification_id'), data.get('name'), data.get('priority'), data.get('count')]):
        error = json.dumps({'error': 'Missing field/s (notification_id, name, priority, count)'})
        return json_response(error, 400)

    query = ('INSERT INTO notifications ("notification_id", "name", "priority", "count") ' 'VALUES (:notification_id, :name, :priority, :count);')

    params = {
        'notification_id': data['notification_id'],
        'name': data['name'],
        'priority': data['priority'],
        'count': data['count']
    }
    g.db.execute(query, params)
    g.db.commit()

    try:
        cursor = g.db.execute('SELECT id, notification_id, name, priority, count FROM notifications;')
    except:
        if request.content_type != JSON_MIME_TYPE:
            return onerror_response('No data available')

    notifications = [{
        'id': row[0],
        'notification_id': row[1],
        'name': row[2],
        'priority': row[3],
        'count': row[4]
    } for row in cursor.fetchall()]

    forward_push(get_users(), notification_id_for_push())
    return onsuccess_response(notifications)

# returns user details
def notification_id_for_push():
    try:
        cursor = g.db.execute('SELECT * FROM notifications ORDER BY id DESC LIMIT 1;')
    except:
        if request.content_type != JSON_MIME_TYPE:
            return onerror_response('No data available')

    notifications = [{
        'id': row[0],
        'notification_id': row[1],
        'name': row[2],
        'priority': row[3],
        'count': row[4]
    } for row in cursor.fetchall()]

    return notifications