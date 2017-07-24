input_exit = True
team = ['Dave Cash', 'Richie Hebner', 'Roberto Clemente', 'Willie Stargell', 'Al Oliver', 'Bob Robertson']
menu = ["Display Team Roster", "Add Member", "Remove Member", "Edit Member", "Exit Program"]


def print_welcome():
    print("Welcome to the Team Manager Program! ")


def print_menu(menu):
    count = 0
    print('\n===========Main Menu===========')
    for x in menu:
        count += 1
        if count is 5:
            count = 9
        print(str(count) + ". " + x)
    user_input = input("Make a selection: ")
    return user_input


def display_team():
    count = 0
    for x in team:
        count += 1
        print(str(count) + ". " + x)


def add_member():
    new_member = input("Name of new member: ")
    team.append(new_member)
    print("Member added.")


def delete_member():
    member_delete = input("Member to delete: ")
    print(member_delete)
    team.remove(member_delete)
    print("Member deleted.")


def edit_member():
    member_edit = input("Member you want to edit: ")
    edit_member_index = team.index(member_edit.strip())
    edit_member_name = team.pop(edit_member_index)
    new_member = input("You are going to edit: " + edit_member_name + "\nWhat is the new name? ")
    team.insert(edit_member_index, new_member)


def user_selection(user_input):
    if user_input is "1":
        display_team()
    elif user_input is "2":
        add_member()
    elif user_input is "3":
        delete_member()
    elif user_input is "4":
        edit_member()
    elif user_input is "9":
        global input_exit
        input_exit = False


def main():
    global input_exit
    global menu

    print_welcome()
    while input_exit is True:
        user_input = print_menu(menu)
        user_selection(user_input)


main()
