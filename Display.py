from tkinter import *
from tkinter.constants import *
from tkinter.ttk import *
import tkinter.filedialog
import World

    
class Display :
    
    def __init__(self, win, cellSize, height, width, world):
        
        self.flag = 0
        self.generation = 0
        self.population = 0
        #vitesse de l'animation      
        self.vitesse = 100        
        
        self.height = height
        self.width = width
        self.win = win
        self.cellSize = cellSize
        self.__world = world

        self.LabelGen = Label(self.win, text ='Generation: 0\nPopulation: 0', width=15)
        self.LabelGen.pack(side='right')   
        
        self.can1  = Canvas(win, width =width, height =height, bg ='white')
        self.can1.bind("<Button-1>", self.__left_click)
        self.can1.bind("<Button-3>", self.__right_click)
        self.can1.pack(side =TOP, padx =5, pady =5)
        
        self.__toGrid()
        
        b1 = Button(self.win, text ='Go!', command = self.__go)
        b2 = Button(self.win, text ='Stop', command =self.__stop)
        b3 = Button(self.win, text ='Save', command =self.__save)   
        
        self.varcombo = StringVar()
        stockFruits	= ('Gosper', 'Planeur')
        combo = Combobox(self.win, textvariable = self.varcombo, values = stockFruits)
        combo.bind('<<ComboboxSelected>>', self.__drawPattern)
        
        combo.pack(side =LEFT, padx =3, pady =3)        
        b1.pack(side =LEFT, padx =3, pady =3)
        b2.pack(side =LEFT, padx =3, pady =3)
        b3.pack(side =RIGHT, padx =3, pady =3)
       
    def __toGrid(self): #fonction dessinant le tableau
        self.__vert_line()
        self.__hor_line()
    
    def __vert_line(self):
        c_x = 0
        while c_x != self.width:
            self.can1.create_line(c_x,0,c_x,self.height,width=1,fill='black')
            c_x+=self.cellSize
    
    def __hor_line(self):
        c_y = 0
        while c_y != self.height:
            self.can1.create_line(0,c_y,self.width,c_y,width=1,fill='black')
            c_y+=self.cellSize
            
    def __left_click(self, event): #fonction rendant vivante la cellule cliquee donc met la valeur 1 pour la cellule cliquee au dico_case
        x = event.x -(event.x%self.cellSize)
        y = event.y -(event.y%self.cellSize)
        self.can1.create_rectangle(x, y, x + self.cellSize, y + self.cellSize, fill='black')
        temp = self.__world.dicoCase
        self.__world.dicoCase[x,y]=1
        self.refreshLabel()
    
    def __right_click(self, event): #fonction tuant la cellule cliquee donc met la valeur 0 pour la cellule cliquee au dico_case
        x = event.x -(event.x%self.cellSize)
        y = event.y -(event.y%self.cellSize)
        self.can1.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill='white')
        self.__world.dicoCase[x,y]=0
        self.refreshLabel()
        
    def __go(self):
        #"demarrage de l'animation"
        if self.flag == 0 and self.population >0:
            self.flag =1
            self.play()
            
    def __stop(self):
        #"arret de l'animation" 
        self.flag =0
        
    def __save(self):
        self.flag =0
        txt = self.__world.save()
        fichier = tkinter.filedialog.asksaveasfile(title = "Enregistrer sous...")
        if fichier != "":
            with open(fichier.name, "w", encoding = "utf-8") as file:
                file.write(txt)
               
    def play(self):
        self.generation+=1
        self.__world.play()
        self.__reDraw()
        self.refreshLabel()
        if self.population ==0: #si aucune cellule vivante, on arrete l animation
            self.flag=0
        if self.flag >0: 
            self.win.after(self.vitesse,self.play)
   
    def refreshLabel(self):
        self.population = self.__world.population()
        self.LabelGen.config(text='Generation: '+str(self.generation)+'\nPopulation: '+str(self.population))
        
    def __reDraw(self): #fonction redessinant le tableau a partir de l'etat du monde
        #TODO deporter l'intelligence d'ici vers l'objet World
        self.can1.delete(ALL)
        self.__toGrid()
        t=0
        while t!= self.width/self.cellSize:
            u=0
            while u!= self.height/self.cellSize:
                x=t*self.cellSize
                y=u*self.cellSize
                if self.__world.dicoState[x,y]==3:
                    self.__world.dicoCase[x,y]=1
                    self.can1.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill='black')
                elif self.__world.dicoState[x,y]==2:
                    if self.__world.dicoCase[x,y]==1:
                        self.can1.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill='black')
                    else:
                        self.can1.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill='white')
                elif self.__world.dicoState[x,y]<2 or self.__world.dicoState[x,y]>3:
                    self.__world.dicoCase[x,y]=0
                    self.can1.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill='white')
                u+=1
            t+=1
            
    def __drawPattern(self, evt):
        choise = self.varcombo.get()
        if choise=='Gosper':   
            self.__world.canon()
        elif choise=='Planeur':
            self.__world.planeur()
        self.__go()       