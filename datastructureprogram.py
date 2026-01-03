def menu():
    xl = 0
    print("\n This program gives a practice on using data structure in Python")
    while (xl != 5):
        print("\n1. For List Example ")
        print("2. For Tuple Example ")
        print("3. For Set Example ")
        print("4. For Dictionary Example ")
        print("5. Exit ")
        xl = int(input("Select one of the options above: "))
        if (xl == 1):
            list_example()
        elif (xl == 2):
            tuple_example()
        elif (xl == 3):
            set_example()
        elif (xl == 4):
            dictionary_example()
        elif (xl == 5):
            print("Program ended, have a great day!")
            break

def list_example():
    #Example code for list data structure
    fruits = ["apple", "banana", "cherry"]
    print("List of fruits:", fruits)
    choice = input("Enter a new fruit to add to the list: ")
    fruits.append(choice)
    print("Updated list of fruits:", fruits)
    choice = input("Enter a fruit to delete from the list: ")
    fruits.remove(choice)
    print("Updated list of fruits after deletion:", fruits)

def tuple_example():
    #Example code for tuple data structure
    colors = ("red", "green", "blue", "yellow", "purple")
    print("Tuple of colors:", colors)
    print("Accessing first color:", colors[0])
    print("Accessing last color:", colors[-1])
    # Allow adding a color to the tuple (create a new tuple)
    add_color = input("Enter a color to add to the tuple (or press Enter to skip): ")
    if add_color:
        colors = colors + (add_color,)
        print("Updated tuple of colors after addition:", colors)

    # Build a new tuple excluding a chosen color (tuples are immutable)
    choice = input("Enter a color to delete from the tuple: ")
    if choice in colors:
        colors = tuple(c for c in colors if c != choice)
        print("Updated tuple of colors after deletion:", colors)
    else:
        print(choice, "not found in the tuple. No changes made.")
        
def set_example():
    #Example code for set data structure
    states = {"California", "Texas", "Florida", "New York"}
    print("Name of states using python sets: ", states)
    choice = input("Enter a new state to add to the set: ")
    states.add(choice)
    print("Updated set of states:", states)
    # Prompt to delete a state from the set and show updated set
    choice = input("Enter a state to delete from the set: ")
    if choice in states:
        states.remove(choice)
        print("Updated set of states after deletion:", states)
    else:
        print(choice, "not found in the set. No changes made.")

def dictionary_example():
    #Example code for dictionary data structure
    this_city = { 'city1': 'Berlin',
                 'country1': 'Germany',
                 'population1': 364500,
                 'city2': 'London',
                 'country2': 'England',
                 'population2': 14500721,}
    print("Printing city info using dictionary in Python: ", this_city.keys())
    print("The values in the dictionary in python: ", this_city.values())
    for x in this_city:
        print(this_city[x])

menu()