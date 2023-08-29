#uppgift 2
tal1 = input("Ange första tal: ") 
tal2 = input("Ange andra tal: ")

print (int(tal1) + int(tal2)) 

tal1 = input("Ange första tal: ") 
tal2 = input("Ange andra tal: ")

print (int(tal1) * int(tal2))
#uppgift 3
age = input("Ange din ålder")

print(age)

#uppgift 5
print("Nu ska vi räkna BMI")
vikt = float( input("Ange din vikt (kg): "))
längd = float(input("Ange din längd (m): "))

bmi = vikt/längd**2

print(f"Ditt BMI är {bmi}")


#uppgift 6
ålder_år = int(input("ange din ålder (år): "))

veckor = ålder_år * 52

print(veckor)

#uppgift 7
vikt_kg = float(input("Ange din vikt (kg): "))

pounds = vikt_kg * 2.20462262

print(f"Din vikt i pounds är: {pounds} lbs")
print("Avrundat är vikten: ",round(pounds))