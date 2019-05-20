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

*This readme is incomplete, and will be changed as the code is refactored.*

## item 
 > *item(name, amount, iconID)* 
 
Parameters 
 >**name** - The name of the item. 
 
 >**amount** - The amount of the item. 
 
 >**iconID** - The icon url, as a string, of the item. 
 
Description 
 >This function creates objects of the type 'item' when called.
