userInput = 1
print("Welcome to the Payroll program of your company.")
while userInput != 0:
    userInput = input("Enter employee's name or enter 0 to quit.\n")
    if userInput == "0":
        print("Good bye")
        raise SystemExit
    hoursWorked = float(input("Enter how many hours the employee worked.\n"))
    payRate = float(input("Enter the employee's hourly wage.\n"))
    if hoursWorked > 40:
        overTimeHours = hoursWorked - 40
        regularPay = payRate * 40
        overTimePay = (payRate * 1.5) * overTimeHours
        grossPay = regularPay + overTimePay
        overTimePayString = str(overTimePay)
        grossPayString = str(grossPay)
        regularPayString = str(regularPay)
        print("The gross pay for " + userInput + " will be:\n" + regularPayString
              + "\nplus overtime:\n" + overTimePayString
              + "\nTotal gross pay for this period:\n" + grossPayString)
    else:
        grossPay = payRate * hoursWorked
        print("The gross pay for " + userInput + " will be:\n" + str(grossPay))




