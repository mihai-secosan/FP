def str2cif(a):
    """
    int -> str de 2 caractere
    :param a: int
    :return: ultimele 2 cifre ale lui a (se completeaza la stanga cu 0-uri)
    :return type: str
    """
    if a % 100 < 10:
        return '0' + str(a % 100)
    return str(a % 100)

def test_str2cif():
    assert str2cif(0) == '00'
    assert str2cif(5) == '05'
    assert str2cif(10) == '10'
    assert str2cif(52) == '52'
    assert str2cif(70) == '70'
    assert str2cif(100) == '00'
    assert str2cif(12345) == '45'


def str4cif(a):
    """
        int -> str de 4 caractere
        :param a: int
        :return: ultimele 4 cifre ale lui a (se completeaza la stanga cu 0-uri)
        :return type: str
        """
    if a % 10000 < 10:
        return '000' + str(a % 10000)
    if a % 10000 < 100:
        return '00' + str(a % 10000)
    if a % 10000 < 1000:
        return '0' + str(a % 10000)
    return str(a % 10000)

def test_str4cif():
    assert str4cif(0) == '0000'
    assert str4cif(5) == '0005'
    assert str4cif(10) == '0010'
    assert str4cif(100) == '0100'
    assert str4cif(1000) == '1000'
    assert str4cif(10000) == '0000'
    assert str4cif(123) == '0123'
    assert str4cif(123456) == '3456'
    assert str4cif(12340) == '2340'


def opus(conditie):
    """
    Returneaza opusul unei conditii
    :param conditie: {'criteriu': criteriu, 'reper': reper, 'semn': semn}
    :return: {'criteriu': criteriu, 'reper': reper, 'semn': semnOpus}
    """
    if conditie['semn'] == '<':
        semn = '>='
    elif conditie['semn'] == '<=':
        semn = '>'
    elif conditie['semn'] == '==':
        semn = '!='
    elif conditie['semn'] == '>=':
        semn = '<'
    elif conditie['semn'] == '>':
        semn = '<='
    else:
        semn = '=='
    return {'criteriu': conditie['criteriu'], 'reper': conditie['reper'], 'semn': semn}

def test_opus():
    assert opus({'criteriu': 'user', 'reper': 'meHIGH', 'semn': '<'}) == {'criteriu': 'user', 'reper': 'meHIGH', 'semn': '>='}


"""def goodOrder(leftItem, rightItem, criteriu, directie, bazaDeDate):
    
    Determina daca cele 2 iteme sunt in ordinea corespunzatoare in lista
    (functia este folosita in implementarea sortarii)
    :param leftItem:
    :param rightItem:
    :param criteriu:
    :param directie:
    :param bazaDeDate:
    :return: True / False
    
    try:
        match criteriu:
            case 'numar evenimente':
                countEv = {}
                for pers in bazaDeDate.listaPersoane:
                    countEv[pers.User] = 0
                for user in bazaDeDate.listaCorespondente:
                    countEv[user] = len(bazaDeDate.listaCorespondente[user])
                if directie == 'crescator':
                    if countEv[leftItem.User] > countEv[rightItem.User]:
                        return False
                else:
                    if countEv[leftItem.User] < countEv[rightItem.User]:
                        return False
            case 'user':
                if directie == 'crescator':
                    if leftItem.User > rightItem.User:
                        return False
                else:
                    if leftItem.User < rightItem.User:
                        return False
            case 'nume':
                if directie == 'crescator':
                    if leftItem.Nume > rightItem.Nume:
                        return False
                else:
                    if leftItem.Nume < rightItem.Nume:
                        return False
            case 'adresa':
                if directie == 'crescator':
                    if leftItem.Adresa > rightItem.Adresa:
                        return False
                else:
                    if leftItem.Adresa < rightItem.Adresa:
                        return False
            case 'numar persoane':
                countPers = {}
                for eveniment in bazaDeDate.listaEvenimente:
                    countPers[eveniment.ID] = 0
                for user in bazaDeDate.listaCorespondente:
                    for id in bazaDeDate.listaCorespondente[user]:
                        countPers[id] += 1
                if directie == 'crescator':
                    if countPers[leftItem.ID] > countPers[rightItem.ID]:
                        return False
                else:
                    if countPers[leftItem.ID] < countPers[rightItem.ID]:
                        return False
            case 'id':
                if directie == 'crescator':
                    if leftItem.ID > rightItem.ID:
                        return False
                else:
                    if leftItem.ID < rightItem.ID:
                        return False
            case 'timp':
                if directie == 'crescator':
                    if leftItem.Timp > rightItem.Timp:
                        return False
                else:
                    if leftItem.Timp < rightItem.Timp:
                        return False
            case 'descriere':
                if directie == 'crescator':
                    if leftItem.Descriere > rightItem.Descriere:
                        return False
                else:
                    if leftItem.Descriere < rightItem.Descriere:
                        return False
            case _:
                return True
    except AttributeError:
        return True
    except KeyError:
        return True
    return True"""


def cleanList(List): #recursiv
    listIsClean = True
    newList = []
    for item in List:
        if type(item) == list:
            for i in item:
                if i != '':
                    newList.append(i)
                    listIsClean = False
        elif item == '':
            listIsClean = False
        else:
            newList.append(item)
    if not listIsClean:
        newList = cleanList(newList)

    return newList
