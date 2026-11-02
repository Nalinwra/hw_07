
document = ""

undo_stack = []
redo_stack = []

while True:
    command = input("Enter command (type/undo/redo/quit): ")

    if command == "type":
        text = input("Enter text: ")

        undo_stack.append(document)
        document = document + text

        redo_stack.clear()

        print("Document:", document)

    elif command == "undo":
        if len(undo_stack) == 0:
            print("Nothing to undo")
        else:
            redo_stack.append(document)
            document = undo_stack.pop()

            print("Document:", document)

    elif command == "redo":
        if len(redo_stack) == 0:
            print("Nothing to redo")
        else:
            undo_stack.append(document)
            document = redo_stack.pop()

            print("Document:", document)

    elif command == "quit":
        break
