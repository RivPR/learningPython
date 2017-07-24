input_exit = True


def print_welcome():
    print("Welcome to the BMI Program! ")
    name_input = input("Please enter the student's name. ")
    return name_input


def get_weight():
    user_weight = int(input("Please enter your weight in pounds. "))

    return user_weight


def get_height():
    user_height = int(input("Please enter your height in inches. "))

    return user_height


def calculate_bmi(user_weight, user_height):
    print("Calculating your BMI...")
    weight = user_weight * 703
    height_squared = user_height * user_height
    bmi = (weight / height_squared)

    return bmi


def print_results(name, bmi):
    bmi_group = "Normal weight"
    print(bmi)
    if bmi < 18.5:
        bmi_group = "Underweight"
    elif 18.5 < bmi < 24.9:
        bmi_group = "Normal weight"
    elif 25 < bmi < 29.9:
        bmi_group = "Overweight"
    elif bmi > 30:
        bmi_group = "Obese"
    else:
        print("Error in calculation. Please try again.")
    print("Bmi: " + str(bmi) + " bmi group: " + bmi_group)
    print("Results for " + name + " are BMI: " +
          str(bmi) + " which classifies under: " + str(bmi_group))


def main():
    global input_exit
    while input_exit is True:
        name = print_welcome()
        if name == "0":
            break
        print("NAME: " + str(name))
        user_weight = get_weight()
        user_height = get_height()
        bmi = calculate_bmi(user_weight, user_height)
        print_results(name, bmi)


main()
