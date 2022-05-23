# The class should be named EnchantedMushroom.
from tkinter import Label

class EnchantedMushroom(object):
# Like the LightBulb class, there should be a shared "class variable" called displayImages. For the mushroom, this will be 
# a list that is initialized to the empty list and will ultimately hold 4 images. 
# There should be a constructor that requires a single argument when invoked for the Label instance used as a display
    displayImages:list = []
    
    def __init__( self, guiElt:Label):
# An int to track the enchantment level of the mushroom, with 0 indicating no enchantment
# A Label to maintain the display for the mushroom (much like the LightBulb class)
# Should initialize the instance properties
        self.__enchant:int = 0
        self.__display:Label = guiElt
# Should set up the display to show the image at index 0 of displayImages
        self.__display["image"] = EnchantedMushroom.displayImages[0]
# Should  "bind" mouse click events to the instance method processClick
        self.__display.bind("<Button>", self.processClick)
# There should be a getter for the enchantment level instance property called getEnchantment that equires no arguments when invoked
    def getEnchantment(self) -> int:
# # Should return an int that is 0 for the initial enchantment level (not enchanted), 1 for the next level of enchantment, etc.
        return self.__enchant
# There should be a setter to change changing the level of enchantment called setEnchantment that
# Requires a single argument when invoked of type int
    def setEnchantment(self, num:int) -> None:
        if num < 0:
            self.__enchant = 0
# If an invalid value is passed, it should assign the closest valid value.  
# For a value < 0, set the enchantment to the the closest valid value.  
        elif num >= len(EnchantedMushroom.displayImages):
            self.__enchant = len(EnchantedMushroom.displayImages)-1
    #For a value > the final level value, set the enchantment to the final level.
        else:
            self.__enchant = num
        self.refreshDisplay()
# There should be an instance method called enchant that:
# Requires no arguments when invoked
    def enchant(self) -> None:
# Should "advance" the level of enchantment by invoking the getEnchantment and setEnchantment methods
        self.setEnchantment(self.getEnchantment()+1)
# Requires a single argument when invoked (we'll skip the type for this as it would require a little more 
# GUI explanation than is within the scope of this course).
# Should invoke the instance method enchant
    def processClick(self, event) -> None:
        print( f"Clicking: {self}" )
        self.enchant()
        print( f"... and now: {self}." )
# Like the LightBulb class, there should be an instance method for refreshing the display called refreshDisplay that:
# Requires no arguments when invoked
    def refreshDisplay(self) -> None: 
# Should update the displayed image to be the corresponding image in the displayImages list.
        self.__display["image"] = EnchantedMushroom.displayImages[self.getEnchantment()]
    
# There should be an instance method called __str__ that:
# Requires no arguments when invoked
    def __str__(self) ->str:
# Should return a string representation of the mushroom. 
# If the mushroom is enchanted at level 0, for example, it should return 
# "A mushroom enchanted at level 0."
        enMushroom:str =  f"A mushroom enchanted at level {self.getEnchantment()}."
        return enMushroom

    
