# -*- coding: utf-8 -*-
"""
@author: Amir Mahmoudi
"""
from inspect import currentframe, getframeinfo

class Node:  # class to initiate a node from the tree
    def __init__(self, plateau,parent=None):
        self.plateau=plateau 
        self.liste=[]          
        self.eval=self.utility()
        if parent is None:
            self.parent=None
        else:
            self.parent=parent
        
    def __str__(self):
        str=""
        for i in range(3):
            for j in range(3):
                if self.plateau[i][j]=="":
                    str+=" "
                str+=self.plateau[i][j]
                str+=" "
                
            
            str+="\n"
        return str
    def IsTerminal(self):  #this function checks if our board game is terminal
        
        if(sum(1 if(self.plateau[i][i])=="x" else 0 for i in range(3))==3):
            return True
        
        elif(sum(1 if(self.plateau[i][i])=="o" else 0 for i in range(3))==3):
            return True
        
        elif(sum(1 if(self.plateau[2-i][i])=="x" else 0 for i in range(3))==3):
            return True
        
        elif(sum(1 if(self.plateau[2-i][i])=="o" else 0 for i in range(3))==3):
            return True
        
        for j in range(3):
            if(sum(1 if(self.plateau[i][j])=="x" else 0 for i in range(3))==3):
               return True
           
            elif(sum(1 if(self.plateau[j][i])=="x" else 0 for i in range(3))==3):
                return True            
            
        for j in range(3):
            if(sum(1 if(self.plateau[i][j])=="o" else 0 for i in range(3))==3):
                return True
            
            elif(sum(1 if(self.plateau[j][i])=="o" else 0 for i in range(3))==3):
                return True
        var=0
        for i in range(3):
            for j in range(3):
                if self.plateau[i][j]=="x" or self.plateau[i][j]=="o":
                    var=var+1
        if var==9:
            return True
        return False
    
    def utility(self):  #Associate a value to the final board game
        if(sum(1 if(self.plateau[i][i])=="x" else 0 for i in range(3))==3):
            return 1
        
        elif(sum(1 if(self.plateau[i][i])=="o" else 0 for i in range(3))==3):
            return -1
        
        elif(sum(1 if(self.plateau[2-i][i])=="x" else 0 for i in range(3))==3):
            return 1
        
        elif(sum(1 if(self.plateau[2-i][i])=="o" else 0 for i in range(3))==3):
            return -1
        
        for j in range(3):
            if(sum(1 if(self.plateau[i][j])=="x" else 0 for i in range(3))==3):
               return 1
           
            elif(sum(1 if(self.plateau[j][i])=="x" else 0 for i in range(3))==3):
                return 1           
            
        for j in range(3):
            if(sum(1 if(self.plateau[i][j])=="o" else 0 for i in range(3))==3):
                return -1
            
            elif(sum(1 if(self.plateau[j][i])=="o" else 0 for i in range(3))==3):
                return -1
            
        return 0
    
    def action(self):#This function will create the childs of the actual node
        
        croix=0
        circle=0
        for i in range (3):
            for j in range(3):
                if self.plateau[i][j]=="x":
                    croix=croix+1
                if self.plateau[i][j]=="o":
                    circle=circle+1
        if croix==circle:     # We decided that the cross will always start first
            for i in range(3):
                for j in range (3):
                    if self.plateau[i][j]=="":
                        temp=[]
                        for k in range(3):
                            temp.append(list(self.plateau[k]))
                        temp[i][j]="x"
                        self.liste.append(Node(temp,self))
        else:
            for i in range(3):
                for j in range (3):
                    if self.plateau[i][j]=="":
                        temp=[]
                        for k in range(3):
                            temp.append(list(self.plateau[k]))                  
                        temp[i][j]="o"
                        self.liste.append(Node(temp,self))
        
    
    
    def Turn(self):  #Check which player have to play
        croix=0
        circle=0
        for i in range (3):
            for j in range(3):
                if self.plateau[i][j]=="x":
                    croix=croix+1
                if self.plateau[i][j]=="o":
                    circle=circle+1
        if croix==circle:
            return 1
        else:
            return 0
    
def Alpha_Beta_Search(node):
    
    if node.Turn()==1:
        v=Max_Value(-600000,600000,node)
    else:
        v=Min_Value(-600000,600000,node)
            
    return v  #v is the value associate to the better child of the actual node

def Max_Value(a,b,node):
    if node.IsTerminal():
        u=node.utility()
        if node.parent is not None:
            node=node.parent
        else:
            print("End of the game")
            
        return u
    v=-600000
    node.action()
    for i in node.liste:
        node=i
        v=max(v,Min_Value(a,b,node))
        node.eval=v
        if v>=b :
            if node.parent is not None:
                node=node.parent
            return v
        a=max(a,v)
    if node.parent is not None:
            node=node.parent
    return v

