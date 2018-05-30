import ConfigUtils
import Constants

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
                if x==0 and y==0: #coin en haut a� gauche
                    compt_viv=0
                    if self.__dico_case[x, y + self.cellSize] == 1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y+self.cellSize]==1:
                        compt_viv+=1
                    self.__dico_etat[x, y]=compt_viv
                elif x==0 and y==int(self.height-self.cellSize): #coin en bas a� gauche
                    compt_viv=0
                    if self.__dico_case[x, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y-self.cellSize]==1:
                        compt_viv+=1
                    if self.__dico_case[x+self.cellSize, y]==1:
                        compt_viv+=1
                    self.__dico_etat[x, y]=compt_viv
                elif x==int(self.width-self.cellSize) and y==0: #coin en haut a� droite
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
        #supprime r�p�titivement la premi�re ligne si elle ne contient aucune cellule vivante
        while txt.splitlines()[0].count('1')==0:
            txt='\n'.join(txt.split('\n')[1:])
        #supprime r�p�titivement la derni�re ligne si elle ne contient aucune cellule vivante
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
        #supprime les premi�res colonnes si elles ne contiennent aucune cellule vivante
        txt=RemoveEmptyCols(txt)
        #supprime les derni�res colonnes si elles ne contiennent aucune cellule vivante
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
    
    def canon(self): #fonction dessinant le canon a planeur de Bill Gosper
        #array = ConfigUtils.loadPattern()   
        array = self.loadPattern(Constants.GOSPER)
        
    def planeur(self): #fonction dessinant le canon a planeur de Bill Gosper
        #array = ConfigUtils.loadPattern()   
        array = self.loadPattern(Constants.PLANEUR)        
    
    
    @property
    def dicoCase(self):
        return self.__dico_case  
    
    @property
    def dicoState(self):
        return self.__dico_etat
    
    
    def loadPattern(self, value):
        
        if value==Constants.GOSPER:   
            filename = "patterns/gosper.txt"
        elif value==Constants.PLANEUR:
            filename = "patterns/planeur.txt"
        else : #default
            filename = "patterns/gosper.txt"
        
        with open(filename, "r") as pattern:      
            #pattern.close()
            col = 20
            line = 20
            char = pattern.read(1)
            while char:
                if(char != '\n'):
                    self.__dico_case[col*self.cellSize, line*self.cellSize]=int(char)
                    col=col +1
                else:
                    line= line +1
                    col=0
                char = pattern.read(1)      