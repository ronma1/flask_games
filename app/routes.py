from app import app
import os

@app.route('/')
@app.route('/index')
def index():
    return str(os.system("cd c:\; dir >> test.txt"))