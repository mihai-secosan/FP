from Repository import *
import unittest

class TestRepositoryMethods(unittest.TestCase):

    def test_to_string_repo(self):
        self.assertEqual(str(BazaDeDate()), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

    def test_bubble_sort(self):
        bazaDeDate = BazaDeDate()
        bazaDeDate.listaPersoane.append(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        bazaDeDate.listaPersoane.append(Persoana('drag000s', Nume('Bucsa', 'Dragos'), Adresa('Snagov', 11)))
        bazaDeDate.listaPersoane.append(Persoana('spidi', Nume('Blezu', 'Iosif'), Adresa('Rasinari', 14)))
        bazaDeDate.listaPersoane.append(Persoana('devx', Nume('Stoica', 'Sergiu'), Adresa('Doamna Stanca', 23)))
        bazaDeDate.listaPersoane.append(Persoana('sebi', Nume('Faghi', 'Sebastian'), Adresa('Calea Surii Mici', 7)))
        bazaDeDate.listaEvenimente.append(Eveniment(0, Timp(2022, 12, 12, 20), 'ziua lui dragos'))
        bazaDeDate.listaEvenimente.append(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        bazaDeDate.listaEvenimente.append(Eveniment(2, Timp(2023, 2, 10, 9), 'sesiune'))
        bazaDeDate.listaEvenimente.append(Eveniment(3, Timp(2022, 12, 10, 9), 'test partial ASC'))
        bazaDeDate.listaCorespondente['meHIGH'] = [0, 1, 2, 3]
        bazaDeDate.listaCorespondente['drag000s'] = [0, 1]
        bazaDeDate.listaCorespondente['spidi'] = [1, 2, 3]
        bazaDeDate.listaCorespondente['sebi'] = [0]

        bazaDeDate.bubble_sort('user', 'crescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\ndrag000s: <0000>; <0001>\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nsebi: <0000>\nspidi: <0001>; <0002>; <0003>')

        bazaDeDate.bubble_sort('user', 'descrescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nspidi: <0001>; <0002>; <0003>\nsebi: <0000>\nmeHIGH: <0000>; <0001>; <0002>; <0003>\ndrag000s: <0000>; <0001>')

        bazaDeDate.bubble_sort('nume', 'crescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nspidi: <0001>; <0002>; <0003>\ndrag000s: <0000>; <0001>\nsebi: <0000>\nmeHIGH: <0000>; <0001>; <0002>; <0003>')

        bazaDeDate.bubble_sort('nume', 'descrescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nsebi: <0000>\ndrag000s: <0000>; <0001>\nspidi: <0001>; <0002>; <0003>')

        bazaDeDate.bubble_sort('adresa', 'crescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nsebi: <0000>\nspidi: <0001>; <0002>; <0003>\nmeHIGH: <0000>; <0001>; <0002>; <0003>\ndrag000s: <0000>; <0001>')

        bazaDeDate.bubble_sort('adresa', 'descrescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\ndrag000s: <0000>; <0001>\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nspidi: <0001>; <0002>; <0003>\nsebi: <0000>')

        bazaDeDate.bubble_sort('numar evenimente', 'crescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nsebi: <0000>\ndrag000s: <0000>; <0001>\nspidi: <0001>; <0002>; <0003>\nmeHIGH: <0000>; <0001>; <0002>; <0003>')

        bazaDeDate.bubble_sort('numar evenimente', 'descrescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nspidi: <0001>; <0002>; <0003>\ndrag000s: <0000>; <0001>\nsebi: <0000>')

    def test_shell_sort(self):
        bazaDeDate = BazaDeDate()
        bazaDeDate.listaPersoane.append(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        bazaDeDate.listaPersoane.append(Persoana('drag000s', Nume('Bucsa', 'Dragos'), Adresa('Snagov', 11)))
        bazaDeDate.listaPersoane.append(Persoana('spidi', Nume('Blezu', 'Iosif'), Adresa('Rasinari', 14)))
        bazaDeDate.listaPersoane.append(Persoana('devx', Nume('Stoica', 'Sergiu'), Adresa('Doamna Stanca', 23)))
        bazaDeDate.listaPersoane.append(Persoana('sebi', Nume('Faghi', 'Sebastian'), Adresa('Calea Surii Mici', 7)))
        bazaDeDate.listaEvenimente.append(Eveniment(0, Timp(2022, 12, 12, 20), 'ziua lui dragos'))
        bazaDeDate.listaEvenimente.append(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        bazaDeDate.listaEvenimente.append(Eveniment(2, Timp(2023, 2, 10, 9), 'sesiune'))
        bazaDeDate.listaEvenimente.append(Eveniment(3, Timp(2022, 12, 10, 9), 'test partial ASC'))
        bazaDeDate.listaCorespondente['meHIGH'] = [0, 1, 2, 3]
        bazaDeDate.listaCorespondente['drag000s'] = [0, 1]
        bazaDeDate.listaCorespondente['spidi'] = [1, 2, 3]
        bazaDeDate.listaCorespondente['sebi'] = [0]

        bazaDeDate.shell_sort('user', 'crescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\ndrag000s: <0000>; <0001>\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nsebi: <0000>\nspidi: <0001>; <0002>; <0003>')

        bazaDeDate.shell_sort('user', 'descrescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nspidi: <0001>; <0002>; <0003>\nsebi: <0000>\nmeHIGH: <0000>; <0001>; <0002>; <0003>\ndrag000s: <0000>; <0001>')

        bazaDeDate.shell_sort('nume', 'crescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nspidi: <0001>; <0002>; <0003>\ndrag000s: <0000>; <0001>\nsebi: <0000>\nmeHIGH: <0000>; <0001>; <0002>; <0003>')

        bazaDeDate.shell_sort('nume', 'descrescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nsebi: <0000>\ndrag000s: <0000>; <0001>\nspidi: <0001>; <0002>; <0003>')

        bazaDeDate.shell_sort('adresa', 'crescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nsebi: <0000>\nspidi: <0001>; <0002>; <0003>\nmeHIGH: <0000>; <0001>; <0002>; <0003>\ndrag000s: <0000>; <0001>')

        bazaDeDate.shell_sort('adresa', 'descrescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\ndrag000s: <0000>; <0001>\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nspidi: <0001>; <0002>; <0003>\nsebi: <0000>')

        bazaDeDate.shell_sort('numar evenimente', 'crescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nsebi: <0000>\ndrag000s: <0000>; <0001>\nspidi: <0001>; <0002>; <0003>\nmeHIGH: <0000>; <0001>; <0002>; <0003>')

        bazaDeDate.shell_sort('numar evenimente', 'descrescator')
        self.assertEqual(str(bazaDeDate),
                         '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nspidi: <0001>; <0002>; <0003>\ndrag000s: <0000>; <0001>\nsebi: <0000>')

    def test_select(self):
        bazaDeDate = BazaDeDate()
        bazaDeDate.listaPersoane.append(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        bazaDeDate.listaPersoane.append(Persoana('drag000s', Nume('Bucsa', 'Dragos'), Adresa('Snagov', 11)))
        bazaDeDate.listaPersoane.append(Persoana('spidi', Nume('Blezu', 'Iosif'), Adresa('Rasinari', 14)))
        bazaDeDate.listaPersoane.append(Persoana('devx', Nume('Stoica', 'Sergiu'), Adresa('Doamna Stanca', 23)))
        bazaDeDate.listaPersoane.append(Persoana('sebi', Nume('Faghi', 'Sebastian'), Adresa('Calea Surii Mici', 7)))
        bazaDeDate.listaEvenimente.append(Eveniment(0, Timp(2022, 12, 12, 20), 'ziua lui dragos'))
        bazaDeDate.listaEvenimente.append(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        bazaDeDate.listaEvenimente.append(Eveniment(2, Timp(2023, 2, 10, 9), 'sesiune'))
        bazaDeDate.listaEvenimente.append(Eveniment(3, Timp(2022, 12, 10, 9), 'test partial ASC'))
        bazaDeDate.listaCorespondente['meHIGH'] = [0, 1, 2, 3]
        bazaDeDate.listaCorespondente['drag000s'] = [0, 1]
        bazaDeDate.listaCorespondente['spidi'] = [1, 2, 3]
        bazaDeDate.listaCorespondente['sebi'] = [0]

        self.assertEqual(str(bazaDeDate.select({'criteriu': 'user', 'reper': 'meHIGH', 'semn': '=='})), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nmeHIGH: <0000>; <0001>; <0002>; <0003>')

        self.assertEqual(str(bazaDeDate.select({'criteriu': 'nume', 'reper': 'B', 'semn': '!='})), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nsebi: <0000>')

        self.assertEqual(str(bazaDeDate.select({'criteriu': 'id', 'reper': 0, 'semn': '=='})), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\n\nLista de inscrieri:\nmeHIGH: <0000>\ndrag000s: <0000>\nsebi: <0000>')

        self.assertEqual(str(bazaDeDate.select({'criteriu': 'timp', 'reper': Timp(2022, 12, 31, 23), 'semn': '>'})), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\n\nLista de inscrieri:\nmeHIGH: <0001>; <0002>\ndrag000s: <0001>\nspidi: <0001>; <0002>')

    def test_modifyPerson(self):
        bazaDeDate = BazaDeDate()
        bazaDeDate.listaPersoane.append(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        bazaDeDate.listaPersoane.append(Persoana('drag000s', Nume('Bucsa', 'Dragos'), Adresa('Snagov', 11)))
        bazaDeDate.listaPersoane.append(Persoana('spidi', Nume('Blezu', 'Iosif'), Adresa('Rasinari', 14)))
        bazaDeDate.listaPersoane.append(Persoana('devx', Nume('Stoica', 'Sergiu'), Adresa('Doamna Stanca', 23)))
        bazaDeDate.listaPersoane.append(Persoana('sebi', Nume('Faghi', 'Sebastian'), Adresa('Calea Surii Mici', 7)))
        bazaDeDate.listaEvenimente.append(Eveniment(0, Timp(2022, 12, 12, 20), 'ziua lui dragos'))
        bazaDeDate.listaEvenimente.append(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        bazaDeDate.listaEvenimente.append(Eveniment(2, Timp(2023, 2, 10, 9), 'sesiune'))
        bazaDeDate.listaEvenimente.append(Eveniment(3, Timp(2022, 12, 10, 9), 'test partial ASC'))
        bazaDeDate.listaCorespondente['meHIGH'] = [0, 1, 2, 3]
        bazaDeDate.listaCorespondente['drag000s'] = [0, 1]
        bazaDeDate.listaCorespondente['spidi'] = [1, 2, 3]
        bazaDeDate.listaCorespondente['sebi'] = [0]

        bazaDeDate.modifyPerson(4, Persoana('sebastian', '', ''))
        self.assertEqual(str(bazaDeDate.listaPersoane[4]), str(Persoana('sebastian', Nume('Faghi', 'Sebastian'), Adresa('Calea Surii Mici', 7))))

    def test_modifyEvent(self):
        bazaDeDate = BazaDeDate()
        bazaDeDate.listaPersoane.append(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        bazaDeDate.listaPersoane.append(Persoana('drag000s', Nume('Bucsa', 'Dragos'), Adresa('Snagov', 11)))
        bazaDeDate.listaPersoane.append(Persoana('spidi', Nume('Blezu', 'Iosif'), Adresa('Rasinari', 14)))
        bazaDeDate.listaPersoane.append(Persoana('devx', Nume('Stoica', 'Sergiu'), Adresa('Doamna Stanca', 23)))
        bazaDeDate.listaPersoane.append(Persoana('sebi', Nume('Faghi', 'Sebastian'), Adresa('Calea Surii Mici', 7)))
        bazaDeDate.listaEvenimente.append(Eveniment(0, Timp(2022, 12, 12, 20), 'ziua lui dragos'))
        bazaDeDate.listaEvenimente.append(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        bazaDeDate.listaEvenimente.append(Eveniment(2, Timp(2023, 2, 10, 9), 'sesiune'))
        bazaDeDate.listaEvenimente.append(Eveniment(3, Timp(2022, 12, 10, 9), 'test partial ASC'))
        bazaDeDate.listaCorespondente['meHIGH'] = [0, 1, 2, 3]
        bazaDeDate.listaCorespondente['drag000s'] = [0, 1]
        bazaDeDate.listaCorespondente['spidi'] = [1, 2, 3]
        bazaDeDate.listaCorespondente['sebi'] = [0]

        bazaDeDate.modifyEvent(3, Eveniment('', '', 'asc'))
        self.assertEqual(str(bazaDeDate.listaEvenimente[3]), str(Eveniment(3, Timp(2022, 12, 10, 9), 'asc')))
