gender = input("Please enter your biological gender(F/M): ")
hemoglobinVal = float(input("Enter your hemoglobin value: "))

if gender == 'F':
    if hemoglobinVal < 117:
        print("Your Hemoglobin level is low.")
    elif hemoglobinVal <= 155:
        print("Your Hemoglobin level is normal")
    else:
        print("Your Hemoglobin level is high")     

elif gender == "M":
    if hemoglobinVal < 134:
        print("Your Hemoglobin level is low")
    elif hemoglobinVal <= 167:
        print("Your Hemoglobin level is normal")   
    else:
        print("Your Hemoglobin level is high")

else:
    print("Invalid Input")        
