from Repository.Repository import *


class BackupManager:
    def __init__(self, fileName, bazaDeDate):
        self.FilePath = fileName
        self.BazaDeDate = bazaDeDate


    def backup(self):
        with open(self.FilePath, 'w') as f:
            f.write(str(self.BazaDeDate))


    def revertFromBackup(self):
        with open(self.FilePath, 'r') as f:
            str = f.read()

        self.BazaDeDate = BazaDeDate()

        str = str.split('\n')
        str = cleanList(str)

        for i in range(len(str)):
            str[i] = str[i].split('User: <')
        str = cleanList(str)

        for i in range(len(str)):
            str[i] = str[i].split('>    Nume: <')
        str = cleanList(str)

        for i in range(len(str)):
            str[i] = str[i].split('>    Adresa: <')
        str = cleanList(str)

        for i in range(len(str)):
            str[i] = str[i].split('ID: <')
        str = cleanList(str)

        for i in range(len(str)):
            str[i] = str[i].split('>    Data si ora: <')
        str = cleanList(str)

        for i in range(len(str)):
            str[i] = str[i].split('>    Descriere: <')
        str = cleanList(str)

        for i in range(len(str)):
            str[i] = str[i].split(': <')
        str = cleanList(str)

        for i in range(len(str)):
            str[i] = str[i].split('>; <')
        str = cleanList(str)

        for i in range(len(str)):
            str[i] = str[i].split('>')
        str = cleanList(str)

        i = 1
        while str[i] != 'Lista de evenimente:':
            nume = str[i + 1].split(' ', 1)
            numeFamilie = nume[0]
            prenume = nume[1]

            adresa = str[i + 2].split(' ')
            strada = adresa[0]
            numar = int(adresa[-1])
            for j in range(1, len(adresa) - 1):
                strada += ' ' + adresa[j]

            self.BazaDeDate.listaPersoane.append(Persoana(str[i], Nume(numeFamilie, prenume), Adresa(strada, numar)))
            i += 3

        i += 1
        while str[i] != 'Lista de inscrieri:':
            timp = str[i + 1].split(' ')
            timp[0] = timp[0].split('/')
            timp[1] = timp[1].split(':')
            an = int(timp[0][0])
            luna = int(timp[0][1])
            zi = int(timp[0][2])
            ora = int(timp[1][0])
            self.BazaDeDate.listaEvenimente.append(Eveniment(int(str[i]), Timp(an, luna, zi, ora), str[i + 2]))
            i += 3

        i += 1
        while i < len(str):
            self.BazaDeDate.listaCorespondente[str[i]] = [int(str[i + 1])]
            j = 2
            try:
                while True:
                    self.BazaDeDate.listaCorespondente[str[i]].append(int(str[i + j]))
                    j += 1
            except ValueError:
                pass
            except IndexError:
                pass
            i += j


        return self.BazaDeDate
