import random
#welkomstekst
print("Welkom bij Galgje!\nGalgje is een spel waar je een woord moet raden die de computer hier heeft uitgekozen.")

#woordenlijst
woordenlijst= ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit" , "heesterperk"]

#computer kiest willekeurig woord
woord= random.choice (woordenlijst)

#lengtewoord (in puntjes)
lengtewoord = len(woord)
temp = "." * lengtewoord
print ("het woord heeft " + str(lengtewoord) + " letters")

#kies een letter
letter = input ("kies een letter\n")