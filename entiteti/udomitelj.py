class Udomitelj():

    def __init__(self, id, ime_prezime, email, razlog, id_zivotinje, ime_ziv, prihvaceno):
        self._id = id
        self._ime_prezime = ime_prezime
        self._email = email
        self._razlog = razlog
        self._id_zivotinje = id_zivotinje
        self._ime_ziv = ime_ziv
        self._prihvaceno = prihvaceno
        
        

    @property
    def id(self):
        return self._id

    @property
    def ime_prezime(self):
        return self._ime_prezime

    @property
    def email(self):
        return self._email

    @property
    def razlog(self):
        return self._razlog
    
    @property
    def id_zivotinje(self):
        return self._id_zivotinje

    @property
    def ime_ziv(self):
        return self._ime_ziv

    @property
    def prihvaceno(self):
        return self._prihvaceno

    
    def __str__(self):
        return """

        id: {0}
        ime_prezime: {1}
        email: {2}
        razlog: {3}
        id_zivotinje: {4}
        ime_ziv: {5}
        prihvaceno: {6}

        ---------------

        """.format(self._id, self._ime_prezime, self._email, self._razlog, self._id_zivotinje, self._ime_ziv, self._prihvaceno)
