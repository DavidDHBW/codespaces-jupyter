
def NutzerEingabe():
    global gameOver, output, won, versuche
    rightGuess = False
    inputChar = input()
    for i in range(0, len(solution)):
        if inputChar[0] == solution[i]:
            output[i] = inputChar[0]
            rightGuess = True
    if inputChar == solution or "".join(output) == solution:
        gameOver = True
        won = True
        return
    if not rightGuess:
        print("nicht richtig. Du hast noch " + str(5 - versuche) + " Versuche überig")
        versuche += 1
    print(hangmanpics[versuche])    

        

#var
versuche = 0
solution = "test"
gameOver = False
hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

output = ["*"] * len(solution)
print("".join(output))
while not gameOver and versuche <= 5:
    print("Rate einen Buchstaben...")
    NutzerEingabe()
    print("Aktueller Fortschritt:", "".join(output))
#gameover
if won == True:
    print("Du hast gewonnen und " + str(versuche) + " Fehlversuche gebraucht")
else:
    print("Du hast zu viele Versuche gebraucht!")
    print("Das gesuchte Wort war: "+ solution)
