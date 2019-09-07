import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return str(os.system('calc'))


if __name__ == '__main__':
    app.run(port=80)