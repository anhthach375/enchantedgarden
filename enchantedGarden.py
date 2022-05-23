from tkinter import *
from EnchantedLog import EnchantedLog
from EnchantedMushroom import EnchantedMushroom


# A main function that:
# Requires no parameters
def main():
# Sets up the Tkinter window:
# create the main tkinter window
    window:Tk = Tk()
# set the background color, The background color should be navy
    window.configure(background="navy")
# set the title
    window.title("Enchanted Garden")
# The dimensions should be 800 x 600
    window.geometry("800x600")
# Initializes the art assets:
# You'll notice they are named with the patter mushroomNUM.png and logNUM.py. This means you can use for loops to create the 
# PhotoImage elements that the EnchantedMushroom and EnchantedLog classes each share.
    for i in range(2):
        EnchantedLog.displayImages.append(PhotoImage(file = f"log{i}.png"))
    
    for i in range(4):
        EnchantedMushroom.displayImages.append(PhotoImage(file = f"mushroom{i}.png"))
# Create and add two logs by invoking the addLogWithMushrooms (described next):
# One log should be at coordinates (0,100) with 3 mushrooms
# The other log should be at coordinates (300,350) with 4 mushrooms
    addLogWithMushrooms(window, 0, 100, 3)
    addLogWithMushrooms(window, 300, 350, 4)
    window.mainloop()

# Requires 4 parameters: The Tkinter window, An int for the x coordinate, an int for the y coordinate, An int for the number of mushrooms
def addLogWithMushrooms(window:Tk, posX:int, posY:int, numMushrooms:int) -> None:
# Should create a Tkinter Label instance to display the log
    logDisplay:Label = Label( window, bg="navy" )
# Should ask the created Label instance to place itself on the window at the specified x and y coordinates
    logDisplay.place(x=posX,y=posY)
# Should create the EnchantedLog instance and pass it the GUI label for displaying
    log:EnchantedLog = EnchantedLog(logDisplay)
# Should create the mushrooms using the createMushroom function (described next) and add them to the log using the log's 
# instance method addMushroom
# The coordinates of the mushroom mushroomNum (assuming mushroomNum takes on the values 0, 1, ...) should be:
    for mushroomNum in range(numMushrooms):
        mushroom:EnchantedMushroom = createMushroom(window, posX+40 + mushroomNum*100, posY-100)
        log.addMushroom(mushroom)
# Create createMushroom function
def createMushroom(window:Tk, posX:int, posY:int) -> EnchantedMushroom:
# Should create a Tkinter Label instance to display the mushroom
    mushroomDisplay:Label = Label( window, bg="navy" )
# Should ask the created Label instance to place itself on the window at the specified x and y coordinates
    mushroomDisplay.place(x=posX,y=posY)
    # Should create the EnchantedMushroom instance and pass it the GUI label for displaying
    mushroom:EnchantedMushroom = EnchantedMushroom(mushroomDisplay)
# Should return the EnchantedMushroom instance (so the log can add it)
    print( f"Just added a EnchantedMushroom: {mushroom}" )
    return mushroom

main()