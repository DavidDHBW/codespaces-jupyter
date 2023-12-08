def NutzerEingabe():
    inputChar = input()
    if inputChar == solution:
        gameOver == True
        won = True
    else:
        for i in range(0, len(solution)):
            if inputChar[0] == solution[i]:
                print("Correct '" + inputChar[0] + "' is in the word")
        print(inputChar[0])

        

#var
gameOver = False
solution = "test" #hier kann später eine Liste mit versch. Wörtern verwendet werden um zufälliges wort auszuwählen
output = ""
for i in range(0, len(solution)):
    output = output + "*"
print(output)

while gameOver == False:
    print("Rate einen Buchstaben...")
    NutzerEingabe()


       



