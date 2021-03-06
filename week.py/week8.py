class Players:

    def __init__(self, name, phone_number, jersey_number):
        self.__name = name
        self.__phone_number = phone_number
        self.__jersey_number = jersey_number

    def set_name(self, name):
        self.__name = name

    def set_phone_number(self, number):
        self.__phone_number = number

    def set_jersey_number(self, number):
        self.__jersey_number = number

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def get_jersey_number(self):
        return self.__jersey_number

    def display_data(self):
        print("Player: " + self.__name)
        print("Phone number: " + str(self.__phone_number))
        print("Jersey: " + str(self.__jersey_number))


input_exit = True
team = {}
menu = ["Display Team Roster.", "Add Member.", "Remove Member.", "Edit Member.",
        "Save Data.", "Load Data.", "Exit Program."]


def print_welcome():
    print("Welcome to the Team Manager Program! ")


def print_menu(menu):
    try:
        count = 0
        print('\n===========Main Menu===========')
        for x in menu:
            count += 1
            if count is 7:
                count = 9
            print(str(count) + ". " + x)
        user_input = input("Make a selection: ")
        return user_input
    except ValueError:
        print("Input not valid ")


def display_team(team):
    if len(team) == 0:
        print("No players in the team, please add one.")

    else:
        for x in team.keys():
            team[x].display_data()


def add_member(team):
    try:
        new_member = str(input("Name of new member: "))
        new_phone_number = int(input("Phone number: "))
        new_jersey_number = int(input("Jersey number: "))
        team[new_member] = Players(new_member, new_phone_number, new_jersey_number)
        print("Member added.")
        return team
    except ValueError:
        print("Input not valid ")


def delete_member(team):
    try:
        member_delete = str(input("Member to delete: "))
        if member_delete in team:
            del team[member_delete]
            print("Member deleted.")
        else:
            print(member_delete + " not found in player roster.")
        return team
    except ValueError:
        print("Input not valid ")


def edit_member(team):
    try:
        member_edit = str(input("Member you want to edit: "))
        if member_edit in team:
            new_name = str(input("Enter the new name: "))
            new_pn = int(input("Player's phone number: "))
            new_jersey = int(input("Player's new jersey number: "))
            team[member_edit] = Players(new_name, new_pn, new_jersey)
            print(member_edit + " has been changed. New name: " + new_name)
        else:
            print("No player found on the roster with the name: " + member_edit)
        return team
    except ValueError:
        print("Input not valid.")


def save_data(team):
    try:
        file_name = str(input("Name of file to save: "))
        print("Saving data...")
        out_file = open(file_name, "wt")

        for x in team.keys():
            name = str(team[x].get_name())
            phone_number = str(team[x].get_phone_number())
            jersey_number = str(team[x].get_jersey_number())
            out_file.write(str(name+","+phone_number+","+jersey_number+"\n"))
        print("Data saved.")
        out_file.close()
    except ValueError:
        print("Input not valid.")
    except OSError:
        print("Problem saving file.")


def load_data(team):
    try:
        file_name = str(input("Name of file to load: "))
        in_file = open(file_name, "rt")
        print("File loading...")
        while True:
            in_line = in_file.readline()
            if not in_line:
                break
            in_line = in_line[:-1]
            name, phone_number, jersey_number = in_line.split(",")
            print(name + " " + jersey_number + " " + phone_number)
            team[name] = Players(name, phone_number, jersey_number)
        print("Data loaded successfully.")
        in_file.close()
        return team
    except ValueError:
        print("Input not valid.")
    except OSError:
        print("Problem loading file.")


def user_selection(user_input):
    if user_input is "1":
        display_team(team)
    elif user_input is "2":
        add_member(team)
    elif user_input is "3":
        delete_member(team)
    elif user_input is "4":
        edit_member(team)
    elif user_input is "5":
        save_data(team)
    elif user_input is "6":
        load_data(team)
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
