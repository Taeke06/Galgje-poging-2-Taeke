import random
counter = 0
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

#heb je het woord
while True:
  userguess = (input(": "))
  match = re.search(userguess, woord)
  if userguess == woord: 
    print('je heb het woord ' + '"' + woord + '"' + " geraden")
    break