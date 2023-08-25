import time
import socket
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory


app = Flask(
    __name__,
    template_folder='.',
    static_folder='.',
    static_url_path='',
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pofile/<usr>')
def pofile(usr):
    return render_template('/templates/pofile.html', usr=usr)

@app.route('/login', methods=['GET', 'POST'])
def login():
    def valid_login(usr,psw):
        with open('./dynamic/usr.csv') as f:
            for i in f.readlines():
                key = i.split(',')
                if usr == key[0] and psw == key[1]:
                    return True
        return False
    error = ''
    if request.method == 'POST':
        if valid_login(request.form['usr'],request.form['psd']):
            return redirect(url_for('pofile',usr=request.form['usr']))
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('/templates/login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('/templates/register.html')


app.run('0.0.0.0',port=5000)