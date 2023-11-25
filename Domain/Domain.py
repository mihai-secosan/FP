from Utils.Utils import *


class Nume:
    """
    NumeDeFamilie
    Prenume
    """
    def __init__(self, numeDeFamilie, prenume):
        self.NumeDeFamilie = numeDeFamilie
        self.Prenume = prenume
        #self.dict = {'NumeDeFamilie': numeDeFamilie, 'Prenume': prenume}

    def getNumeDeFamilie(self):
        return self.NumeDeFamilie
        #return self.dict['NumeDeFamilie']

    def getPrenume(self):
        return self.Prenume
        #return self.dict['Prenume']

    def __str__(self):
        return self.getNumeDeFamilie() + ' ' + self.getPrenume()

    def Validate(self):
        if self.getNumeDeFamilie() == '':
            print("Numele nu poate fi vid")
            raise ValueError
        if self.getNumeDeFamilie()[0] < 'A' or self.getNumeDeFamilie()[0] > 'Z':
            print("Numele trebuie sa inceapa cu litera mare")
            raise ValueError
        if self.getPrenume() == '':
            print("Prenumele nu poate fi vid")
            raise ValueError
        if self.getPrenume()[0] < 'A' or self.getPrenume()[0] > 'Z':
            print("Prenumele trebuie sa inceapa cu litera mare")
            raise ValueError

    def __lt__(self, other):
        if str(self) < str(other):
            return True
        return False

    def __le__(self, other):
        if str(self) <= str(other):
            return True
        for i in range(len(str(other))):
            if str(self)[i] != str(other)[i]:
                return False
        return True

    def __gt__(self, other):
        if str(self) > str(other):
            return True
        return False

    def __ge__(self, other):
        if str(self) >= str(other):
            return True
        for i in range(len(str(other))):
            if str(self)[i] != str(other)[i]:
                return False
        return True

    def __eq__(self, other):
        if str(self) == str(other):
            return True
        for i in range(len(str(other))):
            if str(self)[i] != str(other)[i]:
                return False
        return True

    def copy(self):
        return Nume(self.getNumeDeFamilie(), self.getPrenume())


class Adresa:
    """
    Strada
    Numar
    """
    def __init__(self, strada, numar):
        self.Strada = strada
        self.Numar = numar

    def getStrada(self):
        return self.Strada

    def getNumar(self):
        return self.Numar

    def __str__(self):
        return self.getStrada() + ' ' + str(self.getNumar())

    def Validate(self):
        try:
            self.Numar = int(self.Numar)
        except ValueError:
            print("Cum ai putut sa nu pui un numar unde iti cerea un NUMAR ???!!!")
            raise ValueError
        if self.Numar < 0:
            print("Nimeni nu locuieste la numere negative ???!!!")
            raise ValueError
        if self.Strada == '':
            print("Ai uitat de strada!")
            raise ValueError
        if self.Strada[0] < 'A' or self.Strada[0] > 'Z':
            print("Strada trebuie sa inceapa cu litera mare")
            raise ValueError

    def __lt__(self, other):
        if str(self) < str(other):
            return True
        return False

    def __le__(self, other):
        if str(self) <= str(other):
            return True
        for i in range(len(str(other))):
            if str(self)[i] != str(other)[i]:
                return False
        return True

    def __gt__(self, other):
        if str(self) > str(other):
            return True
        return False

    def __ge__(self, other):
        if str(self) >= str(other):
            return True
        for i in range(len(str(other))):
            if str(self)[i] != str(other)[i]:
                return False
        return True

    def __eq__(self, other):
        if str(self) == str(other):
            return True
        for i in range(len(str(other))):
            if str(self)[i] != str(other)[i]:
                return False
        return True

    def copy(self):
        return Adresa(self.Strada, self.Numar)


