agenda_de_contactes = []

contactes1 = {
    'Nom':'Joan',
    'Telefon': '612345678',
    'Gmail':'joan@example.com',
}

contactes2 = {
    'Nom':'Maria',
    'Telefon':'698765432',
    'Gmail':'maria@example.com',
}
contactes3 = {
    'Nom':'Pere',
    'Telefon':'678123456',
    'Gmail':'pere@example.com',
}

agenda_de_contactes.append(contactes1)

agenda_de_contactes.append(contactes2)

agenda_de_contactes.append(contactes3)

print (agenda_de_contactes)
def validar_telefon(telefon):
    if len(telefon) == 9:
        return True
    return False
    
def validar_email(email):
    if ('@') and ('.')  in email:
        return True
    return False
    
def trobar_contacte():
    for contacte in agenda_de_contactes:
        return contacte

def afegir_contacte():
    nom = input('Nom del contacte: ')
    telefon = input("Introdueix el número de telèfon (9 dígits): ")
    email = input("Introdueix l'adreça de correu electrònic: ")

    if not validar_telefon(telefon):
        print ('El numero de telefon no es valid , ha de tenir 9 digits.')
    if not validar_email(email):
        print('L\'Adreça del correu elecronic no es valida.')
    if trobar_contacte('nom',nom) or trobar_contacte('telefon',telefon) or trobar_contacte('email',email):
        print('Aquest contacte ja existeix')
    agenda_de_contactes.append({'nom': nom ,'telefon': telefon, 'email': email})
    print(f'contacte {nom} afegit correctament')

def eliminar_contacte():
    nom = input('Quin contacte vols eliminar: ')
    contacte = trobar_contacte('nom', nom)
    if contacte:
        agenda_de_contactes.remove(contacte)
    else:
        print(f'El contacte {nom} no existeix')
    print(f'El contacte {nom} eliminat correctament')


def mostrar_agenda_de_contactes():
    if not agenda_de_contactes:
        print('No hi ha contactes a la llista')
        return
    print('Llista de contactes: ')
    for contacte in agenda_de_contactes:
        print(f'Nom:{contacte['nom']}, Telefon: {contacte['telefon']}, Email: {contacte['email']}')

def buscar_contacte():
    telefon = input('Quin numero de telefon vols buscar?: ')
    contacte = trobar_contacte('telefon',telefon)
    if contacte:
        print(f'Contacte trobat: Nom: {contacte['nom']}, Email: {contacte['email']}')
    else:
        print ('Aquest contacte no esta a la llista')

    
    
def menu():
    while True:
        print('Benvingut a la app de la gestió de contactes. Que vols fer?')
        print('Opció 1: Afegir un element a la agenda.')
        print('Opció 2: Eliminar un element de la agenda.')
        print('Opció 3: Mostrar la agenda.')
        print('Opció 4: Buscar contacte ')
        print('Opció 5: sortir')

        opcio = int(input('Opció escollida: '))
            if opcio == 1: 
                afegir_contacte()
            
            elif opcio == 2:
                eliminar_contacte()
            
            elif opcio == 3:
                mostrar_agenda_de_contactes
            elif opcio == 4:
                buscar_contacte
            elif opcio == 5:
                print('Gràcies per utilitzar la nostra aplicació')
                break
            else:
                print('Opció no vàlida. Torna-ho a intentar.')
                
