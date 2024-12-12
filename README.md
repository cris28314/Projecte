# Projecte

1. **Descripció del projecte:**
   - Aquest programa ens permetrà gestionar els contactes afegint i eliminant els contactes de les diferents persones , també ens permet buscar contactes en la nostra agenda.
   
2. **Interacció amb l'usuari:**
   A l'executar el programa ens mostrara diferents opcions com: Contacte afegit amb exit , dades no valides o contacte eliminat amb exit.

   Si l'usuari introdueix una cosa malament li surt un misatge comentant que es el que ha introduit malament o ha afegit o eleminiat un          contacte inexistent.
3.  **Exemples d'us:**
   ```pyhton
 Benvingut a la app de la gestió de contactes. Que vols fer?
Opció 1: Afegir un contacte a la agenda.
Opció 2: Eliminar un contacte de la agenda.
Opció 3: Mostrar la agenda.
Opció 4: Buscar contacte
Opció 5: sortir
Opció escollida: 1
Nom del contacte: Elsa
Introdueix el número de telèfon (9 dígits): 654321789
Introdueix l'adreça de correu electrònic: elsa@gmail.com
contacte Elsa afegit correctament
Benvingut a la app de la gestió de contactes. Que vols fer?
Opció 1: Afegir un contacte a la agenda.
Opció 2: Eliminar un contacte de la agenda.
Opció 3: Mostrar la agenda.
Opció 4: Buscar contacte
Opció 5: sortir
Opció escollida: 2
Quin contacte vols eliminar: Maria
{'nom': 'Maria', 'telefon': '698765432', 'email': 'maria@example.com'}
[{'nom': 'Joan', 'telefon': '612345678', 'email': 'joan@example.com'}, {'nom': 'Pere', 'telefon': '678123456', 'email': 'pere@example.com'}, {'nom': 'Elsa', 'telefon': '654321789', 'email': 'elsa@gmail.com'}]
El contacte Maria eliminat correctament
Benvingut a la app de la gestió de contactes. Que vols fer?
Opció 1: Afegir un contacte a la agenda.
Opció 2: Eliminar un contacte de la agenda.
Opció 3: Mostrar la agenda.
Opció 4: Buscar contacte
Opció 5: sortir
Opció escollida: 3
Llista de contactes: 
Nom:Joan, Telefon: 612345678, Email: joan@example.com
Nom:Pere, Telefon: 678123456, Email: pere@example.com
Nom:Elsa, Telefon: 654321789, Email: elsa@gmail.com
Benvingut a la app de la gestió de contactes. Que vols fer?
Opció 1: Afegir un contacte a la agenda.
Opció 2: Eliminar un contacte de la agenda.
Opció 3: Mostrar la agenda.
Opció 4: Buscar contacte
Opció 5: sortir
Opció escollida: 4
Quin numero de telefon vols buscar?: 612345678
Contacte trobat: Nom: Joan, Email: joan@example.com
Benvingut a la app de la gestió de contactes. Que vols fer?
Opció 1: Afegir un contacte a la agenda.
Opció 2: Eliminar un contacte de la agenda.
Opció 3: Mostrar la agenda.
Opció 4: Buscar contacte
Opció 5: sortir
Opció escollida: 5
Gràcies per utilitzar la nostra aplicació
```
4.  **Funcionament del programa:** 
 ```pyhton
1. 'Benvingut a la app de la gestió de contactes. Que vols fer?')
 ('Opció 1: Afegir un contacte a la agenda.')

   def afegir_contacte(agenda_de_contactes):
       nom = input('Nom del contacte: ')
       telefon = input("Introdueix el número de telèfon (9 dígits): ")
       email = input("Introdueix l'adreça de correu electrònic: ")

       if not validar_telefon(telefon):
           print ('El numero de telefon no es valid , ha de tenir 9 digits.')
       if not validar_email(email):
           print('L\'Adreça del correu elecronic no es valida.')
       if trobar_contacte('nom',nom, agenda_de_contactes) and trobar_contacte('telefon',telefon, agenda_de_contactes) and trobar_contacte('email',email):
           print('Aquest contacte ja existeix')
       agenda_de_contactes.append({'nom': nom ,'telefon': telefon, 'email': email})
       print(f'contacte {nom} afegit correctament')

('Opció 2: Eliminar un contacte de la agenda.')

   def eliminar_contacte(agenda_de_contactes):
       nom = input('Quin contacte vols eliminar: ')
       contacte = trobar_contacte('nom', nom, agenda_de_contactes)
       print(contacte)
       if contacte:
           agenda_de_contactes.remove(contacte)
           print(agenda_de_contactes)
       else:
           print(f'El contacte {nom} no existeix')
       print(f'El contacte {nom} eliminat correctament')
       return agenda_de_contactes

('Opció 3: Mostrar la agenda.')

   def mostrar_agenda_de_contactes(agenda_de_contactes):
       if not agenda_de_contactes:
           print('No hi ha contactes a la llista')
           return
       print('Llista de contactes: ')
       for contacte in agenda_de_contactes:
           print(f'Nom:{contacte['nom']}, Telefon: {contacte['telefon']}, Email: {contacte['email']}')

('Opció 4: Buscar contacte ')
   
   def buscar_contacte(agenda_de_contactes):
       telefon = input('Quin numero de telefon vols buscar?: ')
       contacte = trobar_contacte('telefon',telefon, agenda_de_contactes)
       if contacte:
           print(f'Contacte trobat: Nom: {contacte['nom']}, Email: {contacte['email']}')
       else:
           print ('Aquest contacte no esta a la llista')

('Opció 5: sortir')

   break

```
  
5.  **Autors:**
```python
   Elsa Gonzalez
   Cristian Sànchez
```
