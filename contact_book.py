print("-"*3,"Conatact Book","-"*3)
print("1. Add contact") 
print("2. Look up contact") 
print("3. View all contacts") 
print("4. Delete contact") 
print("5. Quit")
print()

contact_book = {}

def add_contact():
    person_name = input("Name: ")
    phone_number= int(input("Phone: "))
    contact_book[person_name] = phone_number
    print("contact saved!")
    print()
def look_for_contact():
    name_searched = input("Enter name to look up: ")
    print(name_searched,":",contact_book[name_searched])
    print()
def view_all_contact():
    for user_name,phone_number in contact_book.items():
        print(user_name,":",phone_number)
    print()
def delete_contact():
    contact_to_be_deleted = input("Enter name to delete: ")
    contact_book.pop(contact_to_be_deleted)
    print(f"{contact_to_be_deleted} deleted.")
    print()

while True:
    user_input = int(input("Choose an option: "))
    if user_input == 1:
        add_contact()
    if user_input ==2:
        look_for_contact()
    if user_input == 3:
        view_all_contact()
    if user_input == 4:
        delete_contact()
    if user_input == 5:
        print("Thank you!!!")
        print()
        break

    