class Timp:
    """
    An
    Luna
    Zi
    Ora
    """
    def __init__(self, an, luna, zi, ora):
        self.An = an
        self.Luna = luna
        self.Zi = zi
        self.Ora = ora

    def getAn(self):
        return self.An

    def getLuna(self):
        return self.Luna

    def getZi(self):
        return self.Zi

    def getOra(self):
        return self.Ora

    def __str__(self):
        return str4cif(self.getAn()) + '/' + str2cif(self.getLuna()) + '/' + str2cif(self.getZi()) + ' ' + str2cif(self.getOra()) + ':00'

    def Validate(self):
        try:
            self.An = int(self.An)
        except ValueError:
            print("Anul introdus este invalid")
            raise ValueError
        if self.An < 2000 or self.An >= 2150:                       # 2000 <= An < 2150
            print("Anul trebuie sa fie intre 2000 si 2149")
            raise ValueError
        try:
            self.Luna = int(self.Luna)
        except ValueError:
            print("Luna introdusa este invalida")
            raise ValueError
        if self.Luna <= 0 or self.Luna > 12:                        # 0 < Luna <= 12
            print("Luna introdusa este invalida")
            raise ValueError
        try:
            self.Zi = int(self.Zi)
        except ValueError:
            print("Ziua introdusa este invalida")
            raise ValueError
        if self.Zi <= 0 or self.Zi > 31:                            # 0 < Zi <= 31
            print("Ziua introdusa este invalida")
            raise ValueError
        elif self.Luna == 2:                                        # regulile lui Februarie
            if self.An % 4 == 0 and self.Zi > 29:
                print("Ziua introdusa este invalida")
                raise ValueError
            elif self.An % 4 != 0 and self.Zi > 28:
                print("Ziua introdusa este invalida")
                raise ValueError
        elif self.Luna % 2 == 0 and self.Luna < 7 or self.Luna % 2 == 1 and self.Luna > 8 and self.Zi > 30:
            print("Ziua introdusa este invalida")                   # 0 < Zi < 30 (pt lunile potrivite)
            raise ValueError
        try:
            self.Ora = int(self.Ora)
        except ValueError:
            print("Ora introdusa este invalida")
            raise ValueError
        if self.Ora < 0 or self.Ora >= 24:
            print("Ora introdusa este invalida")
            raise ValueError

    def __lt__(self, other):
        if str(self) < str(other):
            return True
        return False

    def __le__(self, other):
        if str(self) <= str(other):
            return True
        for i in range(len(str(other))):
            if str(self)[i] != str(other)[i]:
                return False
        return True

    def __gt__(self, other):
        if str(self) > str(other):
            return True
        return False

    def __ge__(self, other):
        if str(self) >= str(other):
            return True
        for i in range(len(str(other))):
            if str(self)[i] != str(other)[i]:
                return False
        return True

    def __eq__(self, other):
        if str(self) == str(other):
            return True
        for i in range(len(str(other))):
            if str(self)[i] != str(other)[i]:
                return False
        return True

    def copy(self):
        return Timp(self.An, self.Luna, self.Zi, self.Ora)


class Persoana:
    """
    User
    Nume
    Adresa
    """
    def __init__(self, user, nume, adresa):
        self.User = user
        self.Nume = nume
        self.Adresa = adresa

    def getUser(self):
        return self.User

    def setUser(self, newUser):
        self.User = newUser

    def getNume(self):
        return str(self.Nume)

    def setNume(self, newNume):
        self.Nume = newNume

    def getNumeDeFamilie(self):
        return self.Nume.getNumeDeFamilie()

    def setNumeDeFamilie(self, newNumeDeFamilie):
        self.Nume.NumeDeFamilie = newNumeDeFamilie

    def getPrenume(self):
        return self.Nume.getPrenume()

    def setPrenume(self, newPrenume):
        self.Nume.Prenume = newPrenume

    def getAdresa(self):
        return str(self.Adresa)

    def setAdresa(self, newAdresa):
        self.Adresa = newAdresa

    def getAdresaStrada(self):
        return self.Adresa.getStrada()

    def setAdresaStrada(self, newAdresaStrada):
        self.Adresa.Strada = newAdresaStrada

    def getAdresaNumar(self):
        return self.Adresa.getNumar()

    def setAdresaNumar(self, newAdresaNumar):
        self.Adresa.Numar = newAdresaNumar

    def __str__(self):
        return 'User: <' + self.getUser() + '>    Nume: <' + self.getNume() + '>    Adresa: <' + self.getAdresa() + '>'

    def Validate(self, bazaDeDate):
        if self.User == '':
            print("User-ul introdus nu este valid")
            raise ValueError
        for user in bazaDeDate.listaPersoane:
            if user == self.User:
                print("User-ul introdus exista deja")
                raise ValueError
        self.Nume.Validate()
        self.Adresa.Validate()

    def __lt__(self, other):
        if str(self) < str(other):
            return True
        return False

    def __le__(self, other):
        if str(self) <= str(other):
            return True
        return False

    def __gt__(self, other):
        if str(self) > str(other):
            return True
        return False

    def __ge__(self, other):
        if str(self) >= str(other):
            return True
        return False

    def copy(self):
        return Persoana(self.User, self.Nume.copy(), self.Adresa.copy())

    def respecta(self, conditie):
        """
        Verifica daca persoana respecta conditia
        :param conditie: {'criteriu': criteriu, 'reper': reper, 'semn': semn}
        :return: True  daca persoana respecta conditia
                 False daca persoana NU respecta conditia
        """
        if conditie['criteriu'] == 'user':
            if conditie['semn'] == '<':
                if self.User < conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '<=':
                if self.User <= conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '==':
                if self.User == conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '>=':
                if self.User >= conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '>':
                if self.User > conditie['reper']:
                    return True
                return False
            else:
                if self.User != conditie['reper']:
                    return True
                return False
        elif conditie['criteriu'] == 'nume':
            if conditie['semn'] == '<':
                if self.Nume < conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '<=':
                if self.Nume <= conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '==':
                if self.Nume == conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '>=':
                if self.Nume >= conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '>':
                if self.Nume > conditie['reper']:
                    return True
                return False
            else:
                if self.Nume != conditie['reper']:
                    return True
                return False
        elif conditie['criteriu'] == 'adresa':
            if conditie['semn'] == '<':
                if self.Adresa < conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '<=':
                if self.Adresa <= conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '==':
                if self.Adresa == conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '>=':
                if self.Adresa >= conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '>':
                if self.Adresa > conditie['reper']:
                    return True
                return False
            else:
                if self.Adresa != conditie['reper']:
                    return True
                return False
        return True

