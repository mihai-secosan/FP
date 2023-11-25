from Controller import *
import unittest


class TestControllerMethods(unittest.TestCase):

    def test_f1(self):
        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\n\nLista de inscrieri:')

        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('secosan', 'Mihai'), Adresa('Snagov', 1)))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('Secosan', 'mihai'), Adresa('Snagov', 1)))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('snagov', 1)))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        controller = Controller(BazaDeDate())
        controller.f1(Persoana('', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

    def test_f1_black(self):
        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\n\nLista de inscrieri:')

        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('secosan', 'Mihai'), Adresa('Snagov', 1)))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

    def test_f2(self):
        controller = Controller(BazaDeDate())
        controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\n\nLista de inscrieri:')

        controller = Controller(BazaDeDate())
        controller.f2(Eveniment(10000, Timp(2023, 1, 1, 0), 'revelion'))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        controller = Controller(BazaDeDate())
        controller.f2(Eveniment(1, Timp(1999, 1, 1, 0), 'revelion'))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        controller = Controller(BazaDeDate())
        controller.f2(Eveniment(1, Timp(2023, 2, 29, 0), 'revelion'))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        controller = Controller(BazaDeDate())
        controller.f2(Eveniment(1, Timp(2023, 4, 31, 0), 'revelion'))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        controller = Controller(BazaDeDate())
        controller.f2(Eveniment(1, Timp(2023, 0, 1, 0), 'revelion'))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        controller = Controller(BazaDeDate())
        controller.f2(Eveniment(1, Timp(2023, 1, 0, 0), 'revelion'))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        controller = Controller(BazaDeDate())
        controller.f2(Eveniment(1, Timp(2023, 1, 1, 25), 'revelion'))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        controller = Controller(BazaDeDate())
        controller.f2(Eveniment(1, Timp(2020, 2, 29, 0), 'revelion'))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\nID: <0001>    Data si ora: <2020/02/29 00:00>    Descriere: <revelion>\n\nLista de inscrieri:')

    def test_f3(self):
        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        controller.f3(Corespondenta('meHIGH', 1))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\n\nLista de inscrieri:\nmeHIGH: <0001>')

        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        controller.f3(Corespondenta('meHIGH', 0))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\n\nLista de inscrieri:')

        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        controller.f3(Corespondenta('meHIGH', 1))
        controller.f3(Corespondenta('meHIGH', 1))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\n\nLista de inscrieri:\nmeHIGH: <0001>')

    def test_f4(self):
        for i in ['<=', '>=', '==']:
            controller = Controller(BazaDeDate())
            controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
            controller.f4(opus({'criteriu': 'user', 'reper': 'meHIGH', 'semn': i}))
            self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        for i in ['<', '>', '!=']:
            controller = Controller(BazaDeDate())
            controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
            controller.f4(opus({'criteriu': 'user', 'reper': 'meHIGH', 'semn': i}))
            self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\n\nLista de inscrieri:')

        for i in ['<=', '<', '!=']:
            controller = Controller(BazaDeDate())
            controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
            controller.f4(opus({'criteriu': 'user', 'reper': 'spidi', 'semn': i}))
            self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        for i in ['>=', '>', '==']:
            controller = Controller(BazaDeDate())
            controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
            controller.f4(opus({'criteriu': 'user', 'reper': 'spidi', 'semn': i}))
            self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\n\nLista de inscrieri:')

        for i in ['>=', '==']:
            controller = Controller(BazaDeDate())
            controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
            controller.f4(opus({'criteriu': 'nume', 'reper': 'Seco', 'semn': i}))
            self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        for i in ['<', '<=', '!=', '>']:
            controller = Controller(BazaDeDate())
            controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
            controller.f4(opus({'criteriu': 'nume', 'reper': 'Seco', 'semn': i}))
            self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\n\nLista de inscrieri:')

    def test_f5(self):
        for i in ['<=', '>=', '==']:
            controller = Controller(BazaDeDate())
            controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
            controller.f5(opus({'criteriu': 'id', 'reper': 1, 'semn': i}))
            self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        for i in ['<', '>', '!=']:
            controller = Controller(BazaDeDate())
            controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
            controller.f5(opus({'criteriu': 'id', 'reper': 1, 'semn': i}))
            self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\n\nLista de inscrieri:')

        for i in ['<=', '<', '!=']:
            controller = Controller(BazaDeDate())
            controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
            controller.f5(opus({'criteriu': 'id', 'reper': 2, 'semn': i}))
            self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        for i in ['>=', '>', '==']:
            controller = Controller(BazaDeDate())
            controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
            controller.f5(opus({'criteriu': 'id', 'reper': 2, 'semn': i}))
            self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\n\nLista de inscrieri:')

        for i in ['>=', '>', '!=']:
            controller = Controller(BazaDeDate())
            controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
            controller.f5(opus({'criteriu': 'timp', 'reper': Timp(2022, 1, 1, 0), 'semn': i}))
            self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\n\nLista de inscrieri:')

        for i in ['<=', '<', '==']:
            controller = Controller(BazaDeDate())
            controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
            controller.f5(opus({'criteriu': 'timp', 'reper': Timp(2022, 1, 1, 0), 'semn': i}))
            self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\n\nLista de inscrieri:')

    def test_f6(self):
        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        controller.f3(Corespondenta('meHIGH', 1))
        controller.f6('meHIGH', Persoana('me_high', '', ''))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <me_high>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\n\nLista de inscrieri:\nme_high: <0001>')

        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        controller.f3(Corespondenta('meHIGH', 1))
        controller.f6('meHIGH', Persoana('', Nume('Secosan', 'Mihai Sebastian'), ''))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai Sebastian>    Adresa: <Snagov 1>\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\n\nLista de inscrieri:\nmeHIGH: <0001>')

        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        controller.f3(Corespondenta('meHIGH', 1))
        controller.f6('meHIGH', Persoana('', '', Adresa('Leonida Negrescu', 2)))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Leonida Negrescu 2>\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\n\nLista de inscrieri:\nmeHIGH: <0001>')

        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        controller.f3(Corespondenta('meHIGH', 1))
        controller.f6('spidi', Persoana('me_high', '', ''))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\n\nLista de inscrieri:\nmeHIGH: <0001>')

    def test_f7(self):
        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        controller.f3(Corespondenta('meHIGH', 1))
        controller.f7(1, Eveniment(3, '', ''))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\nID: <0003>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\n\nLista de inscrieri:\nmeHIGH: <0003>')

        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        controller.f3(Corespondenta('meHIGH', 1))
        controller.f7(1, Eveniment('', Timp(2024, 2, 29, 0), ''))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\nID: <0001>    Data si ora: <2024/02/29 00:00>    Descriere: <revelion>\n\nLista de inscrieri:\nmeHIGH: <0001>')

        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        controller.f3(Corespondenta('meHIGH', 1))
        controller.f7(1, Eveniment('', '', 'an bisect'))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <an bisect>\n\nLista de inscrieri:\nmeHIGH: <0001>')

        controller = Controller(BazaDeDate())
        controller.f1(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        controller.f2(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        controller.f3(Corespondenta('meHIGH', 1))
        controller.f7(0, Eveniment(10, '', ''))
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\n\nLista de inscrieri:\nmeHIGH: <0001>')

    def test_f8(self):
        controller = Controller(BazaDeDate())
        controller.BazaDeDate.listaPersoane.append(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        controller.BazaDeDate.listaPersoane.append(Persoana('drag000s', Nume('Bucsa', 'Dragos'), Adresa('Snagov', 11)))
        controller.BazaDeDate.listaPersoane.append(Persoana('spidi', Nume('Blezu', 'Iosif'), Adresa('Rasinari', 14)))
        controller.BazaDeDate.listaPersoane.append(Persoana('devx', Nume('Stoica', 'Sergiu'), Adresa('Doamna Stanca', 23)))
        controller.BazaDeDate.listaPersoane.append(Persoana('sebi', Nume('Faghi', 'Sebastian'), Adresa('Calea Surii Mici', 7)))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(0, Timp(2022, 12, 12, 20), 'ziua lui dragos'))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(2, Timp(2023, 2, 10, 9), 'sesiune'))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(3, Timp(2022, 12, 10, 9), 'test partial ASC'))
        controller.BazaDeDate.listaCorespondente['meHIGH'] = [0, 1, 2, 3]
        controller.BazaDeDate.listaCorespondente['drag000s'] = [0, 1]
        controller.BazaDeDate.listaCorespondente['spidi'] = [1, 2, 3]
        controller.BazaDeDate.listaCorespondente['sebi'] = [0]

        self.assertEqual(controller.f8({'criteriu': 'user', 'reper': 'meHIGH', 'semn': '=='}), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nmeHIGH: <0000>; <0001>; <0002>; <0003>')

        self.assertEqual(controller.f8({'criteriu': 'nume', 'reper': 'B', 'semn': '!='}), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nsebi: <0000>')

    def test_f9(self):
        controller = Controller(BazaDeDate())
        controller.BazaDeDate.listaPersoane.append(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        controller.BazaDeDate.listaPersoane.append(Persoana('drag000s', Nume('Bucsa', 'Dragos'), Adresa('Snagov', 11)))
        controller.BazaDeDate.listaPersoane.append(Persoana('spidi', Nume('Blezu', 'Iosif'), Adresa('Rasinari', 14)))
        controller.BazaDeDate.listaPersoane.append(Persoana('devx', Nume('Stoica', 'Sergiu'), Adresa('Doamna Stanca', 23)))
        controller.BazaDeDate.listaPersoane.append(Persoana('sebi', Nume('Faghi', 'Sebastian'), Adresa('Calea Surii Mici', 7)))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(0, Timp(2022, 12, 12, 20), 'ziua lui dragos'))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(2, Timp(2023, 2, 10, 9), 'sesiune'))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(3, Timp(2022, 12, 10, 9), 'test partial ASC'))
        controller.BazaDeDate.listaCorespondente['meHIGH'] = [0, 1, 2, 3]
        controller.BazaDeDate.listaCorespondente['drag000s'] = [0, 1]
        controller.BazaDeDate.listaCorespondente['spidi'] = [1, 2, 3]
        controller.BazaDeDate.listaCorespondente['sebi'] = [0]

        self.assertEqual(controller.f9({'criteriu': 'id', 'reper': 0, 'semn': '=='}), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\n\nLista de inscrieri:\nmeHIGH: <0000>\ndrag000s: <0000>\nsebi: <0000>')

        self.assertEqual(controller.f9({'criteriu': 'timp', 'reper': Timp(2022, 12, 31, 23), 'semn': '>'}), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\n\nLista de inscrieri:\nmeHIGH: <0001>; <0002>\ndrag000s: <0001>\nspidi: <0001>; <0002>')

    def test_f10(self):
        controller = Controller(BazaDeDate())
        controller.BazaDeDate.listaPersoane.append(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        controller.BazaDeDate.listaPersoane.append(Persoana('drag000s', Nume('Bucsa', 'Dragos'), Adresa('Snagov', 11)))
        controller.BazaDeDate.listaPersoane.append(Persoana('spidi', Nume('Blezu', 'Iosif'), Adresa('Rasinari', 14)))
        controller.BazaDeDate.listaPersoane.append(Persoana('devx', Nume('Stoica', 'Sergiu'), Adresa('Doamna Stanca', 23)))
        controller.BazaDeDate.listaPersoane.append(Persoana('sebi', Nume('Faghi', 'Sebastian'), Adresa('Calea Surii Mici', 7)))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(0, Timp(2022, 12, 12, 20), 'ziua lui dragos'))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(2, Timp(2023, 2, 10, 9), 'sesiune'))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(3, Timp(2022, 12, 10, 9), 'test partial ASC'))
        controller.BazaDeDate.listaCorespondente['meHIGH'] = [0, 1, 2, 3]
        controller.BazaDeDate.listaCorespondente['drag000s'] = [0, 1]
        controller.BazaDeDate.listaCorespondente['spidi'] = [1, 2, 3]
        controller.BazaDeDate.listaCorespondente['sebi'] = [0]

        controller.f10(['user', 'crescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\ndrag000s: <0000>; <0001>\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nsebi: <0000>\nspidi: <0001>; <0002>; <0003>')

        controller.f10(['user', 'descrescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nspidi: <0001>; <0002>; <0003>\nsebi: <0000>\nmeHIGH: <0000>; <0001>; <0002>; <0003>\ndrag000s: <0000>; <0001>')

        controller.f10(['nume', 'crescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nspidi: <0001>; <0002>; <0003>\ndrag000s: <0000>; <0001>\nsebi: <0000>\nmeHIGH: <0000>; <0001>; <0002>; <0003>')

        controller.f10(['nume', 'descrescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nsebi: <0000>\ndrag000s: <0000>; <0001>\nspidi: <0001>; <0002>; <0003>')

        controller.f10(['adresa', 'crescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nsebi: <0000>\nspidi: <0001>; <0002>; <0003>\nmeHIGH: <0000>; <0001>; <0002>; <0003>\ndrag000s: <0000>; <0001>')

        controller.f10(['adresa', 'descrescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\ndrag000s: <0000>; <0001>\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nspidi: <0001>; <0002>; <0003>\nsebi: <0000>')

        controller.f10(['numar evenimente', 'crescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nsebi: <0000>\ndrag000s: <0000>; <0001>\nspidi: <0001>; <0002>; <0003>\nmeHIGH: <0000>; <0001>; <0002>; <0003>')

        controller.f10(['numar evenimente', 'descrescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nspidi: <0001>; <0002>; <0003>\ndrag000s: <0000>; <0001>\nsebi: <0000>')

    def test_f11(self):
        controller = Controller(BazaDeDate())
        controller.BazaDeDate.listaPersoane.append(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
        controller.BazaDeDate.listaPersoane.append(Persoana('drag000s', Nume('Bucsa', 'Dragos'), Adresa('Snagov', 11)))
        controller.BazaDeDate.listaPersoane.append(Persoana('spidi', Nume('Blezu', 'Iosif'), Adresa('Rasinari', 14)))
        controller.BazaDeDate.listaPersoane.append(Persoana('devx', Nume('Stoica', 'Sergiu'), Adresa('Doamna Stanca', 23)))
        controller.BazaDeDate.listaPersoane.append(Persoana('sebi', Nume('Faghi', 'Sebastian'), Adresa('Calea Surii Mici', 7)))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(0, Timp(2022, 12, 12, 20), 'ziua lui dragos'))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(2, Timp(2023, 2, 10, 9), 'sesiune'))
        controller.BazaDeDate.listaEvenimente.append(Eveniment(3, Timp(2022, 12, 10, 9), 'test partial ASC'))
        controller.BazaDeDate.listaCorespondente['meHIGH'] = [0, 1, 2, 3]
        controller.BazaDeDate.listaCorespondente['drag000s'] = [0, 1]
        controller.BazaDeDate.listaCorespondente['spidi'] = [1, 2, 3]
        controller.BazaDeDate.listaCorespondente['sebi'] = [0]

        controller.f11(['id', 'crescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\ndrag000s: <0000>; <0001>\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nsebi: <0000>\nspidi: <0001>; <0002>; <0003>')

        controller.f11(['id', 'descrescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\n\nLista de evenimente:\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\n\nLista de inscrieri:\ndrag000s: <0001>; <0000>\nmeHIGH: <0003>; <0002>; <0001>; <0000>\nsebi: <0000>\nspidi: <0003>; <0002>; <0001>')

        controller.f11(['timp', 'crescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\n\nLista de evenimente:\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\n\nLista de inscrieri:\ndrag000s: <0000>; <0001>\nmeHIGH: <0003>; <0000>; <0001>; <0002>\nsebi: <0000>\nspidi: <0003>; <0001>; <0002>')

        controller.f11(['timp', 'descrescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\n\nLista de evenimente:\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\ndrag000s: <0001>; <0000>\nmeHIGH: <0002>; <0001>; <0000>; <0003>\nsebi: <0000>\nspidi: <0002>; <0001>; <0003>')

        controller.f11(['descriere', 'crescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\n\nLista de evenimente:\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\n\nLista de inscrieri:\ndrag000s: <0001>; <0000>\nmeHIGH: <0001>; <0002>; <0003>; <0000>\nsebi: <0000>\nspidi: <0001>; <0002>; <0003>')

        controller.f11(['descriere', 'descrescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\n\nLista de inscrieri:\ndrag000s: <0000>; <0001>\nmeHIGH: <0000>; <0003>; <0002>; <0001>\nsebi: <0000>\nspidi: <0003>; <0002>; <0001>')

        controller.f11(['numar persoane', 'crescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\n\nLista de evenimente:\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\n\nLista de inscrieri:\ndrag000s: <0000>; <0001>\nmeHIGH: <0002>; <0003>; <0000>; <0001>\nsebi: <0000>\nspidi: <0002>; <0003>; <0001>')

        controller.f11(['numar persoane', 'descrescator'])
        self.assertEqual(str(controller.BazaDeDate), '\nLista de persoane:\nUser: <devx>    Nume: <Stoica Sergiu>    Adresa: <Doamna Stanca 23>\nUser: <drag000s>    Nume: <Bucsa Dragos>    Adresa: <Snagov 11>\nUser: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>\nUser: <sebi>    Nume: <Faghi Sebastian>    Adresa: <Calea Surii Mici 7>\nUser: <spidi>    Nume: <Blezu Iosif>    Adresa: <Rasinari 14>\n\nLista de evenimente:\nID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>\nID: <0001>    Data si ora: <2023/01/01 00:00>    Descriere: <revelion>\nID: <0002>    Data si ora: <2023/02/10 09:00>    Descriere: <sesiune>\nID: <0003>    Data si ora: <2022/12/10 09:00>    Descriere: <test partial ASC>\n\nLista de inscrieri:\ndrag000s: <0000>; <0001>\nmeHIGH: <0000>; <0001>; <0002>; <0003>\nsebi: <0000>\nspidi: <0001>; <0002>; <0003>')

if __name__ == '__main__':
    unittest.main()
