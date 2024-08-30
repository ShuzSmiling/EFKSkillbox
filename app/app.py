import logging
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
    return '<h1 style=color:red>HTTP 200 OK!</h1>'

@app.route('/one')
def one():
    return '<h1 style=color:blue>HTTP 201 Created!</h1>', 201


@app.route('/two')
def two():
    return '<h1 style=color:yellow>HTTP 202 Accepted!</h1>', 202


@app.route('/three')
def three():
    return '<h1 style=color:pink>HTTP 203 Non-Authoritative Information!</h1>', 203


@app.route('/four')
def four():
    return 'HTTP 201 No Content', 204


@app.route('/five')
def five():
    return 'HTTP 205 Reset Content', 205


@app.route('/error')
def error():
    return 'HTTP 500 Internal Server Error', 500


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)
else:
    gunicorn_logger = logging.getLogger('gunicorn.Error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

