import sqlite3
import os, sys

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/entiteti/')

from animal import Animal

def demoPodaci():
    con=sqlite3.connect('baza_podataka.db')
    try:
        cur = con.cursor()
        cur.executescript("""

        DROP TABLE IF EXISTS animals;

        CREATE TABLE animals (
        id INTEGER PRIMARY KEY,
        ime TEXT,
        vrsta TEXT,
        dob INTEGER,
        spol TEXT
        zdr_stanje TEXT,
        dat_dolaska TEXT,
        dat_odlaska TEXT,
        financije REAL,
        interes INTEGER);
        """)
        

        print("Uspjesno")

        cur.execute("INSERT INTO animals (ime, vrsta, dob, spol, zdr_stanje, dat_dolaska, dat_odlaska, financije, intres) VALUES (?,?,?,?,?,?,?,?)", ("Pancho", "mačak", 3, "muški", "dobro", "12.1.2018.", "12.1.2019", 1024, 100))
        con.commit()

        print("Uspješno unesen mačak")

    except Exception as e:
        print("Greška", e)
        con.rollback()

    con.close()


def citajPodatke():
    con = sqlite3.connect('baza_podataka.db')
    lista_zivotinja = []

    try:
        cur = con.cursor()
        cur.execute("""SELECT id, ime, vrsta, dob, spol, zdr_stanje, dat_dolaska, dat_odlaska, financije, interes FROM animals """)

        podaci = cur.fetchall()

        for a in podaci:

            an = Animal(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9])
            lista_zivotinja.append(a)
        print("Uspjesno dohvaceni podaci")

        for a in lista_zivotinja:
            print(a)

    except Exception as e:
        print("Greška", e)
        con.rollback()

    con.close()
    return lista_zivotinja

def sacuvaj_zivotinju(ime, vrsta, dob, spol, zdr_stanje, dat_dolaska, dat_odlaska, financije, interes):
    con = sqlite3.connect("baza_podataka.db")

    try:

        cur = con.cursor()
        cur.execute("INSERT INTO animals (ime, vrsta, dob, spol, zdr_stanje, dat_dolaska, dat_odlaska, financije, interes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (ime, vrsta, dob, spol, zdr_stanje, dat_dolaska, dat_odlaska, financije, interes))
        con.commit()

        print("Uspjesno dodana nova zivotinja")
        
    except Exception as e:
        print("Greška", e)
        con.rollback()

    con.close()


def izbrisi_zivotinju(animal_id):
    con = sqlite3.connect("baza_podataka.db")

    try:
        cur = con.cursor()
        cur.execute("DELETE FROM animals WHERE id=?;", (animal_id))
        con.commit()

        print("Uspjesno izbrisana zivotinja iz baze")

    except Exception as e:
        print("Greška", e)
        con.rollback()

    con.close()

def dohvati_id_zivotinje(animal_id):
    con = sqlite3.connect("baza_podataka.db")
    animal = None

    try:
        cur = con.cursor()
        cur.execute("SELECT ime, vrsta, dob, spol, zdr_stanje, dat_dolaska, dat_odlaska, financije, interes FROM animals WHERE id=?;", (animal_id))
        podaci = cur.fetchall()

        print("Podaci : ", podaci)
        animal = Animal(podaci[0], podaci[1], podaci[2], podaci[3], podaci[4],podacia[5], podaci[6], podaci[7], podaci[8], podaci[9])

        print("Uspjesno dohvacena zivotinja")
        
    except Exception as e:
        print("Greška", e)
        con.rollback()

    con.close()
    return animal

def azuriraj_zivotinju(animal_id, ime, vrsta, dob, spol, zdr_stanje, dat_dolaska, dat_odlaska, financije, interes):
    con = sqlite3.connect("baza_podataka.db")

    try:
        cur = con.cursor()
        cur.execute("UPDATE animals SET ime = ?, vrsta = ?, dob = ?, spol = ?, zdr_stanje = ?, dat_dolaska = ?, dat_odlaska = ?, financije = ?, interes = ? WHERE id = ?", (ime, vrsta, dob, spol, zdr_stanje, dat_dolaska, dat_odlaska, financije, interes, animal_id))
        con.commit()

        print("Uspjesno azurirana zivotinja")

    except Exception as e:
        print("Greška", e)
        con.rollback()

    con.close()























    
