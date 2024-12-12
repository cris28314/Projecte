
from funcions import afegir_contacte, eliminar_contacte, buscar_contacte, mostrar_agenda_de_contactes

# Aquest programa t'ajudarà a guardar, afegir i eliminar els teus contactes.


#Aqui creem la nostra agenda de contactes i afegim algun.
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

#En aquesta part proposem les opcions que dona el nostre projecte, i més avall preguntem quina vols utilitzar, depenent de la teva resposta, fem funcionar una resposta o una altra.
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
            # Aquesta opció serveix per a afegir un contacte a l'agenda.
            agenda_de_contactes = afegir_contacte(agenda_de_contactes)
        elif opcio == 2:
            # Aquesta opció serveix per a eliminar un contacte de l'agenda.
            agenda_de_contactes = eliminar_contacte(agenda_de_contactes)
        elif opcio == 3:
            # Aquesta opció serveix per a mostrar l'agenda.
            mostrar_agenda_de_contactes(agenda_de_contactes)
        elif opcio == 4:
            # Aquesta opció serveix per a buscar un contacte dins de l'agenda.
            buscar_contacte(agenda_de_contactes)
        elif opcio == 5:
            #Aquesta opció serveix per a sortir de la nostra aplicació.
            print('Gràcies per utilitzar la nostra aplicació')
            break
        else:
            print('Opció no vàlida. Torna-ho a intentar.')
            
menu_de_contactes(agenda_de_contactes)