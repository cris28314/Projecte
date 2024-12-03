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

def afegir_contacte():
    nom = input('Nom del contacte: ')
    tel = input("Introdueix el número de telèfon (9 dígits): ")
    email = input("Introdueix l'adreça de correu electrònic: ")
    if 

def validar_telefon(telefon):
    return  ((0-9){9}tel) is not None
    
def validar_email(email):
    return([@] not in email)
def trobar_contacte():
    return()




print('Benvingut a la app de la gestió de contactes. Que vols fer?')
print('Opció 1: Afegir un element a la agenda.')
print('Opció 2: Eliminar un element de la agenda.')
print('Opció 3: Mostrar la agenda.')
print('Opció 4: Buscar contacte ')

opcio = int(input('Opció escollida: '))
while opcio != 0:
    if opcio == 1: 
   
        if afegir_contacte in agenda_de_contactes:
            print('Aquest contacte ja existeix')
        if afegir_contacte not in agenda_de_contactes:
            agenda_de_contactes.append(afegir_contacte)
            print('Contacte afegit correctament')
        print(agenda_de_contactes)

    elif opcio == 2:
    def eliminar_contacte():
        nom = input("Introdueix el nom del contacte que vols eliminar: ")
    if nom in agenda_de_contactes:
        del agenda_de_contactes[nom]
        print(f"Contacte {nom} eliminat amb èxit.")
    else:
        print("Aquest contacte no està a la llista.")
        print(agenda_de_contactes)
    elif opcio == 3:
        print(agenda_de_contactes)
    elif opcio == 4:
        cercar_contacte = input('Quin telefon vols buscar')
        if cercar_contacte not in agenda_de_contactes:
            print('El contacte que busques no esta a la agenda')
        elif cercar_contacte in agenda_de_contactes:
            print('cercar_contacte')
            

    


#for contacte_nou in agenda_de_contactes:
    

#nom = input('Nom del contacte: ')
#telefon = input('Numero de telefon: ')
#gmail = input('Correu electronic: ')

#contacte_nou = {'Nom':nom,'Telefon':telefon,'Gmail':gmail}

#agenda_de_contactes.append(contacte_nou)



