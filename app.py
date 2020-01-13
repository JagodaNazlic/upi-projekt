from bottle import Bottle, run, \
     template, debug, get, route, static_file, request, post

import os, sys, sqlite3, datetime

from create_database import demoPodaci, citajPodatke, sacuvaj_zivotinju

demoPodaci()
citajPodatke()

dirname = os.path.dirname(sys.argv[0])
template_path = dirname + '\\views'
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

@app.route('/search')
def ucitaj():
    podaci = citajPodatke()
    return template('search', data = podaci, template_lookup=[template_path])


@app.route('/newA',method=['GET','POST'])
def newAnimal():
    if request.POST.get('unesi','').strip():
        imeziv = request.POST.get('ime')
        vrsta = request.POST.get('vrsta')
        dob = request.POST.get('dob')
        spol = request.POST.get('spol')
        zdr_stanje = request.POST.get('zdrst')
        datodl = request.POST.get('datOdlaska')
        datdol = datetime.datetime.now()
        financije = request.POST.get('fin')
        interes = request.POST.get(0)

        sacuvaj_zivotinju(imeziv, vrsta, dob, spol, zdr_stanje, datodl, datdol, financije, interes)

        return template("search", rows=rows)
    else:
        return template("new_animal")


@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/img')

@app.route('/')
def pocetna():
    con=sqlite3.connect('baza_podataka.db')
    cur=con.cursor()
    rows=cur.execute('SELECT * FROM animals')

    data = {"developer_name": "PMF student",
            "developer_organization": "PMF"}
    return template('index', data = data, rows=rows)
                          

run(app, host='localhost', port = 4040)



