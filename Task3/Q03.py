#Write a program that asks for the biological gender and hemoglobin value (g/l). 
#The program the notifies the user if the hemoglobin value is low, normal or high.
# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.

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
