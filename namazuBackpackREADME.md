NamazuBackpack is a web application created with Bootstrap and JQUERY.
The application utilizes the XIVAPI service, and is meant to supplement users while playing Final Fantasy XIV.

item
  item(name, amount, iconID)
Parameters
  name - The name of the item.
  amount - The amount of the item.
  iconID - The icon url, as a string, of the item.
Description
  This function creates objects of the type 'item' when called.

craftedItem
  craftedItem(name, amount, iconID)
Parameters
  name - The name of the item.
  amount - The amount of the item.
  iconID - The icon url, as a string, of the item.
Description
  This function creates objects of the type 'craftedItem' when called.
  
makeCalls
  makeCalls()
Description
  This function is called when the user clicks the search button, after inputting a string to search for.
  It then searches the XIVapi for items whose name contains the inputted string.
    This search uses the extra parameters &indexes=item&columns=ID,Name,Icon,GameContentLinks
  The result of this search, an array of objects, is then passed into displayItems(id).
  
displayItems
  displayItems(id)
Parameters
  id - The response from searching the XIVApi database, as an array of objects.
Description
  This function takes the object array 'id' as input.
  The array is then filtered to remove any objects not containing a 'GameContentLinks' property.
  The array is further filtered to check for objects whose .ID property matches any value in the array badID[]
  The array is further filtered to ensure the objects contain a 'GameContentLinks.Recipe', and then a 'GameContentLinks.Recipe.ItemResult' properties.
  For every object in the array, the function writeItems() is passed. This loop is limited by the amtSelect value, which is selected by the user via a 'select' type form.
