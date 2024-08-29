# Exercício 13.3: Agenda de Contatos
#
# 1. Crie um dicionário onde as chaves são nomes de contatos e os valores são números de telefone.
# 2. Peça ao utilizador para adicionar um novo contato.
# 3. Permita que o utilizador remova um contato existente.
# 4. Crie uma função para pesquisar um contato pelo nome e imprimir o número de telefone.
# 5. Modifique o programa para permitir que o utilizador atualize o número de telefone de um contato existente.
# 6. Modifique o programa para guardar a lista de contactos num ficheiro contacts.csv.

class ContactsList:
    def __init__(self) -> None:
        self.contacts = {}
    
    def list_contacts(self):
        if len(self.contacts) == 0:
            print("Contacts list is empty!")
        else: 
            for index, (name, number) in enumerate(self.contacts.items(), start=1):
                print(f"{index}. {name}: {number}")
    
    def add_contact(self):
        name = input("Contact Name: ")
        number = input("Number: ")
        if number not in self.contacts.values():
            self.contacts[name] = number
        else:
            print(f"That number is already registered.")
    
    def remove_contact(self):
        name = input("Contact Name: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    def update_contact(self):
        name, number = self.search_contact()

        if name != None and number != None:
            print("""
                What field do you want to update? 
                1. Name
                2. Number
                3. Both
                4. Back
            """)
            option = input("Option: ")

            if option == "4": return

            if option == "1" or option == "3":
                del self.contacts[name]
                name = input("Contact name: ")
                self.contacts[name] = number

            if option == "2" or option == "3":
                number = input("Number: ")
                self.contacts[name] = number
    
    def search_contact(self):
        name = input("Search contact by name: ")
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]}")
            return (name, self.contacts[name])
        else:
            print("Contact not found!")
            return (None, None)
    
    def execute(self, option):
        if option == "1":
            self.list_contacts()
        elif option == "2":
            self.add_contact()
        elif option == "3":
            self.remove_contact()
        elif option == "4":
            self.update_contact()
        elif option == "5":
            self.search_contact()
        else:
            print("Option not found!")

def menu():
    print("""
    ----- Contacts List -----
        1. List all contacts
        2. Add contact
        3. Remove contact
        4. Update contact
        5. Search contact
        0. Quit
    """)
    option = input("Option: ")
    return option

def main():
    contacts_list = ContactsList()
    while True:
        try:
            option = menu()

            if option == "0":
                print("Closing contacts list!")
                break
                
            contacts_list.execute(option)
            
        except:
            print("An error occurred.")

if __name__ == '__main__':
    main()
    