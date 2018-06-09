from tkinter import *
from tkinter.constants import *
from tkinter.ttk import *
from tkinter import messagebox
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
        b2 = Button(self.win, text ='Load', command =self.__load)
        b3 = Button(self.win, text ='Save', command =self.__save)
        b4 = Button(self.win, text = "RAZ", command = self.__raz)
        
        self.varcombo = StringVar()
        patternsValues = ('', 'Gosper', 'Planeur', "Replicateur")
        combo = Combobox(self.win, textvariable = self.varcombo, values = patternsValues)
        
        combo.pack(side =LEFT, padx =3, pady =3)        
        b1.pack(side =LEFT, padx =3, pady =3)
        b2.pack(side =LEFT, padx =3, pady =3)
        b3.pack(side =RIGHT, padx =3, pady =3)
        b4.pack(side = RIGHT, padx = 3, pady = 3)
        
        #regles initiales
        self.regles = {"survie" : [2,3], "naissance" : [3]}
        
        #liste deroulante pour choisir la regle du jeu
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
        #Remise a  zero de l'affichage
        self.__world.raz()
        self.__world.play()
        self.__reDraw()
        self.generation = 0
        self.refreshLabel()
        if self.flag == 1:
            self.__go()
            
    def __go(self):
        #"demarrage/arret de l'animation"
        self.flag = not self.flag
        if self.flag == 1: #and self.population > 0:
            self.text_b1.set("Stop")
            self.play()
        else:
            self.text_b1.set("Go !")
        
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
            self.__world.raz() #on réinitialise la grille
            x, y, alertSize = self.__world.ConfigCenteredfPosition(self.configFile.name) #en fonction des dimensions de la config, on propose un selecteur de position
            if alertSize:
                messagebox.showerror("Chargement de la configuration", "Les dimensions de la configuration sont plus grandes que la grille, elle sera tronquee")
            self.__world.loadConfigPerso(self.configFile.name,x,y)
            self.play()
            self.refreshLabel(True)
               
    def play(self):
        self.generation+=1
        self.__world.play()
        self.__reDraw()
        self.refreshLabel()
        if self.population == 0: #si aucune cellule vivante, on arrete l animation
            self.flag = 0
        if self.flag > 0: 
            self.win.after(self.vitesse,self.play)
   
    def refreshLabel(self, init_generation=False): #on passe en parametre le booleen True à la methode si l on souhaite initialiser le compteur de generatìon à 0 apres execution de play() 
        if init_generation:
            self.generation=0
        self.population = self.__world.population()
        self.LabelGen.config(text='Generation: '+str(self.generation)+'\nPopulation: '+str(self.population))
        
    def __reDraw(self): #fonction redessinant le tableau a partir de l'etat du monde et applique les regles de survie
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
                    #mort si pas dans la regle de survie
                    if self.__world.dicoState[x,y] not in self.regles["survie"]:
                        self.__world.dicoCase[x,y] = 0
                #si la cellule est morte
                else:
                    self.can1.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill='white')
                    #naissance si dans la regle de naissance
                    if self.__world.dicoState[x,y] in self.regles["naissance"]:
                        self.__world.dicoCase[x,y] = 1
                u+=1
            t+=1
            
    def __reDrawOnly(self): #fonction redessinant le tableau a partir de l'etat du monde
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
                #si la cellule est morte
                else:
                    self.can1.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill='white')
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
        self.__world.play()
        self.__reDrawOnly()
        self.refreshLabel()
    
    def changer_regle(self, event):
        cle = self.regle_actuelle.get()
        self.regles["survie"] = rules[cle][0]
        self.regles["naissance"] = rules[cle][1]
        
