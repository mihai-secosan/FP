import random
import string
from Domain.Domain import *


def generatePerson(bazaDeDate):
    """

    :param bazaDeDate:
    :return: o persoana cu date la intamplare
    """
    user = ''
    numeDeFamilie = ''
    prenume = ''
    strada = ''
    numar = 0
    x = ''

    user = user.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k = random.randint(3, 10)))

    #for persoana in bazaDeDate.listaPersoane:
        #if persoana.getUser() == user:
            #return generatePerson(bazaDeDate)

    x = x.join(random.choices(string.ascii_uppercase))
    numeDeFamilie += x
    x = ''
    x = x.join(random.choices(string.ascii_lowercase, k = random.randint(3, 10)))
    numeDeFamilie += x
    x = ''
    x = x.join(random.choices(string.ascii_uppercase))
    prenume += x
    x = ''
    prenume += x
    x = ''
    x = x.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
    prenume += x
    x = ''
    x = x.join(random.choices(string.ascii_uppercase))
    strada += x
    x = ''
    x = x.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
    strada += x
    x = ''
    numar = random.randint(1, 99)

    return Persoana(user, Nume(numeDeFamilie, prenume), Adresa(strada, numar))

def generateEvent(bazaDeDate):
    """

    :param bazaDeDate:
    :return: un eveniment cu date la intamplare
    """
    id = 0
    an = 0
    luna = 0
    zi = 0
    ora = 0
    descriere = ''

    id = random.randint(0, 9999)

    #for eveniment in bazaDeDate.listaEvenimente:
        #if eveniment.getID() == id:
            #return generateEvent(bazaDeDate)

    an = random.randint(2000, 2149)
    luna = random.randint(1, 12)
    zi = random.randint(1, 31)
    ora = random.randint(0, 23)
    descriere = descriere.join(random.choices(string.ascii_lowercase, k = random.randint(1, 20)))

    timp = Timp(an, luna, zi, ora)
    try:
        timp.Validate()
        return Eveniment(id, timp, descriere)
    except ValueError:
        return generateEvent(bazaDeDate)
