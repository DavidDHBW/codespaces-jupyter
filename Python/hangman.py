def NutzerEingabe():
    global gameOver, output, won, versuche
    rightGuess = False
    inputChar = input()
    for i in range(0, len(solution)):
        if inputChar[0] == solution[i]:
            output[i] = inputChar[0]
            rightGuess = True
    if inputChar == solution or output == solution:
        gameOver = True
        won = True
        return
    if not rightGuess:
        versuche += 1

        

#var
versuche = 0
solution = "test"
gameOver = False

output = ["*"] * len(solution)

while not gameOver and versuche <= 6:
    print("Rate einen Buchstaben...")
    NutzerEingabe()
    print("Aktueller Fortschritt:", "".join(output))
#gameover
if won == True:
    print("Du hast gewonnen und " + versuche + " Versuche gebraucht")
else:
    print("Du hast zu viele Versuche gebraucht!")
    print("Das gesuchte Wort war: "+ solution)
