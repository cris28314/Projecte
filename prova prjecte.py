import re

# Llista inicial de contactes
contactes = {
    'Joan': {'tel': '612345678', 'email': 'joan@example.com'},
    'Maria': {'tel': '698765432', 'email': 'maria@example.com'},
    'Pere': {'tel': '678123456', 'email': 'pere@example.com'}
}

def validar_numero_tel(num):
    return re.match(r'^\d{9}$', num) is not None

def validar_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None

def afegir_contacte():
    nom = input("Introdueix el nom del contacte: ")
    tel = input("Introdueix el número de telèfon (9 dígits): ")
    email = input("Introdueix l'adreça de correu electrònic: ")

    if nom in contactes:
        print("Aquest contacte ja existeix.")
        return

    if not validar_numero_tel(tel):
        print("Número de telèfon no vàlid. Ha de tenir 9 dígits.")
        return

    if not validar_email(email):
        print("Adreça de correu electrònic no vàlida.")
        return

    for contacte in contactes.values():
        if contacte['tel'] == tel or contacte['email'] == email:
            print("Ja existeix un contacte amb aquest telèfon o correu electrònic.")
            return

    contactes[nom] = {'tel': tel, 'email': email}
    print(f"Contacte {nom} afegit amb èxit.")

def eliminar_contacte():
    nom = input("Introdueix el nom del contacte que vols eliminar: ")
    if nom in contactes:
        del contactes[nom]
        print(f"Contacte {nom} eliminat amb èxit.")
    else:
        print("Aquest contacte no està a la llista.")

def mostrar_contactes():
    if not contactes:
        print("No hi ha contactes a la llista.")
        return
    print("Llista de contactes:")
    for nom, info in contactes.items():
        print(f"Nom: {nom}, Telèfon: {info['tel']}, Correu electrònic: {info['email']}")

def buscar_contacte():
    tel = input("Introdueix el número de telèfon del contacte que vols cercar: ")
    for nom, info in contactes.items():
        if info['tel'] == tel:
            print(f"Contacte trobat: Nom: {nom}, Telèfon: {info['tel']}, Correu electrònic: {info['email']}")
            return
    print("Aquest contacte no està a la llista.")

def main():
    while True:
        print("\nOpcions:")
        print("1. Afegir un contacte")
        print("2. Eliminar un contacte")
        print("3. Mostrar la llista de contactes")
        print("4. Buscar un contacte")
        print("5. Sortir")
        
        opcio = input("Selecciona una opció (1-5): ")
        
        if opcio == '1':
            afegir_contacte()
        elif opcio == '2':
            eliminar_contacte()
        elif opcio == '3':
            mostrar_contactes()
        elif opcio == '4':
            buscar_contacte()
        elif opcio == '5':
            print("Gràcies per utilitzar l'aplicació de gestió de contactes. Adéu!")
            break
        else:
            print("Opció no vàlida. Si us plau, selecciona una opció correcta.")

if __name__ == "__main__":
    main()