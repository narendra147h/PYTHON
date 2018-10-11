# this files starts server
import os
from _config_route_ import app

if __name__ == '__main__':
    app.debug = True
    app.config['DATABASE_NAME'] = 'NOTIFICATIONS.db'
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