def Min_Value(a,b,node):
    if node.IsTerminal():
        u=node.utility()
        if node.parent is not None:
            node=node.parent  
        else:
            print("End of the game")
        return u
    v=600000
    node.action()
    for i in node.liste:
        node=i
        v=min(v,Max_Value(a,b,node))
        node.eval=v
       
        if v<=a :
            if node.parent is not None:
                node=node.parent
            return v
        b=min(b,v)
    if node.parent is not None:
            node=node.parent
    return v


def OrdivsOrdi(): #The function for a IAvsIA match
    jeu=[["","",""],["","",""],["","",""]]
    node=Node(jeu)
    print(node)
    z=0
    fini=False
    while z<9 and fini==False:
       found=False
       i=0
       v=Alpha_Beta_Search(node)
       while i<len(node.liste) and found==False:
         
          if v==node.liste[i].eval:
             
              print("actual board game: ")
              print(node.liste[i])
              node=node.liste[i]
              node.parent=None 
              found=True
          else:
              i=i+1
            
       z+=1
       if node.IsTerminal():
          fini=True

def OrdivsHumain():#IA vs Human and the IA starts
    jeu=[["","",""],["","",""],["","",""]]
    node=Node(jeu)   
    print(node)   
    z=0
    fini=False
    while z<9 and fini==False:
       if z%2==0:
           found=False
           i=0
           v=Alpha_Beta_Search(node)
           while i<len(node.liste) and found==False:
               if v==node.liste[i].eval:
                   print("actual board game: ")
                   print(node.liste[i])
                   node=node.liste[i]
                   found=True
               else:
                   i=i+1
           node.parent=None           
          
       else:
           abscisse=3
           ordonnee=3
           while ((abscisse!=2 and abscisse!=1 and abscisse!=0 ) or (ordonnee!=2 and ordonnee!=1 and ordonnee!=0)):
               abscisse= int(input("select a row (0 to 2)"))
               ordonnee= int(input("Select a column (0 to 2)"))
               plat=[]
               for k in range(3):
                  plat.append(list(node.plateau[k]))
               if abscisse<3 and ordonnee<3 and abscisse>-1 and ordonnee>-1:
                   if plat[abscisse][ordonnee]=="" :
                       plat[abscisse][ordonnee]="o"
                   else:
                       abscisse=3
                       ordonnee=3
           node.action()  
           for i in node.liste:
               if i.plateau==plat:
                   node=i
               
           
       z+=1
       if node.IsTerminal():
           fini=True
           
def HumainvsOrdi(): #Human vs IA and Human starts
    jeu=[["","",""],["","",""],["","",""]]
    node=Node(jeu)   
    print(node)   
    z=0
    fini=False
    while z<9 and fini==False:
       if z%2==1:
           found=False
           i=0
           v=Alpha_Beta_Search(node)
           while i<len(node.liste) and found==False:
               if v==node.liste[i].eval:
                   print("grille actuelle: ")
                   print(node.liste[i])
                   node=node.liste[i]
                   found=True
               else:
                   i=i+1
           node.parent=None           
          
       else:
           abscisse=3
           ordonnee=3
           while ((abscisse!=2 and abscisse!=1 and abscisse!=0 ) or (ordonnee!=2 and ordonnee!=1 and ordonnee!=0)):
               abscisse= int(input("select a row (0 to 2)"))
               ordonnee= int(input("Select a column (0 to 2)"))
               plat=[]
               for k in range(3):
                  plat.append(list(node.plateau[k]))
               if abscisse<3 and ordonnee<3 and abscisse>-1 and ordonnee>-1:
                   if plat[abscisse][ordonnee]=="" :
                       plat[abscisse][ordonnee]="x"
                   else:
                       abscisse=3
                       ordonnee=3
           node.action()  
           for i in node.liste:
               if i.plateau==plat:
                   node=i
               
       z+=1
       if node.IsTerminal():
           fini=True
           
      
#Main code to select the configuration that we want"
selection=int(input("Select the game : IAVsIA(1) HumanVsIA(2)"))
if selection == 1:
    OrdivsOrdi()
if selection ==2:
    selection=int(input("Do you want to start ? (1) IA start ?(2)"))
    if selection == 1:
        HumainvsOrdi()
    if selection == 2:
        OrdivsHumain()
print("end of the game")
        
        
        
        
        
        
        
        
        
        
        
        
        