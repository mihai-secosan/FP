from UI.UI import *


def run():
    bazaDeDateGoala = BazaDeDate()


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



    bazaDeDateMare = BazaDeDate()

    bazaDeDateMare.listaPersoane.append(Persoana('meHIGH', Nume('Secosan', 'Mihai'), Adresa('Snagov', 1)))
    bazaDeDateMare.listaPersoane.append(Persoana('drag000s', Nume('Bucsa', 'Dragos'), Adresa('Snagov', 11)))
    bazaDeDateMare.listaPersoane.append(Persoana('spidi', Nume('Blezu', 'Iosif'), Adresa('Rasinari', 14)))
    bazaDeDateMare.listaPersoane.append(Persoana('devx', Nume('Stoica', 'Sergiu'), Adresa('Doamna Stanca', 23)))
    bazaDeDateMare.listaPersoane.append(Persoana('sebi', Nume('Faghi', 'Sebastian'), Adresa('Calea Surii Mici', 7)))
    bazaDeDateMare.listaPersoane.append(Persoana('user1', Nume('Nume1', 'Prenume1'), Adresa('Strada', 1)))
    bazaDeDateMare.listaPersoane.append(Persoana('user2', Nume('Nume2', 'Prenume2'), Adresa('Strada', 2)))
    bazaDeDateMare.listaPersoane.append(Persoana('user3', Nume('Nume3', 'Prenume3'), Adresa('Strada', 3)))
    bazaDeDateMare.listaPersoane.append(Persoana('user4', Nume('Nume4', 'Prenume4'), Adresa('Strada', 4)))
    bazaDeDateMare.listaPersoane.append(Persoana('user5', Nume('Nume5', 'Prenume5'), Adresa('Strada', 5)))
    bazaDeDateMare.listaPersoane.append(Persoana('user6', Nume('Nume6', 'Prenume6'), Adresa('Strada', 6)))

    bazaDeDateMare.listaEvenimente.append(Eveniment(0, Timp(2022, 12, 12, 20), 'ziua lui dragos'))
    bazaDeDateMare.listaEvenimente.append(Eveniment(1, Timp(2023, 1, 1, 0), 'revelion'))
    bazaDeDateMare.listaEvenimente.append(Eveniment(2, Timp(2023, 2, 10, 9), 'sesiune'))
    bazaDeDateMare.listaEvenimente.append(Eveniment(3, Timp(2022, 12, 10, 9), 'test partial ASC'))
    bazaDeDateMare.listaEvenimente.append(Eveniment(9999, Timp(2000, 1, 1, 0), 'descriere'))
    bazaDeDateMare.listaEvenimente.append(Eveniment(9998, Timp(2000, 1, 1, 1), 'descriere'))
    bazaDeDateMare.listaEvenimente.append(Eveniment(9997, Timp(2000, 1, 1, 2), 'descriere'))
    bazaDeDateMare.listaEvenimente.append(Eveniment(9996, Timp(2000, 1, 1, 3), 'descriere'))
    bazaDeDateMare.listaEvenimente.append(Eveniment(9995, Timp(2000, 1, 1, 4), 'descriere'))
    bazaDeDateMare.listaEvenimente.append(Eveniment(9994, Timp(2000, 1, 1, 5), 'descriere'))
    bazaDeDateMare.listaEvenimente.append(Eveniment(9993, Timp(2000, 1, 1, 6), 'descriere'))

    bazaDeDateMare.listaCorespondente['meHIGH'] = [0, 1, 2, 3]
    bazaDeDateMare.listaCorespondente['drag000s'] = [0, 1]
    bazaDeDateMare.listaCorespondente['spidi'] = [1, 2, 3]
    bazaDeDateMare.listaCorespondente['sebi'] = [0]
    bazaDeDateMare.listaCorespondente['user2'] = [0, 1, 9993, 9999]
    bazaDeDateMare.listaCorespondente['user4'] = [1, 9998]
    bazaDeDateMare.listaCorespondente['user6'] = [0, 1, 9994]
    bazaDeDateMare.listaCorespondente['user5'] = [1, 9993, 9995]



    controller = Controller(bazaDeDate)          # DE AICI SETEZ PRE-SETURI
    ui = UI(controller)
    ui.print_menu()
    ui.run_menu()
    return


def test_global():
    test_str2cif()
    test_str4cif()
    test_respectare_conditie_persoana()
    test_respectare_conditie_eveniment()
    test_opus()
    test_goodOrder()
    test_to_string()
    test_gettere()
    test_to_string_repo()


#test_global()
run()
