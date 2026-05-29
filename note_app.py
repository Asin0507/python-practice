def add_note():
    note = input("Write your note: ")

    file = open("notes.txt", "a")
    file.write(note + "\n")
    file.close()

    print("Note saved!")


def view_notes():
    file = open("notes.txt", "r")

    print("\nSaved Notes:\n")

    print(file.read())

    file.close()


while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
