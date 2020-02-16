import sqlite3
import os, sys

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/entiteti/')

from animal import Animal
from radnik import Radnik
from udomitelj import Udomitelj

##con = sqlite3.connect("baza_podataka.db")
##
def demoPodaci():
    con = sqlite3.connect("baza_podataka.db")

    try:
        cur = con.cursor()
        cur.executescript("""

        DROP TABLE IF EXISTS animals;

        CREATE TABLE animals (
        id INTEGER PRIMARY KEY,
        ime TEXT NOT NULL,
        vrsta TEXT,
        dob INTEGER,
        spol TEXT,
        zdr_stanje TEXT,
        dat_dolaska TEXT,
        dat_odlaska TEXT,
        financije REAL,
        interes INTEGER,
        id_radnika INTEGER,
        udomljen INTEGER);
        """)

        cur.executescript("""

        DROP TABLE IF EXISTS radnici;

        CREATE TABLE radnici (
        id INTEGER PRIMARY KEY,
        ime_prezime TEXT,
        username TEXT,
        sifra TEXT);
        """)

        cur.executescript("""

        DROP TABLE IF EXISTS udomitelji;

        CREATE TABLE udomitelji (
        id INTEGER PRIMARY KEY,
        ime_prezime TEXT,
        email TEXT,
        razlog TEXT,
        id_zivotinje INTEGER,
        ime_ziv TEXT,
        prihvaceno INTEGER);
        """)
        

        print("Uspjesno")
        cur.execute("INSERT INTO radnici (ime_prezime, username, sifra) VALUES (?,?,?)", ("Martina_Nemet", "mnemet", "123"))
        con.commit()
        cur.execute("INSERT INTO animals (ime, vrsta, dob, spol, zdr_stanje, dat_dolaska, dat_odlaska, financije, interes, id_radnika, udomljen) VALUES (?,?,?,?,?,?,?,?,?,?,?)", ("Pancho", "mačak", 3, "muški", "dobro", "12.1.2018.", "12.1.2019", 1024, 100, 1, 0))
        con.commit()
        cur.execute("INSERT INTO udomitelji (ime_prezime, email, razlog, id_zivotinje, ime_ziv) VALUES (?,?,?,?,?)", ("Martina Nemet", "mnemet@pmf", "neki", 2, "bobi"))
        con.commit()

        print("Uspješno unesen mačak")

    except Exception as e:
        print("Greška", e)
        con.rollback()

    con.close()

##Zivotinja - metode
    
def samoMace():
    con = sqlite3.connect('baza_podataka.db')   
    try:
        cur=con.cursor()
        vrsta="Cat"
        cur.execute('SELECT * FROM animals WHERE vrsta= (?)',(vrsta,)) 
        rows=cur.fetchall()
        
        
        
    except Exception as e:
        print("Error at samoMace: ",e)
        con.rollback
    con.close()
    return rows

def samoPsi():
    con = sqlite3.connect('baza_podataka.db')   
    try:
        cur=con.cursor()
        vrsta="Dog"
        cur.execute('SELECT * FROM animals WHERE vrsta= (?)',(vrsta,)) 
        rows=cur.fetchall()
        
        
        
    except Exception as e:
        print("Error at samoPsi: ",e)
        con.rollback
    con.close()
    return rows

def sortiranje():
    con = sqlite3.connect('baza_podataka.db')   
    try:
        cur=con.cursor()
        cur.execute('SELECT * FROM animals ORDER BY interes DESC') 
        rows=cur.fetchall()
        
        
        
    except Exception as e:
        print("Error at samoPsi: ",e)
        con.rollback
    con.close()
    return rows

def citajPodatke():
    
    con = sqlite3.connect("baza_podataka.db")
    try:
        cur = con.cursor()
        cur.execute("""SELECT * FROM animals """)

        podaci = cur.fetchall()


    except Exception as e:
        print("Greška kod citanja", e)
        con.rollback()

    con.close()
    return podaci


