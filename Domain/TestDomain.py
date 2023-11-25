from Domain import *
import unittest

class TestDomainMethods(unittest.TestCase):

    def test_respectare_conditie_persoana(self):
        self.assertTrue(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)).respecta({'criteriu': 'user', 'reper': 'meHIGH', 'semn': '=='}))
        self.assertTrue(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)).respecta({'criteriu': 'nume', 'reper': 'Secosan', 'semn': '=='}))
        self.assertTrue(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)).respecta({'criteriu': 'adresa', 'reper': 'Snagov', 'semn': '=='}))
        self.assertFalse(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)).respecta({'criteriu': 'user', 'reper': 'meHIGH', 'semn': '<'}))
        self.assertFalse(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)).respecta({'criteriu': 'nume', 'reper': 'A', 'semn': '<='}))
        self.assertFalse(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)).respecta({'criteriu': 'adresa', 'reper': 'Snagov 2', 'semn': '=='}))

    def test_respectare_conditie_eveniment(self):
        self.assertTrue(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion').respecta({'criteriu': 'id', 'reper': 1, 'semn': '=='}))
        self.assertTrue(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion').respecta({'criteriu': 'timp', 'reper': Timp(2023, 1, 1, 0), 'semn': '=='}))
        self.assertTrue(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion').respecta({'criteriu': 'descriere', 'reper': 'revelion', 'semn': '=='}))
        self.assertFalse(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion').respecta({'criteriu': 'id', 'reper': 1, 'semn': '<'}))
        self.assertFalse(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion').respecta({'criteriu': 'timp', 'reper': Timp(2022, 12, 31, 23), 'semn': '=='}))
        self.assertFalse(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion').respecta({'criteriu': 'descriere', 'reper': 'zi de nastere', 'semn': '=='}))

    def test_goodOrder(self):
        self.assertTrue(goodOrder(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)), Persoana('drag000s', Nume('Bucsa', 'Dragos'), Adresa('Snagov', 11)), 'adresa', 'crescator', BazaDeDate()))
        self.assertFalse(goodOrder(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)), Persoana('drag000s', Nume('Bucsa', 'Dragos'), Adresa('Snagov', 11)), 'adresa', 'descrescator', BazaDeDate()))

    def test_to_string(self):
        self.assertEqual(str(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1))), 'User: <meHIGH>    Nume: <Secosan Mihai>    Adresa: <Snagov 1>')
        self.assertEqual(str(Eveniment(0, Timp(2022, 12, 12, 20), 'ziua lui dragos')), 'ID: <0000>    Data si ora: <2022/12/12 20:00>    Descriere: <ziua lui dragos>')

    def test_gettere(self):
        self.assertEqual(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)).getNumeDeFamilie(), 'Secosan')
        self.assertEqual(Eveniment(0, Timp(2022, 12, 12, 20), 'ziua lui dragos').getTimp(), '2022/12/12 20:00')
