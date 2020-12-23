from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3
app = Flask(__name__, static_url_path='/static')

app.config['DEBUG']=True
app.config['SECRET_KEY'] = 'ddd91417-11fa-40b5-98c1-fde58db3086d'


@app.route('/')
def index():
    return  render_template('necklaces.html')

@app.route('/necklaces')
def necklaces():
    return  render_template('necklaces.html')

# @app.route('/logout')
# def logout():
#     if 'username' in session:
#         session.pop('username')
# #    return redirect (url_for('index'))
#     return redirect (url_for('necklaces'))
#
