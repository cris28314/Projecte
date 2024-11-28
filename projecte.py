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


print('Benvingut a la app de la gestió de contactes. Que vols fer?')
print('Opció 1: Afegir un element a la agenda.')
print('Opció 2: Eliminar un element de la agenda.')
print('Opció 3: Mostrar la agenda.')
print('Opció 4: Buscar contacte ')

opcio = int(input('Opció escollida: '))
while opcio != 0:
    if opcio == 1:
        contacte_nou = nom = input('Nom del contacte: ')
        telefon = input('Numero de telefon: ')
        gmail = input('Correu electronic: ')
        if contacte_nou in agenda_de_contactes:
            print('Aquest contacte ja existeix')
        if contacte_nou not in agenda_de_contactes:
            agenda_de_contactes.append(contacte_nou)
            print('Contacte afegit correctament')
        print(agenda_de_contactes)

    elif opcio == 2:
        contacte_nou = input('Quin contacte vols eliminar?')
        if contacte_nou not in agenda_de_contactes:
            print('Aquest contacte no existeix')
        if contacte_nou in agenda_de_contactes:
            agenda_de_contactes.remove(contacte_nou)
            print('Contacte eliminat correctament')
        print(agenda_de_contactes)
    elif opcio == 3:
        print(agenda_de_contactes)
    elif opcio == 4:
        cercar_contacte = input('Quin telefon vols buscar')
        if cercar_contacte not in agenda_de_contactes:
            print('El contacte que vols eliminar no esta a la agenda')
        if cercar_contacte in agenda_de_contactes:
            

    


#for contacte_nou in agenda_de_contactes:
    

#nom = input('Nom del contacte: ')
#telefon = input('Numero de telefon: ')
#gmail = input('Correu electronic: ')

#contacte_nou = {'Nom':nom,'Telefon':telefon,'Gmail':gmail}

#agenda_de_contactes.append(contacte_nou)



