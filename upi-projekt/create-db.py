import sqlite3 as lite
import sys

con=lite.connect('data\\baza_podataka.db')

print ("Creating database/tables...")
with con:
    cur =con.cursor()
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

        

        
con.close()
print ("Database/tables created.")
