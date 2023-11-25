from Repository.BackupManager import *
from Repository.Repository import *
from randomGenerator.randomGenerator import *

class Controller:
    def __init__(self, bazaDeDate):
        self.BazaDeDate = bazaDeDate

    def f1(self, persoana):
        try:
            #persoana = citestePersoana()
            persoana.Validate(self.BazaDeDate)
            self.BazaDeDate.listaPersoane.append(persoana)
        except ValueError:
            pass


    def f2(self, eveniment):
        try:
            #eveniment = citesteEveniment()
            eveniment.Validate(self.BazaDeDate)
            self.BazaDeDate.listaEvenimente.append(eveniment)
        except ValueError:
            pass


    def f3(self, corespondenta):
        try:
            #corespondenta = citesteCorespondenta()
            corespondenta.Validate(self.BazaDeDate)
            try:
                self.BazaDeDate.listaCorespondente[corespondenta.User].append(corespondenta.ID)
            except KeyError:
                self.BazaDeDate.listaCorespondente[corespondenta.User] = [corespondenta.ID]
        except ValueError:
            pass


    def f4(self, criteriu):             # It 2
        try:
            #criteriu = opus(citesteCriteriuPersoana())
            bazaDeDateNoua = BazaDeDate()
            bazaDeDateNoua.copiaza(self.BazaDeDate.select(criteriu))
            self.BazaDeDate.copiaza(bazaDeDateNoua)
        except ValueError:
            pass


    def f5(self, criteriu):             # It 2
        try:
            #criteriu = opus(citesteCriteriuEveniment())
            bazaDeDateNoua = BazaDeDate()
            bazaDeDateNoua.copiaza(self.BazaDeDate.select(criteriu))
            self.BazaDeDate.copiaza(bazaDeDateNoua)
        except ValueError:
            pass


    def f6(self, pers, newPersoana):             # It 2
        try:
            #pers = input("Userul persoanei careia i se schimba datele: ")
            userChanged = False
            if pers != newPersoana.User and newPersoana.User != '':
                userChanged = True
            for persoanaIndex in range(len(self.BazaDeDate.listaPersoane)):
                if self.BazaDeDate.listaPersoane[persoanaIndex].getUser() == pers:
                    #bazaDeDate.listaPersoane[persoanaIndex] = newPersoana
                    self.BazaDeDate.modifyPerson(persoanaIndex, newPersoana)
                    #persoanaSchimbata = newPersoana
                    break
            if userChanged:
                self.BazaDeDate.listaCorespondente[newPersoana.getUser()] = self.BazaDeDate.listaCorespondente[pers]
                self.BazaDeDate.listaCorespondente.pop(pers)
        except ValueError:
            pass
        except KeyError:
            pass


    def f7(self, idEv, newEveniment):             # It 2
        try:
            #idEv = int(input("ID-ul evenimentului careia i se schimba datele: "))
            idChanged = False
            if idEv != newEveniment.ID and newEveniment.ID != '':
                idChanged = True
            for evenimentIndex in range(len(self.BazaDeDate.listaEvenimente)):
                if self.BazaDeDate.listaEvenimente[evenimentIndex].getID() == idEv:
                    self.BazaDeDate.modifyEvent(evenimentIndex, newEveniment)
                    #evenimentSchimbat = newEveniment
                    break
            if idChanged:
                for user in self.BazaDeDate.listaCorespondente:
                    for i in range(len(self.BazaDeDate.listaCorespondente[user])):
                        if self.BazaDeDate.listaCorespondente[user][i] == idEv:
                            self.BazaDeDate.listaCorespondente[user][i] = newEveniment.getID()
        except ValueError:
            pass
        except KeyError:
            pass


    def f8(self, criteriu):
        try:
            #criteriu = citesteCriteriuPersoana()
            return str(self.BazaDeDate.select(criteriu))
        except ValueError:
            raise ValueError


    def f9(self, criteriu):
        try:
            #criteriu = citesteCriteriuEveniment()
            return str(self.BazaDeDate.select(criteriu))
        except ValueError:
            raise ValueError


    def f10(self, x):             # It 3
        try:
            #x = citesteCriteriuOrdonarePersoane()
            self.BazaDeDate.DefaultSortingAlgorithm(x[0], x[1])
            print(str(self.BazaDeDate))
            with open("Raport.txt", "w") as f:
                f.write(str(self.BazaDeDate))
        except ValueError:
            pass


    def f11(self, x):             # It 3
        try:
            #x = citesteCriteriuOrdonareEvenimente()
            self.BazaDeDate.DefaultSortingAlgorithm(x[0], x[1])
            print(str(self.BazaDeDate))
            with open("Raport.txt", "w") as f:
                f.write(str(self.BazaDeDate))
        except ValueError:
            pass


    def f12(self):             # It 3
        self.BazaDeDate.DefaultSortingAlgorithm('numar persoane', 'descrescator')
        countPers = {}
        for eveniment in self.BazaDeDate.listaEvenimente:
            countPers[eveniment.ID] = 0
        for user in self.BazaDeDate.listaCorespondente:
            for id in self.BazaDeDate.listaCorespondente[user]:
                countPers[id] += 1
        print("Primele 20% de evenimente ca numar de participanti")
        for i in range(int((len(self.BazaDeDate.listaEvenimente) - 1) / 5 + 1)):
            print(str(countPers[self.BazaDeDate.listaEvenimente[i].ID]) + ' persoane    ' + str(self.BazaDeDate.listaEvenimente[i]))


    def f13(self):             # It 3
        self.BazaDeDate.DefaultSortingAlgorithm('numar evenimente', 'descrescator')
        countEv = {}
        for persoana in self.BazaDeDate.listaPersoane:
            countEv[persoana.User] = 0
        for user in self.BazaDeDate.listaCorespondente:
            countEv[user] += len(self.BazaDeDate.listaCorespondente[user])
        print("Primele 20% de persoane ca numar de evenimente la care participa")
        for i in range(int((len(self.BazaDeDate.listaPersoane) - 1) / 5 + 1)):
            print(str(countEv[self.BazaDeDate.listaPersoane[i].User]) + ' evenimente    ' + str(self.BazaDeDate.listaPersoane[i]))


    def f14(self, nrPers, nrEvent):
        for i in range(nrPers):
            self.BazaDeDate.addPerson(generatePerson(self.BazaDeDate))

        for i in range(nrEvent):
            self.BazaDeDate.addEvent(generateEvent(self.BazaDeDate))


    def f15(self, fileName):
        BackupManager(fileName, self.BazaDeDate).backup()


    def f16(self, fileName):
        self.BazaDeDate = BackupManager(fileName, self.BazaDeDate).revertFromBackup()
