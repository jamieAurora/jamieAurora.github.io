# jamieAurora.github.io

Hi! This site will serve as a hub for any of my web development projects that regularly update.

I am currently mostly working on the NamazuBackpack, a tool to be used in tandem with FINAL FANTASY XIV.

To use the Crafting Backpack, please head over to
https://jamieaurora.github.io/namazuBackpack

To use the XIV Card Generator, go to 
https://jamieaurora.github.io/XIVcard

To try out Grid Game, go to
https://jamieaurora.github.io/gridGame

# XIV Card Generator README

The XIV Card Generator is a simple display of character data, given the input of your character's name, and the server they reside on.
Improperly entered character names may not pull the proper data.

# Grid Game

Grid Game is an experiment of replicating a retro RPG like Shin Megami Tensei in a single html file. While I was able to replicate grid-based movement, combat, and speaking to NPCs, it eventually proved too much work for a single developer. It is unfinished, but I am proud of my work on it. Movement is with the arrow keys, and Enter to confirm.

# NamazuBackpack README

NamazuBackpack is a web application created with Bootstrap and JQUERY. The application utilizes the XIVAPI service, and is meant to supplement users while playing Final Fantasy XIV.

You can enter the name or an item, or a partial part of the name. 
I.e., you can search for "Hingan Sofa" to return that precise item, or "Hingan" to return all Hingan items.
You can then select the maximum amount of items to display, with a default of 6.

The objects will be returned as buttons. Clicking a button will display the relevant crafting materials needed to craft that item!
You can click the X button on any line to remove it. Removing an entire item will not remove its materials.

*This readme is incomplete, and will be changed as the code is refactored.*

## item 
 > *item(name, amount, iconID)* 
 
**Parameters** 
 >**name** - The name of the item. 
 
 >**amount** - The amount of the item. 
 
 >**iconID** - The icon url, as a string, of the item. 
 
**Description** 
 >This function creates objects of the type 'item' when called.


## craftedItem 
 > *craftedItem(name, amount, iconID)* 
 
**Parameters** 
 >**name** - The name of the item. 
 
 >**amount** - The amount of the item. 
 
 >**iconID** - The icon url, as a string, of the item. 
 
**Description** 
 >This function creates objects of the type 'craftedItem' when called.


## makeCalls 
 > *makeCalls()* 
 
**Description** 
 >This function is called when the user clicks on the search button after inputting a string.
 The function then searches XIVAPI for objects containing that string in their name.
 Additional indexes "item&columns=ID,Name,Icon,GameContentLinks" are added to the call.
 The response is passed over to the retrieveItems function.
 
 
## retrieveItems 
 > *retrieveItems(data)* 
 
**Parameters** 
 >**data** - The array of objects returned from XIVAPI that contain the string entered by the user.
 
**Description** 
 >This function takes the returned object array, 'data', and filters it.
 It is first filtered to ensure that every object in the array contains the property 'GameContentLinks'.
 Then, it checks to ensure that no objects in the array contain a property 'ID' that match any integer included in the array 'badID'.
 Finally, it filters out any objects that do not contain a 'GameContentLinks.Recipe' and then 'GameContentLinks.Recipe.ItemResult' property.
 Then, for every value left in the array, the function passes the 'GameContentLinks.Recipe.ItemResult' property, the integer 'i', the name, and the icon properties to the function createButtons().
 This 'for' loop is limited by the 'amtSelect' form, which is a dropdown select form that the user uses to determine how many results to display.
 
## createButtons
 > *createButtons(itemData, i, name, icon)*
 
**Parameters**
 >**itemData** - The recipeID of the object passed from retrieveItems()
 >**i** - This value is no longer used and should be removed.
 >**name** - The name of the item.
 >**icon** - The icon path of the item.
 
**Description**
 >This function creates a button based on the parameters passed to it.
 The button has the display name of 'name', as well as displaying an icon.
 The icon is pulled from "https://xivapi.com" with the 'icon' value being appended to it.
 On click, these buttons will call itemButton(itemData), with 'itemData' being the recipeID of the relevant item.
 
## itemButton
 > *itemButton(id)*