def sacuvaj_zivotinju(ime, vrsta, dob, spol, zdr_stanje, dat_dolaska, dat_odlaska, financije, interes, id_radnika, udomljen):
    
    con = sqlite3.connect("baza_podataka.db")


    try:

        cur = con.cursor()
        cur.execute("INSERT INTO animals (ime, vrsta, dob, spol, zdr_stanje, dat_dolaska, dat_odlaska, financije, interes, id_radnika, udomljen) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ime, vrsta, dob, spol, zdr_stanje, dat_dolaska, dat_odlaska, financije, interes, id_radnika, udomljen))
        if ime != ""  and vrsta != None and dob != "" and spol != None and zdr_stanje != "" and financije != "":
            
            con.commit()
        else:
            print("Niste unijeli sve podatke")

        print("Uspjesno dodana nova zivotinja")
        
    except Exception as e:
        print("Greška 1", e)
        con.rollback()
    con.close()

def dohvati_id_zivotinje(animal_id):
    con = sqlite3.connect("baza_podataka.db")
    animal = None

    try:
        cur = con.cursor()
        cur.execute("SELECT ime, vrsta, dob, spol, zdr_stanje, dat_dolaska, dat_odlaska, financije, interes, id_radnika, udomljen FROM animals WHERE id=?;", (animal_id))
        podaci = cur.fetchall()

        print("Podaci : ", podaci)
        animal = Animal(podaci[0], podaci[1], podaci[2], podaci[3], podaci[4],podacia[5], podaci[6], podaci[7], podaci[8], podaci[9], podaci[10], podaci[11])

        print("Uspjesno dohvacena zivotinja")
        
    except Exception as e:
        print("Greška", e)
        con.rollback()

    con.close()
    return animal

def azurirajZivotinju(update):
    con = sqlite3.connect('baza_podataka.db')
    try:
        cur = con.cursor()
        rows = cur.execute('SELECT * FROM animals WHERE id = (?)', (update,))
        result = cur.fetchone()

    except Exception as e:
        print("Error at azurirajZivotinju: ", e)
        con.rollback
    con.close()
    return result


def azuriraj(imeziv, vrsta, dob, spol,zdr_stanje, dat_dolaska, dat_odlaska, financije, interes, id_radnika,udomljen, update):
    con = sqlite3.connect('baza_podataka.db')
    try:
        cur = con.cursor()
        cur.execute('UPDATE animals SET ime = (?), vrsta = (?), dob=(?), spol = (?), zdr_stanje=(?), dat_dolaska = (?), dat_odlaska = (?), financije = (?), interes=(?), id_radnika =(?), udomljen = (?) WHERE id= (?)',(imeziv, vrsta, dob, spol,zdr_stanje, dat_dolaska, dat_odlaska, financije, interes, id_radnika,udomljen,update,))
        con.commit()
    
    
    except Exception as e:
        print("Error at azuriraj: ", e)
        con.rollback
    con.close()



def interes(idd):
    print(idd)
    con = sqlite3.connect("baza_podataka.db")
    try:
        cur = con.cursor()

        bla = cur.execute('SELECT * FROM animals WHERE id = (?)', (idd,))
        brojac = bla.fetchone()[9]
        cur.execute('UPDATE animals SET interes = (?) WHERE id = (?)', (brojac+1, idd,))
        con.commit()
    
    except Exception as e:
        print("Error at lajk: ", e)
        con.rollback
    con.close()   




def prihvatiZ(idd, iddU, vrijeme):
    con = sqlite3.connect("baza_podataka.db")
    try:
        cur = con.cursor()
        cur.execute('SELECT * FROM animals WHERE id = (?)', (idd,))
        cur.execute('UPDATE animals SET udomljen = (?), dat_odlaska = (?) WHERE id = (?)', (1, vrijeme, idd,))
        cur.execute('SELECT * FROM udomitelji WHERE id = (?)', (iddU,))
        cur.execute('UPDATE udomitelji SET prihvaceno = (?) WHERE id = (?)', (1, iddU,))
        con.commit()
    
    except Exception as e:
        print("Error at udomi: ", e)
        con.rollback
    con.close()
    

def imeZivotinje(idd):
    con = sqlite3.connect('baza_podataka.db')
    try:
        cur = con.cursor()
        rows = cur.execute('SELECT * FROM animals WHERE id = (?)', (idd,))
        result = cur.fetchone()

    except Exception as e:
        print("Error at imeziv: ", e)
        con.rollback
    con.close()
    return result[1]

##Radnici - metode

def idRadnika(username):
    con = sqlite3.connect('baza_podataka.db')
    try:
        cur = con.cursor()
        rows = cur.execute('SELECT * FROM radnici WHERE username = (?)', (username,))
        result = cur.fetchone()

    except Exception as e:
        print("Error at azurirajZivotinju: ", e)
        con.rollback
    con.close()
    return result[0]

def citajPodatkeLog(idRadnika):
    
    con = sqlite3.connect("baza_podataka.db")
    try:
        cur = con.cursor()
        cur.execute("""SELECT * FROM animals WHERE id_radnika = (?) """ , (idRadnika,))

        podaci = cur.fetchall()


    except Exception as e:
        print("Greška kod citanja", e)
        con.rollback()

    con.close()
    return podaci


def signUpRadnik(ime_prezime, username, password1, password2):
    con = sqlite3.connect("baza_podataka.db")
    test = False
    try:
        cur = con.cursor()
        cur.execute('SELECT username FROM radnici WHERE username= ?',(username,))
        test = cur.fetchone()
        if test == None:
            if password1 == password2:
                cur.execute('INSERT INTO radnici VALUES (null, ?,?,?)', (ime_prezime, username, password1))
                con.commit()
                test = True
                print("You have created an account")
            else:
                test = False
                print("Wrong password")
        else:
            testing=False
            print("Username already exists!")
    except Exception as e:
        print("Error at signUpUser: ",e)
        con.rollback
        
    con.close()
    return test


def logInRadnik(username, password):
    con = sqlite3.connect("baza_podataka.db")
    testing = False
    try:
        cur=con.cursor()
        id1 = cur.execute('SELECT * FROM radnici WHERE username = (?) AND sifra = (?)', (username, password,))
        id1 = cur.fetchone()
        if id1 != None:
            print("Correct username and password")
            testing = True
        else:
            print("Wrong password or username")
            testing = False
    except Exception as e:
        print("Error at logInUser: ",e)
        con.rollback
    con.close()
    return testing
    
    
def sacuvaj_radnika(ime_prezime, username, sifra):
    con = sqlite3.connect("baza_podataka.db")

    try:

        cur = con.cursor()
        cur.execute("INSERT INTO radnici (ime_prezime, username, sifra) VALUES (?, ?, ?)", (ime_prezime, username, sifra))
        con.commit()

        print("Uspjesno dodan novi radnik")
        
    except Exception as e:
        print("Greška", e)
        con.rollback()

    con.close()


   

##Udomitelji- metode
    
def sacuvaj_udomitelja(ime_prezime, email, razlog, id_zivotinje, ime_ziv, prihvaceno):
    con = sqlite3.connect("baza_podataka.db")

    try:

        cur = con.cursor()
        cur.execute("INSERT INTO udomitelji (ime_prezime, email, razlog, id_zivotinje, ime_ziv, prihvaceno) VALUES (?, ?, ?, ?, ?, ?)", (ime_prezime, email, razlog, id_zivotinje, ime_ziv, prihvaceno))
        con.commit()

        print("Uspjesno dodan udomitelj")
        
    except Exception as e:
        print("Greška kod sacuvaj_udomitelja", e)
        con.rollback()

    con.close()



def citajPodatkeUd():
    
    con = sqlite3.connect("baza_podataka.db")
    try:
        cur = con.cursor()
        cur.execute("""SELECT * FROM udomitelji """)

        podaci = cur.fetchall()
        
    except Exception as e:
        print("Greška kod citanja", e)
        con.rollback()

    con.close()
    return podaci



def idZodU(idd):
    con = sqlite3.connect('baza_podataka.db')
    try:
        cur = con.cursor()
        rows = cur.execute('SELECT * FROM udomitelji WHERE id = (?)', (idd,))
        result = cur.fetchone()

    except Exception as e:
        print("Error at id: ", e)
        con.rollback
    con.close()
    return result[4]





    
