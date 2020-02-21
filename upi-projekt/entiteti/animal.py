class Animal():

    def __init__(self, id, ime, vrsta, dob, spol, zdr_stanje, dat_dolaska, dat_odlaska, financije, interes, id_radnika, udomljen):
        self._id = id
        self._ime = ime
        self._vrsta = vrsta
        self._dob = dob
        self._spol = spol
        self._zdr_stanje = zdr_stanje
        self._dat_dolaska = dat_dolaska
        self._dat_odlaska = dat_odlaska
        self._financije = financije
        self._interes = interes
        self._id_radnika = id_radnika
        self._udomljen = udomljen
        

    @property
    def id(self):
        return self._id

    @property
    def ime(self):
        return self._ime

    @property
    def vrsta(self):
        return self._vrsta
    
    @property
    def dob(self):
        return self._dob

    @property
    def spol(self):
        return self._spol

    @property
    def zdr_stanje(self):
        return self._zdr_stanje

    @property
    def dat_dolaska(self):
        return self._dat_dolaska

    @property
    def dat_odlaska(self):
        return self._dat_odlaska

    @property
    def financije(self):
        return self._financije

    @property
    def interes(self):
        return self._interes

    @property
    def id_radnika(self):
        return self._id_radnika

    @property
    def udomljen(self):
        return self._udomljen

    
    def __str__(self):
        return """

        id: {0}
        ime: {1}
        vrsta: {2}
        dob: {3}
        spol: {4}
        zdr_stanje: {5}
        dat_dolaska: {6}
        dat_odlaska: {7}
        financije: {8}
        interes: {9}
        id_radnika: {10}
        udomljen: {11}

        ---------------

        """.format(self._id, self._ime, self._vrsta, self._dob, self._spol, self._zdr_stanje, self._dat_dolaska, self._dat_odlaska, self._financije, self._interes, self._id_radnika, self._udomljen)
