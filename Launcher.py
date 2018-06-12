from tkinter import *
import Display
import World

#programme "principal" 

# taille de la grille
height = 700
width = 1000
#taille des cellules
cellSize = 10


window = Tk()
window.title('Game of life ISN 2018')
window["bg"] = "#e7e7e7"
world = World.World(height, width, cellSize)
display=Display.Display(window,cellSize,height,width, world)

window.mainloop()
