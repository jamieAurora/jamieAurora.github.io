CHEAT SHEET



Creating dynamic buttons from JS.
document.getElementById("buttonHome").innerHTML += "<button id="+i+" onClick=executeBattle("+tempVariable+ "," +i+");>" +actorList[i].name +"</button>";

With two parameters.
document.getElementById("buttonHome").innerHTML += "<button id="+i+" onClick=executeBattle("+tempVariable+ "," +i+");>" +actorList[i].name +"</button>";


Removing buttons of a class from JS.
[].forEach.call(document.querySelectorAll('.combatOptionButton'),function(e){
  e.parentNode.removeChild(e);
});

document.getElementById("textDisplay").style.visibility = "visible";
document.getElementById("textBox").style.visibility = "visible";
document.getElementById("textDisplay").innerHTML = "Text goes here.";


/*So, let's say we have a room.
[]
Each room will have four walls, a floor, and a ceiling.
Each room will also display the rooms two rooms forward.
So, a map may look like...

 y1 y2 y3 y4 y5 y6
x1 [0,0][1,0][2,0][3,0][4,0][5,0]
x2 [0,1][1,1][2,1][3,1][4,1][5,1]
x3 [X][X][X][O][O][X]
x4 [O][O][X][O][O][X]

So, this would be an array.

var tile = function(x,y,val)
{
this.x = x;
this.y = y;
this.val = val;
}

so, a textfile like
OOXOOO
OOXXXX
XXX00X
00X00X
Would be read through line by line, character by character
var rowCount = 0;
int i = 0;
the character is then assigned to a tile value in an array.
[i, rowCount, val] with val being X or O, O denoting a space the player can move in.
when we get to a newline, i is set back to 0, and rowCount is incremented by one.
Do this until we get to the end.

The "player" is instantiated. The player has a x and y value similar to a tile object. This x and y value is given a starting position.
We can imagine that the starting position is [1,1]
The game waits for user input.
Inputs UP, the game checks to see that there is a tile object at [x,y-1].
Inputs DOWN, the game checks to see that there is a tile object at [x,y+1].
Inputs RIGHT, the game checks to see that there is a tile object at [x+1,y].
Inputs LEFT, the game checks to see that there is a tile object at [x-1,y].
Assuming there IS a tile value at that value, and that tile.value = O, the player's coordinates are then updated to that position.
--------
-----O--
-OOOOOO-
---O-O--
-OOOO---
--------
The map grid should always be displayed.
for every value in the map array, print out [, value, ]. Then, newline.
*/
//var testMapData = "----O-,OOOOOO,--O-O-,OOOO--";
