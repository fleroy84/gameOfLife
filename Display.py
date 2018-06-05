from tkinter import *
from tkinter.constants import *
from tkinter.ttk import *
import tkinter.filedialog
import World
from Regles import *

    
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
        
        #etiquette initiale
        self.LabelGen = Label(self.win, text ='Generation: 0\nPopulation: 0', width=15)
        self.LabelGen.pack(side='right', padx = 5)
        
        self.can1  = Canvas(win, width =width, height =height, bg ='white')
        self.can1.bind("<Button-1>", self.__left_click)
        self.can1.pack(side =TOP, padx =5, pady =5)
        
        self.__toGrid()
        
        self.text_b1 = StringVar()
        self.text_b1.set("Go !")
        b1 = Button(self.win, textvariable =self.text_b1, command = self.__go)
        b3 = Button(self.win, text ='Save', command =self.__save)
        b4 = Button(self.win, text = "RAZ", command = self.__raz)
        
        self.varcombo = StringVar()
        patternsValues = ('', 'Gosper', 'Planeur', "Réplicateur")
        combo = Combobox(self.win, textvariable = self.varcombo, values = patternsValues)
        
        combo.pack(side =LEFT, padx =3, pady =3)        
        b1.pack(side =LEFT, padx =3, pady =3)
        b3.pack(side =RIGHT, padx =3, pady =3)
        b4.pack(side = RIGHT, padx = 3, pady = 3)
        
        #règles initiales
        self.regles = {"survie" : [2,3], "naissance" : [3]}
        
        #liste déroulante pour choisir la règle du jeu
        self.regle_actuelle = StringVar()
        self.regle_actuelle.set("Standard")
        liste_regles = list(rules.keys())
        self.liste_deroulante = Combobox(self.win, textvariable = self.regle_actuelle, values = liste_regles)
        self.liste_deroulante.pack(side = "bottom", padx = 3, pady = 3)
        self.liste_deroulante.bind("<<ComboboxSelected>>", self.changer_regle)


       
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
            
    def __left_click(self, event): #fonction rendant vivante ou morte la cellule cliquee
        x = event.x -(event.x%self.cellSize)
        y = event.y -(event.y%self.cellSize)
        if self.__world.dicoCase[x,y] == 0:
            
            # L'utilisateur a t-il un pattern a afficher ?
            if self.varcombo.get() == "" :
                self.can1.create_rectangle(x, y, x + self.cellSize, y + self.cellSize, fill='black')
                self.__world.dicoCase[x,y] = 1
                self.refreshLabel()
            else :
                self.__drawPattern(x, y)
        else:
            self.can1.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill='white')
            self.__world.dicoCase[x,y]=0
            self.refreshLabel()


    def __raz(self):
        #Remise a� zero de l'affichage et du compteur de generation
        self.generation = 0
        self.__world.raz()
        self.__world.play()
        self.__reDraw()
        self.refreshLabel()
        
    def __go(self):
        #"demarrage/arret de l'animation"
        self.flag = not self.flag
        if self.flag == 1: #and self.population > 0:
            self.text_b1.set("Stop")
            self.play()
        else:
            self.text_b1.set("Go !")
        
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
        if self.population == 0: #si aucune cellule vivante, on arrete l animation
            self.flag = 0
        if self.flag > 0: 
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
                #si la cellule est vivante
                if self.__world.dicoCase[x,y]:
                    self.can1.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill='black')
                    #mort si pas dans la règle de survie
                    if self.__world.dicoState[x,y] not in self.regles["survie"]:
                        self.__world.dicoCase[x,y] = 0
                #si la cellule est morte
                else:
                    self.can1.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill='white')
                    #naissance si dans la règle de naissance
                    if self.__world.dicoState[x,y] in self.regles["naissance"]:
                        self.__world.dicoCase[x,y] = 1
                u+=1
            t+=1
            
    def __drawPattern(self, x, y):
        choise = self.varcombo.get()
        if choise == 'Gosper':   
            self.__world.canon(x, y)
        elif choise == 'Planeur':
            self.__world.planeur(x, y)
        elif choise == "Réplicateur":
            self.__world.replicateur(x, y)
        self.__world.play()
        self.__reDraw()
        self.refreshLabel()
    
    def changer_regle(self, event):
        cle = self.regle_actuelle.get()
        self.regles["survie"] = rules[cle][0]
        self.regles["naissance"] = rules[cle][1]
        