def test_respectare_conditie_persoana():
    assert Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)).respecta(
        {'criteriu': 'user', 'reper': 'meHIGH', 'semn': '=='})
    assert Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)).respecta(
        {'criteriu': 'nume', 'reper': 'Secosan', 'semn': '=='})
    assert Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)).respecta(
        {'criteriu': 'adresa', 'reper': 'Snagov', 'semn': '=='})
    assert Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)).respecta(
        {'criteriu': 'user', 'reper': 'meHIGH', 'semn': '<'}) == False
    assert Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)).respecta(
        {'criteriu': 'nume', 'reper': 'A', 'semn': '<='}) == False
    assert Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)).respecta(
        {'criteriu': 'adresa', 'reper': 'Snagov 2', 'semn': '=='}) == False


class Eveniment:
    """
    ID
    Timp
    Descriere
    """
    def __init__(self, id, timp, descriere):
        self.ID = id
        self.Timp = timp
        self.Descriere = descriere

    def getID(self):
        return self.ID

    def setID(self, newID):
        self.ID = newID

    def getTimp(self):
        return str(self.Timp)

    def setTimp(self, newTimp):
        self.Timp = newTimp

    def getDescriere(self):
        return self.Descriere

    def setDescriere(self, newDescriere):
        self.Descriere = newDescriere

    def __str__(self):
        return 'ID: <' + str4cif(self.getID()) + '>    Data si ora: <' + self.getTimp() + '>    Descriere: <' + self.getDescriere() + '>'

    def Validate(self, bazaDeDate):
        try:
            self.ID = int(self.ID)
        except ValueError:
            print("ID-ul introdus nu este valid")
            raise ValueError
        if self.ID > 9999 or self.ID < 0:
            print("ID-ul introdus nu este valid")
            raise ValueError
        for id in bazaDeDate.listaEvenimente:
            if id == self.ID:
                print("ID-ul introdus exista deja")
                raise ValueError
        self.Timp.Validate()

    def __lt__(self, other):
        if str(self) < str(other):
            return True
        return False

    def __le__(self, other):
        if str(self) <= str(other):
            return True
        return False

    def __gt__(self, other):
        if str(self) > str(other):
            return True
        return False

    def __ge__(self, other):
        if str(self) >= str(other):
            return True
        return False

    def copy(self):
        return Eveniment(self.ID, self.Timp.copy(), self.Descriere)

    def respecta(self, conditie):
        """
        Verifica daca evenimentul respecta conditia
        :param conditie: {'criteriu': criteriu, 'reper': reper, 'semn': semn}
        :return: True  daca evenimentul respecta conditia
                 False daca evenimentul NU respecta conditia
        """
        if conditie['criteriu'] == 'id':
            if conditie['semn'] == '<':
                if self.ID < conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '<=':
                if self.ID <= conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '==':
                if self.ID == conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '>=':
                if self.ID >= conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '>':
                if self.ID > conditie['reper']:
                    return True
                return False
            else:
                if self.ID != conditie['reper']:
                    return True
                return False
        elif conditie['criteriu'] == 'timp':
            if conditie['semn'] == '<':
                if self.Timp < conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '<=':
                if self.Timp <= conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '==':
                if self.Timp == conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '>=':
                if self.Timp >= conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '>':
                if self.Timp > conditie['reper']:
                    return True
                return False
            else:
                if self.Timp != conditie['reper']:
                    return True
                return False
        elif conditie['criteriu'] == 'descriere':
            if conditie['semn'] == '<':
                if self.Descriere < conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '<=':
                if self.Descriere <= conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '==':
                if self.Descriere == conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '>=':
                if self.Descriere >= conditie['reper']:
                    return True
                return False
            elif conditie['semn'] == '>':
                if self.Descriere > conditie['reper']:
                    return True
                return False
            else:
                if self.Descriere != conditie['reper']:
                    return True
                return False
        return True

