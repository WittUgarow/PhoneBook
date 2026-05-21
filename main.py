database = [{"name": "John", "contact": "123"}, {"name": "Will", "contact": "421"}, {"name": "Henry", "contact": "871"}]


def addContact(nameIn, contactIn):
    database.append({"name": nameIn, "contact":contactIn})

def viewDatabase(database):
    print("Contacts:")
    for i in range(len(database)):
        print("\tName: "+database[i]["name"]+" - Contact: "+str(database[i]["contact"]))

def searchDatabase(search):
    results = []
    for i in range(len(database)):
        if search in database[i]["name"] or search in str(database[i]["contact"]):
            results.append(database[i])
    return results

def main():
    choice = 0
    while choice != 4:
        print("\n===============================\n")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. See All Contacts")
        print("4. Exit")
        print("")

        choice = input("Choice: ")

        try:
            choice = int(choice)
        except:
            pass

        print("")

        if choice == 1:
            name = input("Name: ")
            contact = input("Contact: ")
            addContact(name, contact)
            print("\nCONTACT ADDED")
        elif choice == 2:
            search = input("Search: ")
            results = searchDatabase(search)
            viewDatabase(results)
        elif choice == 3:
            viewDatabase(database)
        elif choice == 4:
            break
        else:
            print("ERROR: Not a valid option") 

main()