import json
from flask import make_response

JSON_MIME_TYPE = 'application/json; charset=utf-8'
STATUS = 'success'


def search_notification(notifications, notification_id):
    for notification in notifications:
        if notification['id'] == notification_id:
            return notification

# utils file to store re used APIS's
def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)


def onerror_response(error):
    error = json.dumps({'status': 'failed',
                        'error': error})
    return json_response(error)

def is_data_not_exist(cursor):
    count = len(cursor.fetchall())
    # Check if user exists
    if count == 0:
        return True
    else:
        return False

def is_data_exist(cursor):
    count = len(cursor.fetchall())
    # Check if user exists
    if count > 0:
        return True
    else:
        return False


def onsuccess_response(result):
    format = {'status': 'success',
              'result': result}
    return json_response(json.dumps(format))
