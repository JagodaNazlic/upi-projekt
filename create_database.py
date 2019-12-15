import sqlite3 as lite
import sys

con=lite.connect('database\\animals.dat')

print ("Stvaranje baze podataka...")
with con:
    cur =con.cursor()
    #DROP TABLE
    cur.execute("DROP TABLE IF EXISTS animals")
    
    #CREATE TABLE
    cur.execute("CREATE TABLE animals (id INTEGER PRIMARY KEY AUTOINCREMENT, ime TEXT, vrsta TEXT, dob INTEGER, spol TEXT, zdr_stanje TEXT, dat_dolaska TEXT, dat_odlaska TEXT, financije REAL, zainteresiranost INTEGER)")

con.close()
print ("Baza stvorena.")
