from bottle import Bottle, run, \
     template, debug, get, route, static_file, request, post

import os, sys, sqlite3, datetime

dirname = os.path.dirname(sys.argv[0])

app = Bottle()
debug(True)

@app.route('/static/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root=dirname+'/static/assets/css')

@app.route('/static/<filename:re:.*\.css.map>')
def send_cssmap(filename):
    return static_file(filename, root=dirname+'/static/assets/css')

@app.route('/static/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root=dirname+'/static/assets/js')

@app.route('/static/<filename:re:.*\.js.map>')
def send_jsmap(filename):
    return static_file(filename, root=dirname+'/static/assets/js')



@app.route('/')
def index():
    data = {"developer_name": "PMF student",
            "developer_organization": "PMF"}
    return template('index', data = data)

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/img')

@app.route('/newA')
def newAnimal():
    return template('new_animal')


run(app, host='localhost', port = 4040)



