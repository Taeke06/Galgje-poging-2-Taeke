import random
counter = 0
#welkomstekst
print("Welkom bij Galgje!\nGalgje is een spel waar je een woord moet raden die de computer hier heeft uitgekozen.")

#woordenlijst
woordenlijst= ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit" , "heesterperk"]
gekozenletters = []
gamerunning = True

#computer kiest willekeurig woord
woord= random.choice (woordenlijst)

#lengtewoord (in puntjes)
lengtewoord = len(woord)
temp = "." * lengtewoord
print ("het woord heeft " + str(lengtewoord) + " letters")
print(f"het woord is {woord}")



#heb je het woord
while gamerunning:
  streepjes = []
  #kies een letter
  l = input ("kies een letter\n")
  gekozenletters.append(l)
  print(gekozenletters)
  for letter in woord:
    if letter in gekozenletters:
      streepjes.append(letter)
    else: 
      streepjes.append("_")

  print(" ".join(streepjes))
  
  # i = input("nog een beurt?")
  # if(i == "n"):
  #   print("ok dan niet")
  #   gamerunning = False

