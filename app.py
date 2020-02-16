from bottle import Bottle, run,redirect, \
     template, debug, get, route, static_file, request, post

import os, sys, sqlite3, datetime

from create_database import citajPodatke,samoMace,samoPsi, prihvatiZ, sacuvaj_zivotinju, signUpRadnik, \
     logInRadnik, azuriraj, azurirajZivotinju, interes, idRadnika, citajPodatkeLog, sortiranje, \
     sacuvaj_udomitelja, citajPodatkeUd, idZodU, imeZivotinje

citajPodatke()
save_id=0

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

@app.route('/search',method=['GET','POST'])
def ucitaj():
    data = citajPodatke()
    print("ovo su podaci:")
    print(data)
    return template('search', data = data, template_lookup=[template_path])


@app.route('/newA',method=['GET','POST'])
def newAnimal():
    if request.POST.get('unesi','').strip():
        imeziv = request.POST.get('ime')
        vrsta = request.POST.get('vrsta')
        dob = request.POST.get('dob')
        spol = request.POST.get('spol')
        zdr_stanje = request.POST.get('zdrst')
        datodl = request.POST.get('datOdlaska')
        datdol = datetime.datetime.now().date()
        financije = request.POST.get('fin')
        interes = "0"
        id_radnika = idRadnika(user)
    
        udomljen = 0
        
        sacuvaj_zivotinju(imeziv, vrsta, dob, spol, zdr_stanje, datodl, datdol, financije, interes, id_radnika, udomljen)
        

        redirect('/index')
    else:
        return template("new_animal")

@app.route('/upd<upd:re:[0-9]+>',method=['GET','POST'])
def upd(upd):
    update = upd
    global save_id
##    if save_id == 0:
##        redirect('/')
     
    if request.POST.get('update','').strip():
        imeziv = request.POST.get('ime')
        vrsta = request.POST.get('vrsta')
        dob = request.POST.get('dob')
        spol = request.POST.get('spol')
        zdr_stanje = request.POST.get('zdrst')
        datodl = request.POST.get('datOdlaska')
        datdol = datetime.datetime.now().date()
        financije = request.POST.get('fin')
        interes = "0"
        id_radnika = idRadnika(user)
        save_id=id_radnika
        udomljen = 0
        azuriraj(imeziv, vrsta, dob, spol, zdr_stanje, datodl, datdol, financije, interes, id_radnika,udomljen, update)
        

        redirect('/index')
    else:
        result = azurirajZivotinju(update)
        save_id = result[10]
        imeziv = result[1]
        dob=result[3]
        datodl=result[6]
        financije=result[8]
        stanje=result[5]
        
        return template("updateAnimal",update=update,imeziv=imeziv,dob=dob,datodl=datodl,financije=financije,stanje=stanje)
        
        

@app.route('/delete<delete:re:[0-9]+>')
def delete_delete(delete):
    con=sqlite3.connect('baza_podataka.db')
    cur=con.cursor()
    idd=delete
    cur.execute('DELETE FROM animals WHERE id=?',(idd,))
    con.commit()
    con.close()
    redirect('/search')

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/img')

@app.route('/signUp', method = ['GET','POST'])
def signUp():
    global save_id
    if request.POST.get('register','').strip():
        ime_prezime = request.POST.get('ime_prezime')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        test = signUpRadnik(ime_prezime, username, password1, password2)
        if test == False:
            return template('signUp')
        else:
            id_radnika = idRadnika(user)
            save_id=id_radnika
            redirect('/')
    else:
        return template('signUp')

@app.route('/logout')
def logout():
    
    redirect('/')


@app.route('/logIn', method = ['GET','POST'])
def logIn():
    global save_id
    if request.POST.get('login','').strip():
        username = request.POST.get('username')
        global user
        user = username
        password = request.POST.get('password')
        testing = logInRadnik(username, password)
        if testing == True:
            id_radnika = idRadnika(user)
            save_id=id_radnika
            redirect('/index')
        else:
            return template('logIn')
    else:
        
        return template('logIn')


@app.route('/like<like:re:[0-9]+>')
def lajk(like):
    idd = like
    interes(idd)
    redirect('/searchGuest')


@app.route('/maca')
def mace():
    rezultat=samoMace()
    data=rezultat
    print("OVO JE REZULTAT:")
    print(data)
    return template('searchmace',data=data)

@app.route('/psi')
def psi():
    rezultat=samoPsi()
    data=rezultat
    print("OVO JE REZULTAT:")
    print(data)
    return template('searchpsi',data=data)

@app.route('/sort')
def sortiraj():
    rezultat = sortiranje()
    data = rezultat
    print(data)
    return template("sortirani", data = data)
                
                
@app.route('/')
def pocetna():
    
    return template('pocetna')


@app.route('/udomi<udomi:re:[0-9]+>',method=['GET','POST'])
def udomi(udomi):
    idd = udomi
    if request.POST.get('moze','').strip():
        ime_prezime = request.POST.get('imeU')
        email = request.POST.get('mejl')
        razlog = request.POST.get('razlog')
        id_zivotinje = idd
        ime_ziv = imeZivotinje(idd)
        prihvaceno = 0
        print('ppp')
        sacuvaj_udomitelja(ime_prezime, email, razlog, id_zivotinje, ime_ziv, prihvaceno)
        data = citajPodatkeUd()
        print(data)
        redirect('/searchGuest')
    else:
        return template('udomi', idd = idd)



@app.route('/searchGuest')
def pocetna():
    data = citajPodatke()
    print(data)
    return template('searchGuest', data = data, template_lookup=[template_path])

@app.route('/index')
def index():
    
    return template('index')

@app.route('/prijave')
def prijave():
    data = citajPodatkeUd()

    return template('prijave', data = data, template_lookup=[template_path])

@app.route('/povijest')
def prijave():
    data = citajPodatkeUd()

    return template('povijest', data = data, template_lookup=[template_path])

@app.route('/deleteU<deleteU:re:[0-9]+>')
def deleteU_deleteU(deleteU):
    con=sqlite3.connect('baza_podataka.db')
    cur=con.cursor()
    idd=deleteU
    cur.execute('DELETE FROM udomitelji WHERE id=?',(idd,))
    con.commit()
    con.close()
    redirect('/prijave')

@app.route('/prihvati<prihvati:re:[0-9]+>', method=['GET','POST'])
def prihvati(prihvati):
    idd = prihvati
    vrijeme = datetime.datetime.now().date()
    idzivotinje = idZodU(idd)
    prihvatiZ(idzivotinje, idd, vrijeme)
    redirect('/index')


@app.route('/index_guest')
def index():
    
    return template('index_guest')




run(app, host='localhost', port = 4040)



