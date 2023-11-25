from Domain.Domain import *


class BazaDeDate:
    """
    listaPersoane
    listaEvenimente
    listaCorespondente
    """
    def __init__(self):
        self.listaPersoane = []
        self.listaEvenimente = []
        self.listaCorespondente = {}
        #comp = self.goodOrder
        self.DefaultSortingAlgorithm = self.bubble_sort

    def copiaza(self, altaBazaDeDate):
        self.listaPersoane = altaBazaDeDate.listaPersoane
        self.listaEvenimente = altaBazaDeDate.listaEvenimente
        self.listaCorespondente = altaBazaDeDate.listaCorespondente

    def __str__(self):
        Legit = True

        if Legit:
            string = '\nLista de persoane:'
            for persoana in self.listaPersoane:
                string += '\n' + str(persoana)
            string += '\n\nLista de evenimente:'
            for eveniment in self.listaEvenimente:
                string += '\n' + str(eveniment)
            string += '\n\nLista de inscrieri:'
            for user in self.listaCorespondente.keys():
                string += '\n' + user + ': <'
                string += str4cif(self.listaCorespondente[user][0])
                for i in range(1, len(self.listaCorespondente[user])):
                    string += '>; <' + str4cif(self.listaCorespondente[user][i])
                string += '>'
            return string
        else:
            string = '\\nLista de persoane:'
            for persoana in self.listaPersoane:
                string += '\\n' + str(persoana)
            string += '\\n\\nLista de evenimente:'
            for eveniment in self.listaEvenimente:
                string += '\\n' + str(eveniment)
            string += '\\n\\nLista de inscrieri:'
            for user in self.listaCorespondente.keys():
                string += '\\n' + user + ': <'
                string += str4cif(self.listaCorespondente[user][0])
                for i in range(1, len(self.listaCorespondente[user])):
                    string += '>; <' + str4cif(self.listaCorespondente[user][i])
                string += '>'
            return string

    def __eq__(self, other):
        if str(self) == str(other):
            return True
        return False

    def select(self, conditie):
        copie = BazaDeDate()
        for i in range(len(self.listaPersoane)):
            if self.listaPersoane[i].respecta(conditie):
                copie.listaPersoane.append(self.listaPersoane[i].copy())
        for i in range(len(self.listaEvenimente)):
            if self.listaEvenimente[i].respecta(conditie):
                copie.listaEvenimente.append(self.listaEvenimente[i].copy())
        for user in self.listaCorespondente.keys():
            userulExista = False
            for i in range(len(copie.listaPersoane)):
                if user == copie.listaPersoane[i].User:
                    userulExista = True
                    break

            if userulExista:
                existaMinimUnID = False
                for eveniment in self.listaCorespondente[user]:
                    for i in range(len(copie.listaEvenimente)):
                        if eveniment == copie.listaEvenimente[i].ID:
                            existaMinimUnID = True
                            break
                    if existaMinimUnID:
                        break
                if existaMinimUnID:
                    copie.listaCorespondente[user] = []
                    for eveniment in self.listaCorespondente[user]:
                        idulExista = False
                        for i in range(len(copie.listaEvenimente)):
                            if eveniment == copie.listaEvenimente[i].ID:
                                idulExista = True
                                break
                        if idulExista:
                            copie.listaCorespondente[user].append(eveniment)

        return copie


    def goodOrder(self, bazaDeDate, leftItem, rightItem, criteriu, directie):
        x = lambda l, r : True
        try:
            match criteriu:
                case 'numar evenimente':
                    countEv = {}
                    for pers in self.listaPersoane:
                        countEv[pers.User] = 0
                    for user in self.listaCorespondente:
                        countEv[user] = len(self.listaCorespondente[user])
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
                    for eveniment in self.listaEvenimente:
                        countPers[eveniment.ID] = 0
                    for user in self.listaCorespondente:
                        for id in self.listaCorespondente[user]:
                            countPers[id] += 1
                    if directie == 'crescator':
                        if countPers[leftItem.ID] > countPers[rightItem.ID]:
                            return False
                    else:
                        if countPers[leftItem.ID] < countPers[rightItem.ID]:
                            return False
                case 'id':
                    if directie == 'crescator':
                        x = lambda l, r: l.ID > r.ID
                        #if leftItem.ID > rightItem.ID:
                            #return False
                    else:
                        if leftItem.ID < rightItem.ID:
                            return False
                case 'timp':
                    if directie == 'crescator':
                        x = lambda l, r : l.Timp < r.Timp
                        #if leftItem.Timp > rightItem.Timp:
                            #return False
                    else:
                        x = lambda l, r: l.Timp > r.Timp
                        #if leftItem.Timp < rightItem.Timp:
                            #return False
                case 'descriere':
                    if directie == 'crescator':
                        x = lambda l, r: l.Descriere > r.Descriere
                        #if leftItem.Descriere > rightItem.Descriere:
                            #return False
                    else:
                        x = lambda l, r: l.Descriere < r.Descriere
                        #if leftItem.Descriere < rightItem.Descriere:
                            #return False
                case _:
                    return True
        except AttributeError:
            return True
        except KeyError:
            return True
        except ValueError:
            return x(leftItem, rightItem)
        return x(leftItem, rightItem)


    def bubble_sort(self, criteriu, directie, criteriuSecundar = 'nume', directieSecundara = 'crescator', comparator = goodOrder):
        """
        Calculul complexitatii:

        Caz favorabil   : lista e sortata -> (n)
        Caz defavorabil : lista e sortata in directia gresita -> (n^2)
        Caz mediu       : (n^2)

        Complexitatea generala  : O(n^2)
        Complexitatea ca spatiu aditional de memorie    : (1)
            (este un algoritm de sortare in-place)

        """
        comparator = self.goodOrder

        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(self.listaPersoane) - 1):
                if not comparator(self, self.listaPersoane[i], self.listaPersoane[i + 1], 'user', 'crescator'):
                    aux = self.listaPersoane[i]
                    self.listaPersoane[i] = self.listaPersoane[i + 1]
                    self.listaPersoane[i + 1] = aux
                    is_sorted = False

        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(self.listaEvenimente) - 1):
                if not comparator(self, self.listaEvenimente[i], self.listaEvenimente[i + 1], 'id', 'crescator'):
                    aux = self.listaEvenimente[i]
                    self.listaEvenimente[i] = self.listaEvenimente[i + 1]
                    self.listaEvenimente[i + 1] = aux
                    is_sorted = False

        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(self.listaPersoane) - 1):
                if not comparator(self, self.listaPersoane[i], self.listaPersoane[i + 1], criteriuSecundar, directieSecundara):
                    aux = self.listaPersoane[i]
                    self.listaPersoane[i] = self.listaPersoane[i + 1]
                    self.listaPersoane[i + 1] = aux
                    is_sorted = False

        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(self.listaEvenimente) - 1):
                if not comparator(self, self.listaEvenimente[i], self.listaEvenimente[i + 1], criteriuSecundar, criteriuSecundar):
                    aux = self.listaEvenimente[i]
                    self.listaEvenimente[i] = self.listaEvenimente[i + 1]
                    self.listaEvenimente[i + 1] = aux
                    is_sorted = False

        if criteriu == 'numar evenimente' or criteriu == 'user' or criteriu == 'nume' or criteriu == 'adresa':
            is_sorted = False
            while not is_sorted:
                is_sorted = True
                for i in range(len(self.listaPersoane) - 1):
                    if not comparator(self, self.listaPersoane[i], self.listaPersoane[i + 1], criteriu, directie):
                        aux = self.listaPersoane[i]
                        self.listaPersoane[i] = self.listaPersoane[i + 1]
                        self.listaPersoane[i + 1] = aux
                        is_sorted = False
        else:
            is_sorted = False
            while not is_sorted:
                is_sorted = True
                for i in range(len(self.listaEvenimente) - 1):
                    if not comparator(self, self.listaEvenimente[i], self.listaEvenimente[i + 1], criteriu, directie):
                        aux = self.listaEvenimente[i]
                        self.listaEvenimente[i] = self.listaEvenimente[i + 1]
                        self.listaEvenimente[i + 1] = aux
                        is_sorted = False

        personIndex = {}
        for i in range(len(self.listaPersoane)):
            personIndex[self.listaPersoane[i].getUser()] = i

        eventIndex = {}
        for i in range(len(self.listaEvenimente)):
            eventIndex[self.listaEvenimente[i].getID()] = i

        listaSortataDeCorespondente = {}

        listaUseriActivi = []
        for user in self.listaCorespondente:
            listaUseriActivi.append(user)
        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(listaUseriActivi) - 1):
                if personIndex[listaUseriActivi[i]] > personIndex[listaUseriActivi[i + 1]]:
                    aux = listaUseriActivi[i]
                    listaUseriActivi[i] = listaUseriActivi[i + 1]
                    listaUseriActivi[i + 1] = aux
                    sorted = False
        for user in listaUseriActivi:
            listaSortataDeCorespondente[user] = self.listaCorespondente[user]

        self.listaCorespondente = listaSortataDeCorespondente

        for user in self.listaCorespondente:
            sorted = False
            while not sorted:
                sorted = True
                for i in range(len(self.listaCorespondente[user]) - 1):
                    if eventIndex[self.listaCorespondente[user][i]] > eventIndex[self.listaCorespondente[user][i + 1]]:
                        aux = self.listaCorespondente[user][i]
                        self.listaCorespondente[user][i] = self.listaCorespondente[user][i + 1]
                        self.listaCorespondente[user][i + 1] = aux
                        sorted = False


    def shell_sort(self, criteriu, directie, criteriuSecundar = 'nume', directieSecundara = 'crescator', comparator = goodOrder):
        """
        Calculul complexitatii:

        len(gaps) * (len(list) - len(gaps)) *
        """
        gaps = [701, 301, 132, 57, 23, 10, 4, 1]

        for gap in gaps:
            for i in range(gap, len(self.listaPersoane)):
                temp = self.listaPersoane[i]
                j = i
                while j >= gap and comparator(self, temp, self.listaPersoane[j - gap], 'user', 'crescator'):
                    self.listaPersoane[j] = self.listaPersoane[j - gap]
                    j -= gap
                self.listaPersoane[j] = temp

        for gap in gaps:
            for i in range(gap, len(self.listaEvenimente)):
                temp = self.listaEvenimente[i]
                j = i
                while j >= gap and comparator(self, temp, self.listaEvenimente[j - gap], 'id', 'crescator'):
                    self.listaEvenimente[j] = self.listaEvenimente[j - gap]
                    j -= gap
                self.listaEvenimente[j] = temp

        for gap in gaps:
            for i in range(gap, len(self.listaPersoane)):
                temp = self.listaPersoane[i]
                j = i
                while j >= gap and comparator(self, temp, self.listaPersoane[j - gap], criteriuSecundar, directieSecundara):
                    self.listaPersoane[j] = self.listaPersoane[j - gap]
                    j -= gap
                self.listaPersoane[j] = temp

        for gap in gaps:
            for i in range(gap, len(self.listaEvenimente)):
                temp = self.listaEvenimente[i]
                j = i
                while j >= gap and comparator(self, temp, self.listaEvenimente[j - gap], criteriuSecundar, directieSecundara):
                    self.listaEvenimente[j] = self.listaEvenimente[j - gap]
                    j -= gap
                self.listaEvenimente[j] = temp

        if criteriu == 'numar evenimente' or criteriu == 'user' or criteriu == 'nume' or criteriu == 'adresa':
            for gap in gaps:
                for i in range(gap, len(self.listaPersoane)):
                    temp = self.listaPersoane[i]
                    j = i
                    while j >= gap and comparator(self, temp, self.listaPersoane[j - gap], criteriu, directie):
                        self.listaPersoane[j] = self.listaPersoane[j - gap]
                        j -= gap
                    self.listaPersoane[j] = temp
        else:
            for gap in gaps:
                for i in range(gap, len(self.listaEvenimente)):
                    temp = self.listaEvenimente[i]
                    j = i
                    while j >= gap and comparator(self, temp, self.listaEvenimente[j - gap], criteriu, directie):
                        self.listaEvenimente[j] = self.listaEvenimente[j - gap]
                        j -= gap
                    self.listaEvenimente[j] = temp

        personIndex = {}
        for i in range(len(self.listaPersoane)):
            personIndex[self.listaPersoane[i].getUser()] = i

        eventIndex = {}
        for i in range(len(self.listaEvenimente)):
            eventIndex[self.listaEvenimente[i].getID()] = i

        listaSortataDeCorespondente = {}
        listaUseriActivi = []

        for user in self.listaCorespondente:
            listaUseriActivi.append(user)

        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(listaUseriActivi) - 1):
                if personIndex[listaUseriActivi[i]] > personIndex[listaUseriActivi[i + 1]]:
                    aux = listaUseriActivi[i]
                    listaUseriActivi[i] = listaUseriActivi[i + 1]
                    listaUseriActivi[i + 1] = aux
                    is_sorted = False
        for user in listaUseriActivi:
            listaSortataDeCorespondente[user] = self.listaCorespondente[user]

        self.listaCorespondente = listaSortataDeCorespondente

        for user in self.listaCorespondente:
            is_sorted = False
            while not is_sorted:
                is_sorted = True
                for i in range(len(self.listaCorespondente[user]) - 1):
                    if eventIndex[self.listaCorespondente[user][i]] > eventIndex[self.listaCorespondente[user][i + 1]]:
                        aux = self.listaCorespondente[user][i]
                        self.listaCorespondente[user][i] = self.listaCorespondente[user][i + 1]
                        self.listaCorespondente[user][i + 1] = aux
                        is_sorted = False


    def modifyPerson(self, pers1Index, pers2):
        if str(pers2.User) != '':
            self.listaPersoane[pers1Index].User = pers2.User
        if str(pers2.Nume) != '':
            self.listaPersoane[pers1Index].Nume = pers2.Nume
        if str(pers2.Adresa) != '':
            self.listaPersoane[pers1Index].Adresa = pers2.Adresa
        #self.listaPersoane[pers1Index] = pers2


    def modifyEvent(self, event1Index, event2):
        if str(event2.ID) != '':
            self.listaEvenimente[event1Index].ID = event2.ID
        if str(event2.Timp) != '':
            self.listaEvenimente[event1Index].Timp = event2.Timp
        if str(event2.Descriere) != '':
            self.listaEvenimente[event1Index].Descriere = event2.Descriere
        #self.listaEvenimente[event1Index] = event2


    def addPerson(self, person):
        self.listaPersoane.append(person)


    def addEvent(self, event):
        self.listaEvenimente.append(event)


def test_to_string_repo():
    assert str(BazaDeDate()) == '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:'
