import time
from flask import Flask

app = Flask(__name__, static_folder='../../client/build', static_url_path='/')


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