**Parameters**
 >**id** - The recipeID of the item.
 
**Description**
 > This function executes when a recipeButton is clicked.
 A call is made to XIVAPI.COM/RECIPE/ with the 'id' field being appended to it.
 The returned data is passed to the printList() function.
 
 
## printList
 > *printList(data)*

**Parameters**
 >**data** - The recipeItem object passed from itemButton()

**Description**
 > This function first searches the 'craftedItemArray' by 'data.Name', to find if the item already exists.
 > The variable 'searchNum' is created, which is the location of the item in the 'craftedItemArray'
 > If the item already exists, the function incrementCraftedItems(searchNum) is called.
 > If the item does not exist, the new item is pushed into the array, and the function displayAllCraftedItems(data) is called.
 > For every 'data.AmountIngredientX', with X being any number between 0 and 5, the function updateArray(data.ItemIngredientX.Name, data.AmountIngredientX, data.ItemIngredientX.Icon) is called.

## updateArray
 > *updateArray(name,amount,icon)*
 
**Parameters**
 >**name** - The name of the item.
 >**amount** - The amount of this specific item.
 >**icon** - The icon path of the item.

**Description**
 > The array 'itemArray' is searched by the 'name' field.
 If the item exists in 'itemArray', itemArray[searchNum] is incremented by 'amount'.
 The incrementItems(searchNum) function is then called.
 If the item does not exist, it is then pushed into itemArray.
 The displayAllItems(searchNum) function is then called.
 
## incrementItems
 > *incrementItems(searchNum)*

**Parameters**
 >**searchNum** - The location of the item in itemArray.

**Description**
 >The function takes the item's location in itemArray.
 It then finds the HTML element with ID "amount" + itemArray[searchNum].name
 The .amount property is set equal to itemArray[searchNum].amount

## incrementCraftedItems
 > *incrementCraftedItems(searchNum)*

**Parameters**
 >**searchNum** - The location of the item in craftedItemArray.
 
**Description**
 >The function takes the item's location in craftedItemArray.
 This item, craftedItemArray[searchNum].amount is incremented by 1.
 It then finds the HTML element with ID "amount" + craftedItemArray[searchNum].name
 The .amount property of that element is set equal to craftedItemArray[searchNum].amount
 
## displayAllItems
 > *displayAllItems(i)*

**Parameters**
 >**i** - The index of an item in an array.

**Description**
 > This creates an HTML element named 'container'.
 This element contains a text field 'name', a text field 'amount', an image, and a button.
 The name and amount are set to itemArray[i].name and itemArray[i].amount, respectively.
 The image is set to the icon of the item.
 The button is created to the right of the item image, and on click, calls the deleteItem(ID) function.
 The container element is then appended to the 'displayIconList' HTML element. The ID of this container is set to itemArray[i].name

## deleteItem
 > *deleteItem(i)*

**Parameters**
 >**i** - The name of an item in an array.

**Description**
 >The function searches itemArray for any item with the name matching 'i'.
 This item is removed from the array, if it exists.

## deleteCItem
 >*deleteCItem(i)*
 
**Parameters**
 >**i** - The name of an item in an array.
 
**Description**
 >The function searches craftedItemArray for any item with the name matching 'i'
 This item is removed from the array, if it exists.
 
## displayAllCraftedItems
 >*displayAllCraftedItems(i)*

**Parameters**
 >**i** - The index of an item in an array.
 
**Description**
 > This creates an HTML element named 'container'.
 This element contains a text field 'name', a text field 'amount', an image, and a button.
 The name and amount are set to craftedItemArray[i].name and craftedItemArray[i].amount, respectively.
 The image is set to the icon of the item.
 The button is created to the right of the item image, and on click, calls the deleteCItem(ID) function.
 The container element is then appended to the 'displayIconList' HTML element. The ID of this container is set to craftedItemArray[i].name
 
## deleteCItem
 >*deleteCItem(id)*

**Parameters**
 >**id** - The name of the item in an array.

**Description**
 >The function searches craftedItemArray for any objects matching 'id'.
 If a matching object is found, it is removed from the array.
