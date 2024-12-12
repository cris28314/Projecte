# Projecte

1. **Descripció del projecte:**
   - Aquest programa ens permetra gestionar els contactes afegint i eliminant els contactes de les diferents persones , també ens permet buscar contactes en la nostra agenda.
2. **Interacció amb l'usuari**
   A l'executar el programa ens mostrara diferents opcions com : contacte afegit amb exit , dades no valides o contacte eliminat amb exit.

   Si l'usuari introdueix una cosa malament li surt un misatge comentant que es el que ha introduit mlament o ha afegit o eleminiat un       contacte inexistent.
3. **Comentaris en Blocs de Codi**
```python
#Comprovar la llargada del telefon

 if len(telefon) == 9:
        return True
    return False

#Et busca el contacte que tu vulguis trobar en aquesta llista de contactes

  for contacte in agenda_de_contactes:
    if contacte[item] == valor_item:
        return contacte    
    else:
        return False

#T'afegeix el contacte que tu vulguis crear

 nom = input('Nom del contacte: ')
    telefon = input("Introdueix el número de telèfon (9 dígits): ")
    email = input("Introdueix l'adreça de correu electrònic: ")
   if not validar_telefon(telefon):
        print ('El numero de telefon no es valid , ha de tenir 9 digits.')
    if not validar_email(email):
        print('L\'Adreça del correu electronic no es valida.')
    if trobar_contacte('nom',nom, agenda_de_contactes) and trobar_contacte('telefon',telefon, agenda_de_contactes) and trobar_contacte('email',email):
        print('Aquest contacte ja existeix')
    agenda_de_contactes.append({'nom': nom ,'telefon': telefon, 'email': email})
    print(f'contacte {nom} afegit correctament')
    return agenda_de_contactes

#T'elimina un contacte que ja exiteixi a la llista de contactes

def eliminar_contacte(agenda_de_contactes):
    nom = input('Quin contacte vols eliminar: ')
    contacte = trobar_contacte('nom', nom, agenda_de_contactes)
    if contacte:
        agenda_de_contactes.remove(contacte)
    else:
        print(f'El contacte {nom} no existeix')
    print(f'El contacte {nom} eliminat correctament')

#Et mostra tota l'agenda amb els usuaris afegits o eliminats anteriorment(si es que s'ha eliminat o afegit algun)

if not agenda_de_contactes:
        print('No hi ha contactes a la llista')
        return
    print('Llista de contactes: ')
    for contacte in agenda_de_contactes:
        print(f'Nom:{contacte['nom']}, Telefon: {contacte['telefon']}, Email: {contacte['email']}')
```


5. **Autors**
   Elsa Gonzalez
   Cristian Sànchez

