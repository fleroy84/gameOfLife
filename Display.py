from tkinter import *
from tkinter.constants import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter.filedialog
import World
from Regles import *

    
class Display :
    def __init__(self, win, cellSize, height, width, world, chrono):
        #chronométrage
        self.chronometre = chrono
        
        #couleurs
        self.c_vivante = "#1525A9"
        self.c_morte = "#FFFFFF"
        self.c_bords = "#999999"
        
        #propriétés
        self.flag = 0
        self.generation = 0
        self.population = 0
        self.vitesse = 100
        self.height = height
        self.width = width
        self.win = win
        self.cellSize = cellSize
        self.__world = world
        
        #cadres
        self.cadre1 = Frame(self.win, borderwidth = 2, relief = GROOVE)
        self.cadre2 = Frame(self.win, borderwidth = 2, relief = GROOVE)
        self.cadre3 = Frame(self.win, borderwidth = 2, relief = GROOVE)
        self.cadre4 = Frame(self.win, borderwidth = 2, relief = GROOVE)
        
        #etiquette initiale
        self.LabelGen = Label(self.cadre2, text ='Generation: 0\nPopulation: 0', width=15)
        
        #canevas contenant la grille
        self.can1  = Canvas(win, width =width, height =height, bg = self.c_morte)
        self.can1.bind("<Button-1>", self.__left_click)
        
        #Boutons
        self.text_b1 = StringVar()
        self.text_b1.set("Go !")
        self.b1 = Button(self.cadre3, textvariable =self.text_b1, command = self.__go)
        self.b2 = Button(self.cadre4, text ='Load', command =self.__load)
        self.b3 = Button(self.cadre4, text ='Save', command =self.__save)
        self.b4 = Button(self.cadre3, text = "RAZ", command = self.__raz)
        
        #liste déroulante pour choisir un pattern à insérer
        self.varcombo = StringVar()
        patternsValues = ('', 'Gosper', 'Planeur', "Replicateur")
        self.combo = Combobox(self.cadre1, textvariable = self.varcombo, values = patternsValues)
        
        #liste deroulante pour choisir la regle du jeu
        self.regle_actuelle = StringVar()
        self.regle_actuelle.set("Standard")
        liste_regles = list(rules.keys())
        self.liste_deroulante = Combobox(self.cadre1, textvariable = self.regle_actuelle, values = liste_regles)
        self.liste_deroulante.bind("<<ComboboxSelected>>", self.changer_regle)
        
        #placement des widgets
        self.can1.grid(row = 1, column = 0, padx = 5, pady = 5, rowspan = 3)
        self.cadre1.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.combo.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.liste_deroulante.grid(row = 0, column = 1, padx = 5, pady = 5)
        self.cadre2.grid(row = 2, column = 1, padx = 5, pady = 5)
        self.LabelGen.grid(row = 0, column = 0)
        self.cadre3.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.b1.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.b4.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.cadre4.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.b2.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.b3.grid(row = 1, column = 0, padx = 5, pady = 5)
        
        #grille initiale
        self.__toGrid()
       
    def __toGrid(self): #fonction dessinant le tableau
        self.__vert_line()
        self.__hor_line()
    
    def __vert_line(self):
        c_x = 0
        while c_x != self.width:
            self.can1.create_line(c_x,0,c_x,self.height,width=1,fill=self.c_bords)
            c_x+=self.cellSize
    
    def __hor_line(self):
        c_y = 0
        while c_y != self.height:
            self.can1.create_line(0,c_y,self.width,c_y,width=1,fill=self.c_bords)
            c_y+=self.cellSize
            
    def __left_click(self, event): #fonction rendant vivante ou morte la cellule cliquee
        x = event.x -(event.x%self.cellSize)
        y = event.y -(event.y%self.cellSize)
        if self.__world.dicoCase[x,y] == 0:
            # L'utilisateur a t-il un pattern a afficher ?
            if self.varcombo.get() == "" :
                self.can1.create_rectangle(x, y, x + self.cellSize, y + self.cellSize, fill= self.c_vivante, outline = self.c_bords)
                self.__world.dicoCase[x,y] = 1
                self.refreshLabel()
            else :
                self.__drawPattern(x, y)
        else:
            self.can1.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill=self.c_morte, outline = self.c_bords)
            self.__world.dicoCase[x,y]=0
            self.refreshLabel()

    def __raz(self):
        #Remise a zero de l'affichage
        self.flag = 0
        self.__world.raz()
        self.__reDraw()
        self.refreshLabel(True)
        self.text_b1.set("Go !")
        self.chronometre.raz()
        self.chronometre.initfile()
            
    def __go(self):
        #"demarrage/arret de l'animation"
        self.flag = not self.flag
        if self.flag == 1: #and self.population > 0:
            self.text_b1.set("Stop")
            self.chronometre.chronostart()
            self.play()
        else:
            self.text_b1.set("Go !")
            self.chronometre.chronostop()
            self.chronometre.tofile(self.generation, self.population)
        
    def __save(self):
        if self.flag == 1:
            self.__go()
        if self.__world.population()>0:
            txt = self.__world.save()
            filename = tkinter.filedialog.asksaveasfile(title = "Enregistrer sous...")
            if filename is None:
                    return            
            if filename != "":
                with open(filename.name, "w", encoding = "utf-8") as file:
                    file.write(txt)
  
        else:
            messagebox.showerror("Sauvergarde de la configuration impossible", "La grille ne contient aucune cellule vivante.")
    
    def __load(self):
        if self.flag == 1:
            self.__go()
        self.configFile = tkinter.filedialog.askopenfile(initialdir = "/", title = "Choisissez une configuration", filetypes = (("fichiers texte","*.txt"),("tous les fichiers","*.*")))
        if self.configFile:
            self.__world.raz() #on r�initialise la grille
            x, y, alertSize = self.__world.ConfigCenteredfPosition(self.configFile.name) #en fonction des dimensions de la config, on propose un selecteur de position
            if alertSize:
                messagebox.showerror("Chargement de la configuration", "Les dimensions de la configuration sont plus grandes que la grille, elle sera tronquee")
            self.__world.loadConfigPerso(self.configFile.name,x,y)
            self.play()
            self.refreshLabel(True)
               
    def play(self):
        self.__world.play()
        self.__reDraw()
        self.refreshLabel()
        #point chronometre toute les 10 générations
        if self.generation % 10 == 0:
            self.chronometre.chronostop()
            self.chronometre.tofile(self.generation, self.population)
        if self.population == 0: #si aucune cellule vivante, on arrete l animation
            self.generation+=1
            self.flag = 0
            self.text_b1.set("Go !")
        if self.flag > 0: 
            self.generation+=1
            self.win.after(self.vitesse,self.play)
   
    def refreshLabel(self, init_generation=False): #on passe en parametre le booleen True � la methode si l on souhaite initialiser le compteur de generat�on � 0 apres execution de play() 
        if init_generation:
            self.generation=0
        self.population = self.__world.population()
        self.LabelGen.config(text='Generation: '+str(self.generation)+'\nPopulation: '+str(self.population))
            
    def __reDraw(self): #fonction redessinant le tableau a partir de l'etat du monde
        self.can1.delete(ALL)
        t=0
        while t!= self.width/self.cellSize:
            u=0
            while u!= self.height/self.cellSize:
                x=t*self.cellSize
                y=u*self.cellSize
                #si la cellule est vivante
                if self.__world.dicoCase[x,y]:
                    self.can1.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill=self.c_vivante, outline = self.c_bords)
                #si la cellule est morte
                else:
                    self.can1.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill=self.c_morte, outline = self.c_bords)
                u+=1
            t+=1
    
    def __drawPattern(self, x, y):
        choise = self.varcombo.get()
        if choise == 'Gosper':   
            self.__world.canon(x, y)
        elif choise == 'Planeur':
            self.__world.planeur(x, y)
        elif choise == "Replicateur":
            self.__world.replicateur(x, y)
        self.__reDraw()
        self.refreshLabel()
    
    def changer_regle(self, event):
        cle = self.regle_actuelle.get()
        self.__world.regles["survie"] = rules[cle][0]
        self.__world.regles["naissance"] = rules[cle][1]
        
