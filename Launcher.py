from tkinter import *
import Display
import World

#programme "principal" 

# taille de la grille
height = 400
width = 400
#taille des cellules
cellSize = 10


window = Tk()
world = World.World(height, width, cellSize)
display=Display.Display(window,cellSize,height,width, world)

window.mainloop()
