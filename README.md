# jamieAurora.github.io

Hi! This site will serve as a hub for any of my web development projects that regularly update.

I am currently mostly working on the NamazuBackpack, a tool to be used in tandem with FINAL FANTASY XIV.

To use the Crafting Backpack, please head over to
https://jamieaurora.github.io/namazuBackpack

You can enter the name or an item, or a partial part of the name. 
I.e., you can search for "Hingan Sofa" to return that precise item, or "Hingan" to return all Hingan items.
You can then select the maximum amount of items to display, with a default of 6.

The objects will be returned as buttons. Clicking a button will display the relevant crafting materials needed to craft that item!
You can click the X button on any line to remove it. Removing an entire item will not remove its materials.


# NamazuBackpack README

NamazuBackpack is a web application created with Bootstrap and JQUERY. The application utilizes the XIVAPI service, and is meant to supplement users while playing Final Fantasy XIV.

#### item 
# *item(name, amount, iconID)* 
## Parameters 
### name - The name of the item. 
### amount - The amount of the item. 
### iconID - The icon url, as a string, of the item. 
## Description 
### This function creates objects of the type 'item' when called.

#### craftedItem 
# *craftedItem(name, amount, iconID)*
## Parameters
### name - The name of the item.
### amount - The amount of the item. 
### iconID - The icon url, as a string, of the item.
## Description 
### This function creates objects of the type 'craftedItem' when called.

#### makeCalls 
# *makeCalls()*
## Description 
### This function is called when the user clicks the search button, after inputting a string to search for. It then searches the XIVapi for items whose name contains the inputted string. This search uses the extra parameters &indexes=item&columns=ID,Name,Icon,GameContentLinks The result of this search, an array of objects, is then passed into displayItems(id).

#### displayItems
# *displayItems(id)* 
## Parameters 
### id - The response from searching the XIVApi database, as an array of objects. 
## Description 
### This function takes the object array 'id' as input. The array is then filtered to remove any objects not containing a 'GameContentLinks' property. The array is further filtered to check for objects whose .ID property matches any value in the array badID[] The array is further filtered to ensure the objects contain a 'GameContentLinks.Recipe', and then a 'GameContentLinks.Recipe.ItemResult' properties. For every object in the array, the function writeItems() is passed. This loop is limited by the amtSelect value, which is selected by the user via a 'select' type form.
