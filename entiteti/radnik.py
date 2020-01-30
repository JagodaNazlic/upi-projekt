class Radnik():

    def __init__(idd, ime_prezime, username, sifra):
        if " " in username:
            raise ValueError("Username cannot have space")
        if len(sifra) < 5:
            raise ValueError("Password")
        if len(ime_prezime) < 2:
            raise ValueError("Name")


        Radnik._id = idd
        Radnik._ime_prezime = ime_prezime
        Radnik._username = username
        Radnik._sifra = sifra
        
        

    @property
    def id(self):
        return Radnik._id

    @property
    def ime_prezime(self):
        return Radnik._ime_prezime

    @property
    def username(self):
        return Radnik._username

    @property
    def sifra(self):
        return Radnik._sifra
    
    def __str__(self):
        return """

        id: {0}
        ime_prezime: {1}
        username: {2}
        sifra: {3}

        ---------------

        """.format(Radnik._id, Radnik._ime_prezime, Radnik._username, Radnik._sifra)