def test_respectare_conditie_eveniment():
    assert Eveniment(1, Timp(2023, 1, 1, 0), 'revelion').respecta(
        {'criteriu': 'id', 'reper': 1, 'semn': '=='})
    assert Eveniment(1, Timp(2023, 1, 1, 0), 'revelion').respecta(
        {'criteriu': 'timp', 'reper': Timp(2023, 1, 1, 0), 'semn': '=='})
    assert Eveniment(1, Timp(2023, 1, 1, 0), 'revelion').respecta(
        {'criteriu': 'descriere', 'reper': 'revelion', 'semn': '=='})
    assert Eveniment(1, Timp(2023, 1, 1, 0), 'revelion').respecta(
        {'criteriu': 'id', 'reper': 1, 'semn': '<'}) == False
    assert Eveniment(1, Timp(2023, 1, 1, 0), 'revelion').respecta(
        {'criteriu': 'timp', 'reper': Timp(2022, 12, 31, 23), 'semn': '=='}) == False
    assert Eveniment(1, Timp(2023, 1, 1, 0), 'revelion').respecta(
        {'criteriu': 'descriere', 'reper': 'zi de nastere', 'semn': '=='}) == False


class Corespondenta:
    """
    User
    ID
    """
    def __init__(self, user, id):
        self.User = user
        self.ID = id

    def getUser(self):
        return self.User

    def getID(self):
        return self.ID

    def __str__(self):
        return 'Persoana: <' + str(self.getUser()) + '>    Eveniment: <' + self.getID() + '>'

    def Validate(self, bazaDeDate):
        if self.User == '':
            print("ID-ul introdus nu este valid")
            raise ValueError
        exista = False
        for persoana in bazaDeDate.listaPersoane:
            if persoana.User == self.User:
                exista = True
        if not exista:
            print("User-ul nu exista")
            raise ValueError
        try:
            self.ID = int(self.ID)
        except ValueError:
            print("ID-ul introdus nu este valid")
            raise ValueError
        if self.ID > 9999 or self.ID < 0:
            print("ID-ul introdus nu este valid")
            raise ValueError
        exista = False
        for eveniment in bazaDeDate.listaEvenimente:
            if eveniment.ID == self.ID:
                exista = True
        if not exista:
            print("ID-ul nu exista")
            raise ValueError
        try:
            for id in bazaDeDate.listaCorespondente[self.User]:
                if self.ID == id:
                    print("User-ul deja participa la acest eveniment")
                    raise ValueError
        except KeyError:
            pass


def test_goodOrder():
    assert goodOrder(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)), Persoana('drag000s', Nume('Bucsa', 'Dragos'), Adresa('Snagov', 11)), 'adresa', 'crescator', BazaDeDate()) == True
    assert goodOrder(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)), Persoana('drag000s', Nume('Bucsa', 'Dragos'), Adresa('Snagov', 11)), 'adresa', 'descrescator', BazaDeDate()) == False


def test_to_string():
    assert str(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1))) == 'User: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>'
    assert str(Eveniment(0, Timp(2022, 12, 12, 20), 'ziua lui dragos')) == 'ID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>'


def test_gettere():
    assert Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)).getNumeDeFamilie() == 'Secosan'
    assert Eveniment(0, Timp(2022, 12, 12, 20), 'ziua lui dragos').getTimp() == '2022/12/12 20:00'
