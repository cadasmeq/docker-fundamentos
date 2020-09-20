from flask import Flask
from redis import Redis
import os
import socket
app = Flask(__name__)
redis = Redis(host='redis', port=6379, socket_connect_timeout=5)
host = socket.gethostname()

@app.route('/')
def hello():
    redis.incr('hits')
    return '\nHelloWorld!\n I have been seen %s times. \nMyHost name is %s \n\n' % (redis.get('hits'), host)

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)