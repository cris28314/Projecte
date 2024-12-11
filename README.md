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
   if not validar_telefon(telefon):
        print ('El numero de telefon no es valid , ha de tenir 9 digits.')
    if not validar_email(email):
        print('L\'Adreça del correu electronic no es valida.')
    if trobar_contacte('nom',nom, agenda_de_contactes) and trobar_contacte('telefon',telefon, agenda_de_contactes) and trobar_contacte('email',email):
        print('Aquest contacte ja existeix')
    agenda_de_contactes.append({'nom': nom ,'telefon': telefon, 'email': email})
    print(f'contacte {nom} afegit correctament')

    return agenda_de_contactes

```python
   
   Aquesta funció ens permet afegir un contacte.


    Aquesta funció ens permet eliminar un contacte.


     Aquesta funció ens permet buscar un contacte.

   
   Aquesta funció ens permet mostrar la agenda de contactes.


5. **Autors**
   Elsa Gonzalez
   Cristian Sànchez

