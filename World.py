import ConfigUtils

class World:
    
    def __init__(self, height, width, cellSize):
        self.height = height
        self.width = width
        self.cellSize = cellSize
        self.__dico_etat = {} #dictionnaire contenant le nombre de cellules vivantes autour de chaque cellule
        self.__dico_case = {} #dictionnaire contenant les coordonnees de chaques cellules et une valeur 0 ou 1 si elles sont respectivement mortes ou vivantes
        
        i=0
        while i!= self.width/ self.cellSize: #assigne une valeur 0(morte) a chaque coordonnees(cellules)
            j=0
            while j!= self.height/ self.cellSize:
                x=i* self.cellSize
                y=j* self.cellSize
                self.__dico_case[x,y]=0
                j+=1
            i+=1        
        
    
    def play(self): #fonction comptant le nombre de cellules vivantes autour de chaque cellule
        v=0
        while v!= self.width/self.cellSize:
            w=0
            while w!= self.height/self.cellSize:
                x=v*self.cellSize
                y=w*self.cellSize
    
                # cas speciaux:
                # les coins
                if x==0 and y==0: #coin en haut a  gauche
                    compt_viv=0
                    if self.__dico_case[x, y + self.cellSize] == 1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y+self.cellSize]==1:
                        compt_viv+=1
                    self.__dico_etat[x, y]=compt_viv
                elif x==0 and y==int(self.height-self.cellSize): #coin en bas a  gauche
                    compt_viv=0
                    if self.__dico_case[x, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y]==1:
                        compt_viv+=1
                    self.__dico_etat[x, y]=compt_viv
                elif x==int(self.width-self.cellSize) and y==0: #coin en haut a  droite
                    compt_viv=0
                    if self.__dico_case[x-self.cellSize, y]==1:
                        compt_viv+=1
                    if self.__dico_case[x-self.cellSize, y+self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x, y+self.cellSize]==1:
                        compt_viv+=1
                    self.__dico_etat[x, y]=compt_viv
                elif x==int(self.width-self.cellSize) and y==int(self.height-self.cellSize): #coin en bas Ã  droite
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
    
    def canon(self): #fonction dessinant le canon a planeur de Bill Gosper
        #array = ConfigUtils.loadPattern()   
        array = self.loadPattern()
    
    
    @property
    def dicoCase(self):
        return self.__dico_case  
    
    @property
    def dicoState(self):
        return self.__dico_etat
    
    
    def loadPattern(self):
        #TODO prendre en parametre le nom du fichier
        with open("patterns/planeur.txt", "r") as pattern:      
            #pattern.close()
            col = 0
            line = 0
            char = pattern.read(1)
            while char:
                if(char != '\n'):
                    self.__dico_case[line*self.cellSize,col*self.cellSize]=int(char)
                    col=col +1
                else:
                    line= line +1
                    col=0
                char = pattern.read(1)      