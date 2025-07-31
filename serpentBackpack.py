import requests
import json
import sys

print("Hello World")

api_url = "https://v2.xivapi.com/api/search?sheets=Recipe&query=ItemResult.Name="
#api_url = "https://v2.xivapi.com/api/search?sheets=Recipe&query=ItemResult.Name=%22Bronze%20Ingot%22"

print("Enter query.")
searchedItem = input()
print("Searching for " + searchedItem)
response = requests.get(api_url+"%22"+searchedItem+"%22").json()

print ("Got here!")
print(response)
print(response)

rawJSON = json.dumps(response)
parsedJSON = json.loads(rawJSON)
valueWeWant = parsedJSON["results"]
print("valueWeWant is",valueWeWant)



#about to do some bullshit here
asString = str(valueWeWant)
splitString = asString.split(":")
print(splitString)
print(splitString[3])
moreSplit = splitString[3].split(",")
print(moreSplit[0])
itemID = moreSplit[0]
itemID = itemID[1:]
print(itemID)




#innerVal = getattr(valueWeWant, row_id[default_value])
newVal = list(valueWeWant)
newerList = valueWeWant[0]
newerList = list(newerList)
#print(newVal)
#print(newerList)
#print("New Val is ", newerList.index('row_id'))
#print(valueString)

#Recipe is the sheet at XIVApi
#Let's look for Bronze Ingot, and look for field Ingredient[0], and AmountIngredient[0]
#The field I want to be looking for is ItemResult, which is = "Bronze Ingot"
#requests.get(https://v2.xivapi.com/api/search?sheets=Recipe&query=ItemResult="Bronze Ingot")

#https://v2.xivapi.com/api/sheet/Recipe/1?fields=Ingredient

#https://v2.xivapi.com/api/sheet/Recipe/1?fields=Ingredient,AmountIngredient
#Grabs the amount ingredient, and ingredients.
#Fields.Name
#Create FOR loop. While X != 0, add value to two column array. 

itemList = []
amountList = []
response2 = requests.get("https://v2.xivapi.com/api/sheet/Recipe/"+itemID+"?fields=Ingredient,AmountIngredient").json()
rawJSON2 = json.dumps(response2)
parsedJSON2 = json.loads(rawJSON2)
valueWeWant2 = parsedJSON2["fields"]
valueWeWant3 = valueWeWant2["Ingredient"]
valueWeWant4 = valueWeWant3[0]
valueWeWant5 = valueWeWant4["fields"]
valueWeWant6 = valueWeWant5["Name"]



print("2nd call",valueWeWant6)
#itemID
i = 0
while i != 6:
  valueWeWant2 = parsedJSON2["fields"]
  valueWeWant3 = valueWeWant2["Ingredient"]
  valueWeWant4 = valueWeWant3[i]
  valueWeWant5 = valueWeWant4["fields"]
  valueWeWant6 = valueWeWant5["Name"]
 
  if valueWeWant6 == "":
    break
  print("Loop call: ",i,", ",valueWeWant6)
  itemList.insert(i,valueWeWant6)
  i+=1


q = 0
while q != 6:
  valueWeWant2 = parsedJSON2["fields"]
  valueWeWant3 = valueWeWant2["AmountIngredient"]
  valueWeWant4 = valueWeWant3[q]

 
  if valueWeWant4 == 0:
    break
  print("Loop call 2: ",q,", ",valueWeWant4)
  amountList.insert(q,valueWeWant4)
  q+=1


print(itemList)
print(amountList)