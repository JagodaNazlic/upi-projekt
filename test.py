import unittest
import os, sys, sqlite3, datetime
dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/entiteti/')
con=sqlite3.connect('baza_podataka.db')
cur=con.cursor()
from radnik import Radnik
from animal import Animal
from udomitelj import Udomitelj
from create_database import signUpRadnik, sacuvaj_zivotinju, sacuvaj_udomitelja,idZodU, azuriraj, sacuvaj_radnika


if __name__ == "__main__":
  
    dirname = os.path.dirname(sys.argv[0])
    sys.path.append(dirname.replace('\\', '/') + '/entiteti/')
    con=sqlite3.connect('baza_podataka.db')
    cur=con.cursor()
    from radnik import Radnik
    from animal import Animal
    from create_database import signUpRadnik, sacuvaj_zivotinju


class Test(unittest.TestCase):

    def test_init_username_error(self):
        with self.assertRaises(ValueError):
            Radnik("","aa bbb","")

    def test_init_imeprezime_error(self):
        with self.assertRaises(ValueError):
            Radnik("jn","","")

    def test_init_sifra_error(self):
        with self.assertRaises(ValueError):
            Radnik("","","123")

    def test_signUp(self):
        radnik = signUpRadnik("testImee","test2","1234","1234")
        username="test2"
        
        con = sqlite3.connect('baza_podataka.db')
        cur = con.cursor()
        idd=cur.execute('SELECT id FROM radnici WHERE username=(?)',(username,)).fetchone()[0]
        print("ovo je idd:")
        print(idd)

        v = cur.execute('SELECT * from radnici WHERE id = (?)',(idd,)).fetchone()
        self.assertEqual(v,(idd, 'testImee', 'test2', '1234'))

        con = sqlite3.connect('baza_podataka.db')
        cur = con.cursor()
        cur.execute('DELETE from radnici WHERE id = (?)', (idd,))
        con.commit()

    def test_nova(self):
        zivotinja = sacuvaj_zivotinju("ben","pas",4,"male", "ok", "", "02022020", 500, 0, 1, 0)
        ime = "ben"

        con = sqlite3.connect('baza_podataka.db')
        cur = con.cursor()
        idd = cur.execute('SELECT id from animals WHERE ime = (?)', (ime,)).fetchone()[0]
        print('ovo je idd:', idd)

        v = cur.execute('SELECT * from animals WHERE id = (?)',(idd,)).fetchone()
        self.assertEqual(v,(idd, "ben","pas",4,"male", "ok", "", "02022020", 500, 0, 1, 0))

    def test_udomitelj(self):
        udomitelj = sacuvaj_udomitelja("Jagoda", "jnazlic@pmfst.hr", "zelim imati ljubimca", 1, "Pancho", 0 )
        ime = 'Jagoda'

        con = sqlite3.connect('baza_podataka.db')
        cur = con.cursor()
        ud = cur.execute('SELECT id from udomitelji WHERE ime_prezime = (?)', (ime,)).fetchone()[0]
        print("ovo je idd udomitelja: ", ud )

        v = cur.execute('SELECT * from udomitelji WHERE id = (?)',(ud,)).fetchone()
        self.assertEqual(v,(ud, "Jagoda", "jnazlic@pmfst.hr", "zelim imati ljubimca", 1, "Pancho", 0))

    def test_azuriraj(self):
        update = azuriraj("Rio", "pas", "6", "male", "good", "20022020", "", 500, 0, 2, 0 ,0)
        ime = "Rio"

        con = sqlite3.connect('baza_podataka.db')
        cur = con.cursor()
        ziv = cur.execute('SELECT id from animals WHERE ime = (?)', (ime,)).fetchone()[0]
        print("ovo je idd azuriranog: ", ziv )

    def test_sacuvaj_radnika(self):
        novi = sacuvaj_radnika("Martina", "mnemet", "123456")
        idd = "Martina"

        con = sqlite3.connect('baza_podataka.db')
        cur = con.cursor()
        radnik = cur.execute('SELECT id from radnici WHERE ime_prezime = (?)', (idd,)).fetchone()[0]
        print("ovo je id novog radnika: ", radnik )

    
    def test_idZodU(self):
         
         idZ = idZodU(2)
         idd = 2
         con = sqlite3.connect('baza_podataka.db')
         cur = con.cursor()
         udomitelj = cur.execute('SELECT id from udomitelji WHERE id_zivotinje = (?)', (idd,)).fetchone()[0]
         print("ovo je id zivotinje udomitelja: ", udomitelj )

        

    

if __name__ == "__main__":
    unittest.main()
        
