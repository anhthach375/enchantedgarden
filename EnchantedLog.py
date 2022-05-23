from tkinter import Label
from EnchantedMushroom import EnchantedMushroom

class EnchantedLog(object):
# empty list to hold display elements
    displayImages:list = []
# There should be a constructor that:
# Requires a single argument when invoked for the Label instance used as a display
# Should initialize the instance properties
# Should set up the display to show the image at index 0 of displayImages
    def __init__(self, guiElt:Label):
# There should be a three instance properties:
# A list to track the EnchantedMushroom instances associated to the log; it should be initialized to the empty list
        self.__enchanted:bool = False
# A bool to track whether the log is enchanted (True) or not (False); it should initially not be enchanted
        self.__mushroomList:list = []
# A Label to maintain the display for the log (much like the EnchantedMushroom class)
        self.__display:Label = guiElt
# # Should set up the display to show the image at index 0 of displayImages
        self.__display["image"] = EnchantedLog.displayImages[0]
# should "bind" mouse click events to the instance method processClick       
        self.__display.bind("<Button>", self.processClick)

# There should be a getter for the enchantment level instance property called isEnchanted that:
# Requires no arguments when invoked, Should return an bool
    def isEnchanted(self) -> bool:
        return self.__enchanted
# There should be an instance method called enchant that: Requires no arguments when invoked Should have a return type of None
    
    def enchant(self) -> None:
        foundedMushroom:bool = False
# Should check if all the mushrooms associated to this log have some level of enchantment (>0).
        for mushroom in self.__mushroomList:
            if mushroom.getEnchantment() == 0:
# If so, should update the instance property to set the enchanted state to True and refresh the display.
                foundedMushroom = True
        if not foundedMushroom:
            self.__enchanted = True
# refresh the display
            self.refreshDisplay()
# There should be an instance method called addMushroom that:
# Requires a single argument when invoked of type EnchantedMushroom, Should have a return type of None
    def addMushroom(self, mushroom:EnchantedMushroom) -> None:
# Should add the passed mushroom to the list of mushrooms (maintained as an instance property)
        self.__mushroomList.append(mushroom)

# Like the EnchantedMushroom class, there should be an instance method for handling click events called processClick
    def processClick(self, event) -> None:
        print( f"Clicking: {self}" )
        self.enchant()
        print( f"... and now: {self}." )

# Like the EnchantedMushroom class, there should be an instance method for refreshing the display called refreshDisplay
    def refreshDisplay(self) -> None: 
# Requires no arguments when invoked
# Should update the displayed image to be the corresponding image in the displayImages list:
# If the log is enchanted, display the image at index 0
        if self.isEnchanted():
            self.__display["image"] = EnchantedLog.displayImages[1]
# Otherwise, display the image at index 1
        else:
            self.__display["image"] = EnchantedLog.displayImages[0]

# There should be an instance method called __str__ that Requires no arguments when invoke should return a string
    def __str__(self) -> str:
# "A log that is not enchanted with 3 mushrooms." or "A log that is enchanted with 4 mushrooms."
        result:str = "A log that is "
        if not self.isEnchanted():
            result += "not "
        result += f"enchanted with {len(self.__mushroomList)} mushrooms."
        return result
