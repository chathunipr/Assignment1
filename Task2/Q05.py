#Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). 
#The program converts the input to full kilograms and grams and outputs the result to the user:

#One talent is 20 pounds.
#One pound is 32 lots.
#One lot is 13,3 grams.

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

pounds_per_talents = 20
lots_per_pounds = 32
grams_per_lots = 13.3

tot_lots =(talents * pounds_per_talents * lots_per_pounds) + (pounds * lots_per_pounds) + lots

tot_grams = tot_lots * grams_per_lots

kg = int(tot_grams // 1000)
grams = tot_grams % 1000

print("The weight is", kg, "kilograms and", round(grams, 2), "grams.")
