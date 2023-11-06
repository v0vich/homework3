from flask import Flask
from utils import phones_create, phones_read, phones_update, phones_delete
from create_table import create_table

app = Flask(__name__)
create_table()


@app.route('/phones/create')
def create():
    return phones_create()


@app.route('/phones/read')
def read():
    return phones_read()


@app.route('/phones/update')
def update():
    return phones_update()


@app.route('/phones/delete')
def delete():
    return phones_delete()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
