list = [1,2,3,3,4,5,6]
print(list)
max(list)
min(list)

dictionary = {"brand":"mercedes","color":["red","black","yellow"]}
print(dictionary)
print(dictionary["color"][0])

t1 = {"amount":100,"date":"yesterday","type":"purchase"}
t2 = {"amount":30,"date":"today","type":"sale"}
t3 = {"amount":1000,"date":"yesterday","type":"sale"}
transaktionen =[t1,t2,t3]
cntr = 0
for i in range (0,len(transaktionen)):
    if transaktionen[i]["date"] == "yesterday":
        cntr +=1
print("transactions yesterday: " + str(cntr))

cntr = 0
for i in range (0,len(transaktionen)):
    if transaktionen[i]["type"] == "sale":
        cntr = transaktionen[i]["amount"] +cntr
    else:
        cntr = cntr - transaktionen[i]["amount"] 
print("total amount: " + str(cntr))

