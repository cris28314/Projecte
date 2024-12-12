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
5.  
 ```pyhton
1. En executar el programa, et mostrará les seguents opcions:
   'Benvingut a la app de la gestió de contactes. Que vols fer?')
    ('Opció 1: Afegir un contacte a la agenda.')
    ('Opció 2: Eliminar un contacte de la agenda.')
    ('Opció 3: Mostrar la agenda.')
    ('Opció 4: Buscar contacte ')
    ('Opció 5: sortir')
2. Al escollir una opció et sortirán diferentes funcions:
   2.1 Opció 1: et demana que afegeixis un programa posant un nom, telèfon i un correu
   2.2 Opció 2: et demana que eliminis un contacte existent en aquesta ageda de contactes
   2.3 Opció 3: et mostrará tota l'agenda amb els contactes afegits i eliminats anteriorment
   2.4 Opció 4: et busca un contacte a aprtir del número de telèfon
   2.5 Opció 5: surts de l'aplicació i et surt un missatge donant les gràcies per utilitzar aquesta aplicació
```
  
5.  **Autors:**
```python
   Elsa Gonzalez
   Cristian Sànchez
```
