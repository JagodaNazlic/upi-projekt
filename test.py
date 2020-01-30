import unittest
import os, sys, sqlite3, datetime

from create_database import citajPodatke, citajPodatkeLog, dohvati_id_ziv, citajRadnika, signUpRadnik, logInRadnik, sacuvaj_zivotinju, sacuvaj_radnika, dohvati_id_zivotinje, dohvati_id_radnika, azurirajZivotinju, azuriraj, interes
dirname = os.path.dirname(sys.argv[0])
from radnik import Radnik

class TestStringMethods(unittest.TestCase):

    def test_init_value_error_password(self):
        with self.assertRaises(ValueError):
            Radnik("","","123")

    def test_init_username_error(self):
        with self.assertRaises(ValueError):
            Radnik("m", "","")

    def test_init_name_error(self):
        with self.assertRaises(ValueError):
            Radnik("","m nemet", "")

    
        
        

unittest.main()
