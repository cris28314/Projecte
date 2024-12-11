from funcions import afegir_contacte, eliminar_contacte, buscar_contacte, mostrar_agenda_de_contactes

agenda_de_contactes = []

contactes1 = {
    'nom':'Joan',
    'telefon': '612345678',
    'email':'joan@example.com',
}

contactes2 = {
    'nom':'Maria',
    'telefon':'698765432',
    'email':'maria@example.com',
}
contactes3 = {
    'nom':'Pere',
    'telefon':'678123456',
    'email':'pere@example.com',
}

agenda_de_contactes.append(contactes1)

agenda_de_contactes.append(contactes2)

agenda_de_contactes.append(contactes3)

print(agenda_de_contactes)
    
    
def menu_de_contactes(agenda_de_contactes):
    while True:
        print('Benvingut a la app de la gestió de contactes. Que vols fer?')
        print('Opció 1: Afegir un contacte a la agenda.')
        print('Opció 2: Eliminar un contacte de la agenda.')
        print('Opció 3: Mostrar la agenda.')
        print('Opció 4: Buscar contacte ')
        print('Opció 5: sortir')

        opcio = int(input('Opció escollida: '))
        if opcio == 1: 
            agenda_de_contactes = afegir_contacte(agenda_de_contactes)
        elif opcio == 2:
            agenda_de_contactes = eliminar_contacte(agenda_de_contactes)
        elif opcio == 3:
            mostrar_agenda_de_contactes(agenda_de_contactes)
        elif opcio == 4:
            buscar_contacte(agenda_de_contactes)
        elif opcio == 5:
            print('Gràcies per utilitzar la nostra aplicació')
            break
        else:
            print('Opció no vàlida. Torna-ho a intentar.')
            
menu_de_contactes(agenda_de_contactes)