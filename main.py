import random
counter = 6

#welkomstekst
print("Welkom bij Galgje!\nGalgje is een spel waar je een woord moet raden die de computer hier heeft uitgekozen.")

#woordenlijst
woordenlijst= ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit" , "heesterperk"]


#computer kiest willekeurig woord
woord= random.choice (woordenlijst)

geradenletters= []

#checkt of woord is geraden
def gewonnen():
  for i in range(len(woord)):
    if not woord[i] in geradenletters:
     return(False)
  return(True)

#print ? + letter (checken)
def letter():
  for a in range(len(woord)):
    if woord[a] in geradenletters:
       print(woord[a], "", end="")
    else:
       print(" ? ", end="")
  print("")
  print(" . " * len(woord))

letter()

#while functie + input + checken of letter al in woord zit
while True:
  l = input("kies een letter\n")
  if len(l) == 1:
    if l in geradenletters:
      print ("die letter heb je al geraden")
      letter()
#uitvoeren van functie letter + gewonnen
    else:
      geradenletters += l
      if l in woord:
       letter()
       if gewonnen():
        print("je hebt gewonnen")
        print("het woord was " + woord)
        break
#letter niet in woord counter -1 
      else:
       print ("-1")
       counter -= 1
       letter()
#hele woord in 1 keer goed of fout
  elif l == woord:
    print ("je hebt gewonnen")
    print("het woord was " + woord)

    break
  else:
    print("fout woord")
    print("-2")
    counter -= 2
    letter()
#verloren
  if counter <= 0:
    print ("je hebt verloren")
    print("het woord was " + woord)
    break
  print("je hebt nog", counter, "levens over")







#while functie + input + checken of letter al in woord zit

#letter niet in woord counter -1 
