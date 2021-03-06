import ConfigUtils
import Constants

class World:
    
    def __init__(self, height, width, cellSize):
        self.height = height
        self.width = width
        self.cellSize = cellSize
        self.__dico_etat = {} #dictionnaire contenant le nombre de cellules vivantes autour de chaque cellule
        self.__dico_case = {} #dictionnaire contenant les coordonnees de chaques cellules et une valeur 0 ou 1 si elles sont respectivement mortes ou vivantes
        
        #regles initiales
        self.regles = {"survie" : [2,3], "naissance" : [3]}        
        
        #Mise a zero de la grille du jeu
        self.raz()
    
    
    def play(self): #fonction permettant au monde d'evoluer
        self.__count()
        self.__update_world()   
            
    def __count(self): #fonction comptant le nombre de cellules vivantes autour de chaque cellule
        v=0
        while v!= self.width/self.cellSize:
            w=0
            while w!= self.height/self.cellSize:
                x=v*self.cellSize
                y=w*self.cellSize
    
                # cas speciaux:
                # les coins
                if x==0 and y==0: #coin en haut a gauche
                    compt_viv=0
                    if self.__dico_case[x, y + self.cellSize] == 1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y+self.cellSize]==1:
                        compt_viv+=1
                    self.__dico_etat[x, y]=compt_viv
                elif x==0 and y==int(self.height-self.cellSize): #coin en bas a gauche
                    compt_viv=0
                    if self.__dico_case[x, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y]==1:
                        compt_viv+=1
                    self.__dico_etat[x, y]=compt_viv
                elif x==int(self.width-self.cellSize) and y==0: #coin en haut a droite
                    compt_viv=0
                    if self.__dico_case[x-self.cellSize, y]==1:
                        compt_viv+=1
                    if self.__dico_case[x-self.cellSize, y+self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x, y+self.cellSize]==1:
                        compt_viv+=1
                    self.__dico_etat[x, y]=compt_viv
                elif x==int(self.width-self.cellSize) and y==int(self.height-self.cellSize): #coin en bas à droite
                    compt_viv=0
                    if self.__dico_case[x-self.cellSize, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x-self.cellSize, y]==1:
                        compt_viv+=1
                    if self.__dico_case[x, y-self.cellSize]==1:
                        compt_viv+=1
                    self.__dico_etat[x, y]=compt_viv
    
                # cas speciaux:
                # les bords du tableau (sans les coins)    
                elif x==0 and 0<y<int(self.height-self.cellSize): # bord de gauche
                    compt_viv=0
                    if self.__dico_case[x, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x, y+self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y+self.cellSize]==1:
                        compt_viv+=1
                    self.__dico_etat[x, y]=compt_viv
                elif x==int(self.width-self.cellSize) and 0<y<int(self.height-self.cellSize): # bord de droite
                    compt_viv=0
                    if self.__dico_case[x-self.cellSize, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x-self.cellSize, y]==1:
                        compt_viv+=1
                    if self.__dico_case[x-self.cellSize, y+self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x, y+self.cellSize]==1:
                        compt_viv+=1
                    self.__dico_etat[x, y]=compt_viv
                elif 0<x<int(self.width-self.cellSize) and y==0: # bord du haut
                    compt_viv=0
                    if self.__dico_case[x-self.cellSize, y]==1:
                        compt_viv+=1
                    if self.__dico_case[x-self.cellSize, y+self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x, y+self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y+self.cellSize]==1:
                        compt_viv+=1
                    self.__dico_etat[x, y]=compt_viv
                elif 0<x<int(self.width-self.cellSize) and y==int(self.height-self.cellSize): # bord du bas
                    compt_viv=0
                    if self.__dico_case[x-self.cellSize, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x-self.cellSize, y]==1:
                        compt_viv+=1
                    if self.__dico_case[x, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y]==1:
                        compt_viv+=1
                    self.__dico_etat[x, y]=compt_viv
    
                #cas generaux
                #les cellules qui ne sont pas dans les bords du tableau
                else:
                    compt_viv=0
                    if self.__dico_case[x-self.cellSize, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x-self.cellSize, y]==1:
                        compt_viv+=1
                    if self.__dico_case[x-self.cellSize, y+self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x, y+self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y+self.cellSize]==1:
                        compt_viv+=1
                    self.__dico_etat[x, y]=compt_viv
    
                w+=1
            v+=1        

    def __update_world(self): #fonction redessinant le tableau a partir de l'etat du monde et applique les regles de survie
        t=0
        while t!= self.width/self.cellSize:
            u=0
            while u!= self.height/self.cellSize:
                x=t*self.cellSize
                y=u*self.cellSize
                #si la cellule est vivante
                if self.__dico_case[x,y]:
                    #mort si pas dans la regle de survie
                    if self.__dico_etat[x,y] not in self.regles["survie"]:
                        self.__dico_case[x,y] = 0
                #si la cellule est morte
                else:
                    #naissance si dans la regle de naissance
                    if self.__dico_etat[x,y] in self.regles["naissance"]:
                        self.__dico_case[x,y] = 1
                u+=1
            t+=1


    #sauvegarder une grille    
    def save(self):
        txt=""
        v=0
        while v!= self.height/self.cellSize:
            w=0
            while w!= self.width/self.cellSize:
                x=w*self.cellSize
                y=v*self.cellSize
                txt+=str(self.__dico_case[x,y])
                w+=1
            txt=txt+"\n"
            v+=1   
        i=0
        #supprime respectivement la premiere ligne si elle ne contient aucune cellule vivante
        while txt.splitlines()[0].count('1')==0:
            txt='\n'.join(txt.split('\n')[1:])
        #supprime respectivement la derniere ligne si elle ne contient aucune cellule vivante
        while txt.splitlines()[-1].count('1')==0:
            txt=txt[:txt.rfind('\n')]
        #fonction de suppression de colonnes
        def RemoveEmptyCols(txt,direction=0):
            list = txt.splitlines()
            tab=[]
            for elem in list:
                if direction==0:
                    n=elem.find('1')
                    if n!=-1:
                        tab.append(n)
                else:
                    tab.append(len(elem)-elem.rfind('1')-1)
            nbLines=min(tab)
            if nbLines>0:
                i=len(list)-1
                while i>=0:
                    s=list[i]
                    if direction==0:
                        s=s[nbLines:]
                    else:
                        s=s[:-nbLines]
                    list[i]=s
                    i-=1           
            txt='\n'.join(list)
            return txt        
        #supprime les premieres colonnes si elles ne contiennent aucune cellule vivante
        txt=RemoveEmptyCols(txt)
        #supprime les dernieres colonnes si elles ne contiennent aucune cellule vivante
        txt=RemoveEmptyCols(txt,1)
        return txt
    
    #compte le nombre de cellules vivantes
    def population(self):
        n=0
        v=0        
        while v!= self.height/self.cellSize:
            w=0
            while w!= self.width/self.cellSize:
                x=w*self.cellSize
                y=v*self.cellSize
                if self.__dico_case[x,y]==1:
                    n+=1
                w+=1
            v+=1
        return n
    
    def canon(self, x, y): #fonction dessinant le canon de Bill Gosper
        array = self.loadPattern(Constants.GOSPER, x, y)
        
    def planeur(self, x, y): #fonction dessinant le planeur
        array = self.loadPattern(Constants.PLANEUR, x, y)
        
    def replicateur(self, x, y):
        #fonction dessinant le replicateur
        array = self.loadPattern(Constants.REPLICATEUR, x, y)
        
    def raz(self):
        i=0
        while i!= self.width/ self.cellSize: #assigne une valeur 0(morte) a chaque coordonnees(cellules)
            j=0
            while j!= self.height/ self.cellSize:
                x=i* self.cellSize
                y=j* self.cellSize
                self.__dico_case[x,y] = 0
                j+=1
            i+=1
    
    
    @property
    def dicoCase(self):
        return self.__dico_case
    
    @property
    def dicoState(self):
        return self.__dico_etat
    
    def loadPattern(self, value, x, y):
        if value==Constants.GOSPER:
            filename = "patterns/gosper.txt"
        elif value==Constants.PLANEUR:
            filename = "patterns/planeur.txt"
        elif value == Constants.REPLICATEUR:
            filename = "patterns/replicateur.txt"
        else : #default
            filename = "patterns/gosper.txt"
        
        with open(filename, "r") as pattern:      
            col = x
            line = y
            char = pattern.read(1)
            while char:
                if(char != '\n'):
                    self.__dico_case[col, line] = int(char)
                    col = col + self.cellSize
                else:
                    line = line + self.cellSize
                    col = x
                char = pattern.read(1)
                
    
    def ConfigCenteredfPosition(self, filename):
        with open(filename, "r") as configfile:         
            txt = configfile.read()
            nb_char = txt.count('0')+txt.count('1') #nombre de caracteres
            configfile.seek(0, 0)
            nb_col = len(configfile.readline())-1 #nombre de colonnes (de caracteres de la premiere ligne)
            nb_lines = nb_char / nb_col #nombre de lignes
        configfile.closed
        x = int((self.width/self.cellSize-nb_col)/2)*self.cellSize
        y = int((self.height/self.cellSize-nb_lines)/2)*self.cellSize
        alertSize = False
        if x<0:
            x=0
            alertSize=True
        if y<0:
            y=0
            alertSize=True
        return x,y,alertSize
    
    def loadConfigPerso(self, filename, x, y):         
        with open(filename, "r") as configfile:
            col = x
            line = y
            char = configfile.read(1)
            while char:
                if(char != '\n'):
                    self.__dico_case[col, line] = int(char)
                    col = col + self.cellSize
                else:
                    line = line + self.cellSize
                    col = x
                char = configfile.read(1)