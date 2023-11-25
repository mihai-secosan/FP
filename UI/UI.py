from Controller.Controller import *


class UI:
    def __init__(self, controller):
        self.Controller = controller

    def print_menu(self):
        print("\n1. Inregistreaza persoana")
        print("2. Inregistreaza eveniment")
        print("3. Inscrie persoana la eveniment")
        print("4. Sterge persoane din lista")
        print("5. Sterge evenimente din lista")
        print("6. Modifica datele unor persoane")
        print("7. Modifica datele unui eveniment")
        print("8. Cautare persoane")
        print("9. Cautare evenimente")
        print("10. Ordonarea listei de persoane")
        print("11. Ordonarea listei de evenimente")
        print("12. Selectare evenimente populare")
        print("13. Selectare persoane dedicate")
        print("14. Adauga date randomizate in baza de date")
        print("15. Backup")
        print("16. Revert from backup")


    """def run_menu(self):
        while True:
            opt = input("Optiunea dvs: ")
            if self.lucreazaCu(opt) == 'invalid':
                if opt == 'exit':
                    break
                else:
                    print("Optiune invalida!")
                    continue
            self.print_menu()"""


    def run_menu(self): #recursiv
        opt = input("Optiunea dvs: ")
        if self.lucreazaCu(opt) == 'invalid' and opt != 'exit':
            print("Optiune invalida!")
        else:
            self.print_menu()
        if opt != 'exit':
            self.run_menu()


    def lucreazaCu(self, opt):
        s = 'valid'
        if opt == '1':
            try:
                self.Controller.f1(self.citestePersoana())
            except ValueError:
                pass
        elif opt == '2':
            try:
                self.Controller.f2(self.citesteEveniment())
            except ValueError:
                pass
        elif opt == '3':
            try:
                self.Controller.f3(self.citesteCorespondenta())
            except ValueError:
                pass
        elif opt == '4':
            try:
                self.Controller.f4(opus(self.citesteCriteriuPersoana()))
            except ValueError:
                pass
        elif opt == '5':
            try:
                self.Controller.f5(opus(self.citesteCriteriuEveniment()))
            except ValueError:
                pass
        elif opt == '6':
            try:
                self.Controller.f6(input("Userul persoanei careia i se schimba datele: "), self.schimbaDatePersoana())
            except ValueError:
                pass
        elif opt == '7':
            try:
                self.Controller.f7(int(input("ID-ul evenimentului careia i se schimba datele: ")), self.schimbaDateEveniment())
            except ValueError:
                pass
        elif opt == '8':
            try:
                print(self.Controller.f8(self.citesteCriteriuPersoana()))
            except ValueError:
                pass
        elif opt == '9':
            try:
                print(self.Controller.f9(self.citesteCriteriuEveniment()))
            except ValueError:
                pass
        elif opt == '10':
            try:
                self.Controller.f10(self.citesteCriteriuOrdonarePersoane())
            except ValueError:
                pass
        elif opt == '11':
            try:
                self.Controller.f11(self.citesteCriteriuOrdonareEvenimente())
            except ValueError:
                pass
        elif opt == '12':
            try:
                self.Controller.f12()
            except ValueError:
                pass
        elif opt == '13':
            try:
                self.Controller.f13()
            except ValueError:
                pass
        elif opt == '14':
            try:
                self.Controller.f14(int(input("Cate persoane sa fie adaugate? ")), int(input("Cate evenimente sa fie adaugate? ")))
            except ValueError:
                pass
        elif opt == '15':
            try:
                self.Controller.f15("Backup.txt")
                print(str(self.Controller.BazaDeDate))
            except ValueError:
                pass
        elif opt == '16':
            try:
                self.Controller.f16("Backup.txt")
                print(str(self.Controller.BazaDeDate))
            except ValueError:
                pass
        elif opt == 'p':
            print(str(self.Controller.BazaDeDate))
        else:
            s = 'invalid'
        return s


    def citesteNume(self):
        numeDeFamilie = input("Nume de familie: ")
        prenume = input("Prenume: ")
        return Nume(numeDeFamilie, prenume)


    def citesteAdresa(self):
        strada = input("Strada: ")
        numar = input("Numar: ")
        return Adresa(strada, numar)


    def citesteTimp(self):
        an = input("An: ")
        luna = input("Luna: ")
        zi = input("Zi: ")
        ora = input("Ora: ")
        return Timp(an, luna, zi, ora)


    def citestePersoana(self):
        user = input("User: ")
        nume = self.citesteNume()
        adresa = self.citesteAdresa()
        return Persoana(user, nume, adresa)


    def schimbaDatePersoana(self):#, persoana):
        print("Ce date trebiue schimbate?")
        print("1. User")
        print("2. Nume")
        print("3. Adresa\n")
        opt = input("Optiunea dvs: ")
        newUser = ''#persoana.User
        newNume = ''#persoana.Nume
        newAdresa = ''#persoana.Adresa
        if opt == '1':
            newUser = input("Introduceti noul user: ")
            if newUser == '':
                print("User-ul nu poate fi vid")
                raise ValueError
            for pers in self.Controller.BazaDeDate.listaPersoane:
                if pers.User == newUser:
                    print("User-ul exista deja")
                    raise ValueError
            #persoana.setUser(newUser)
        elif opt == '2':
            print("Introduceti noul nume: ")
            newNume = self.citesteNume()
            newNume.Validate()
            #persoana.setNume(newNume)
        elif opt == '3':
            print("Introduceti noua adresa: ")
            newAdresa = self.citesteAdresa()
            newAdresa.Validate()
            #persoana.setAdresa(newAdresa)
        else:
            print("Optiune invalida!")
            raise ValueError
        return Persoana(newUser, newNume, newAdresa)


    def citesteEveniment(self):
        id = input("ID eveniment (4 cifre): ")
        timp = self.citesteTimp()
        descriere = input("Descriere: ")
        return Eveniment(id, timp, descriere)


    def schimbaDateEveniment(self):#, eveniment):
        print("Ce date trebiue schimbate?")
        print("1. ID")
        print("2. Timp")
        print("3. Descriere\n")
        newID = ''#eveniment.ID
        newTimp = ''#eveniment.Timp
        newDescriere = ''#eveniment.Descriere
        opt = input("Optiunea dvs: ")
        if opt == '1':
            newID = int(input("Introduceti noul ID: "))
            if newID < 0 or newID > 9999:
                print("ID-ul nu este valid")
                raise ValueError
            for ev in self.Controller.BazaDeDate.listaEvenimente:
                if ev.getID() == newID:
                    print("ID-ul exista deja")
                    raise ValueError
            #eveniment.setID(newID)
        elif opt == '2':
            print("Introduceti noua data: ")
            newTimp = self.citesteTimp()
            newTimp.Validate()
            #eveniment.setTimp(newTimp)
        elif opt == '3':
            newDescriere = input("Introduceti noua descriere: ")
            if newDescriere == '':
                print("Descrierea nu poate fi vida")
                raise ValueError
            #eveniment.setDescriere(newDescriere)
        else:
            print("Optiune invalida!")
            raise ValueError
        return Eveniment(newID, newTimp, newDescriere)


    def citesteCorespondenta(self):
        user = input("User: ")
        id = input("ID eveniment: ")
        return Corespondenta(user, id)


    def citesteCriteriuPersoana(self):
        print("La ce face referinta criteriul?")
        print("1. User")
        print("2. Nume")
        print("3. Adresa\n")
        opt = input("Optiunea dvs: ")
        if opt == '1':
            criteriu = 'user'
            reper = input("Introduceti un user ca reper: ")
            if reper == '':
                print("User-ul nu poate fi vid")
                raise ValueError
        elif opt == '2':
            criteriu = 'nume'
            reper = input("Introduceti un nume ca reper: ")
            #print("Introduceti un nume ca reper: ")
            #reper = citesteNume()
            #reper.Validate()
        elif opt == '3':
            criteriu = 'adresa'
            reper = input("Introduceti o adresa ca reper: ")
            #print("Introduceti o adresa ca reper: ")
            #reper = citesteAdresa()
            #reper.Validate()
        else:
            print("Optiune invalida!")
            raise ValueError
        semn = input("Relatia fata de reper (<, <=, ==, >=, >, !=): ")
        if semn != '<' and semn != '<=' and semn != '==' and semn != '>=' and semn != '>' and semn != '!=':
            print("Optiune invalida!")
            raise ValueError
        return {'criteriu': criteriu, 'reper': reper, 'semn': semn}


    def citesteCriteriuEveniment(self):
        print("La ce face referinta criteriul?")
        print("1. ID")
        print("2. Timp")
        print("3. Descriere\n")
        opt = input("Optiunea dvs: ")
        if opt == '1':
            criteriu = 'id'
            reper = int(input("Introduceti un id ca reper: "))
            if reper < 0 or reper > 9999:
                print("ID-ul nu poate fi vid!")
                raise ValueError
        elif opt == '2':
            criteriu = 'timp'
            print("Introduceti un moment ca reper: ")
            reper = self.citesteTimp()
            reper.Validate()
        elif opt == '3':
            criteriu = 'descriere'
            reper = input("Introduceti o descriere ca reper: ")
            if reper == '':
                print("Descrierea nu poate fi vida")
                raise ValueError
        else:
            print("Optiune invalida!")
            raise ValueError
        semn = input("Relatia fata de reper (<, <=, ==, >=, >, !=): ")
        if semn != '<' and semn != '<=' and semn != '==' and semn != '>=' and semn != '>' and semn != '!=':
            print("Optiune invalida!")
            raise ValueError
        return {'criteriu': criteriu, 'reper': reper, 'semn': semn}


    def citesteCriteriuOrdonarePersoane(self):
        print("Dupa ce criteriu sa fie ordonate?")
        print("1. User")
        print("2. Nume")
        print("3. Adresa")
        print("4. Numar de evenimente la care participa\n")
        opt = input("Optiunea dvs: ")
        if opt == '1':
            criteriu = 'user'
        elif opt == '2':
            criteriu = 'nume'
        elif opt == '3':
            criteriu = 'adresa'
        elif opt == '4':
            criteriu = 'numar evenimente'
        else:
            print("Optiune invalida!")
            raise ValueError

        print("Cum sa fie ordonate?")
        print("1. Crescator")
        print("2. Descrescator\n")
        opt = input("Optiunea dvs: ")
        if opt == '1':
            directie = 'crescator'
        elif opt == '2':
            directie = 'descrescator'
        else:
            print("Optiune invalida!")
            raise ValueError

        return [criteriu, directie]


    def citesteCriteriuOrdonareEvenimente(self):
        print("Dupa ce criteriu sa fie ordonate?")
        print("1. ID")
        print("2. Data")
        print("3. Descriere")
        print("4. Numar de persoane care participa la ele\n")
        opt = input("Optiunea dvs: ")
        if opt == '1':
            criteriu = 'id'
        elif opt == '2':
            criteriu = 'timp'
        elif opt == '3':
            criteriu = 'descriere'
        elif opt == '4':
            criteriu = 'numar persoane'
        else:
            print("Optiune invalida!")
            raise ValueError

        print("Cum sa fie ordonate?")
        print("1. Crescator")
        print("2. Descrescator\n")
        opt = input("Optiunea dvs: ")
        if opt == '1':
            directie = 'crescator'
        elif opt == '2':
            directie = 'descrescator'
        else:
            print("Optiune invalida!")
            raise ValueError

        return [criteriu, directie]
