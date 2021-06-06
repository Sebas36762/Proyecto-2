about="""

    País de producción Costa Rica
    Tecnológico de Costa Rica, ingeniería en Computadores
    Proyecto 1: From mars to saturn, Año 2021, Grupo 02
    Profesor Milton Villegas Lemus
    Versión del programa 1.0
    Autores: Angelo Fabian Ceciliano Ortega, Sebastian Chaves Ruiz
    Autores de algunos módulos utilizados: José Fernando Morales
    
    

    """
#caca 
from tkinter import *
import vlc 
from os import path
#from time import Thread
import glob 
#import random 

#FLAG para cerrar hilos y parar procesos
ACTIVE=TRUE

#Ventana principalds
Space_p = Tk()
Space_p.title('SPACE INVADER')
Space_p.minsize(800,800)
Space_p.resizable(width=NO, height=NO)

 
  
#Ventana de seleccion de niveles

     

    

def credits():
    global ACTIVE,Space_p
    Space_p.withdraw()
    credit = Toplevel()
    credit.title('About')
    credit.minsize(800,800)
    credit.resizable(width=NO,height=NO)


    C_credit= Canvas(credit,bg='White',width=800,height=800)
    
    C_credit.fonde= img_load('credist.png')
    fonde = C_credit.create_image(0,0, anchor=NW, image=C_credit.fonde)

    C_credit.create_text(0,0,text=about,fill='Yellow',font='Terminal', anchor=NW)
    C_credit.place(x=0,y=0)


    def close_credits():
        global Space_p,ACTIVE
        ACTIVE=False
        credit.withdraw()
        Space_p.deiconify()  
    B_close=Button(credit,bg='Red',text='Back',command=close_credits)
    B_close.place(x=0,y=0)
    
    credit.protocol('WM_DELETE_WINDOW',close_credits)

def highscore():
    global ACTIVE,Space_p
    Space_p.withdraw()
    score = Toplevel()
    score.title('High Score')
    score.minsize(800,800)
    score.resizable(width=NO,height=NO)
   
    C_score= Canvas(score,bg='White',width=800,height=800)
    C_score.place(x=0,y=0)
    C_score.fonde= img_load('score.png')
    fonde = C_score.create_image(0,0, anchor=NW, image=C_score.fonde)
    

    def close_score():
        global Space_p,ACTIVE
        ACTIVE=False
        score.withdraw()
        Space_p.deiconify()
        
    B_close=Button(score,bg='Red',text='Back',command=close_score)
    B_close.place(x=0,y=0)

def level1():    
    global ACTIVE 
    Space_p.withdraw()
    
    levelone = Toplevel()
    levelone.title('1 level')
    levelone.minsize(800,800)
    levelone.resizable(width=NO,height=NO)

    C_level1 = Canvas(levelone,bg='White',width=800,height=800)
    C_level1.place(x=0,y=0)

    C_level1.ship = img_load('ship_player\\tile001.png')
    ship = C_level1.create_image(350,750, anchor=NW, image=C_level1.ship)
    
    if(ACTIVE):
        def move_ship(event):
            if event.keysym =='Up':
                if C_level1.coords(ship)[1]>0:
                    C_level1.move(ship,0,-15)
            elif event.keysym =='Down':
                if C_level1.coords(ship)[1]<780:
                    C_level1.move(ship,0,15)
            elif event.keysym =='Left':
                if C_level1.coords(ship)[0]>30:
                    C_level1.move(ship,-15,0)
            elif event.keysym =='Right':
                if C_level1.coords(ship)[0]<780:
                     C_level1.move(ship,15,0)
        


        C_level1.bind_all('<KeyPress-Up>',move_ship)
        C_level1.bind_all('<KeyPress-Down>',move_ship)
        C_level1.bind_all('<KeyPress-Left>',move_ship)
        C_level1.bind_all('<KeyPress-Right>',move_ship)
        #C_level1.bind_all('<KeyRelease-space>',fire)
    

    #####CERRAR VENTANA##############
    def closelevel1():
        global ACTIVE
        ACTIVE=False 
        stop_sound()
        Space_p.deiconify()
        levelone.withdraw()
    #####Botones########
    B_closelevels = Button(levelone,bg='Red',text='Back and Close',font='Terminal',command=closelevel1)
    B_closelevels.place(x=0,y=0)
    levelone.protocol('WM_DELETE_WINDOW',closelevel1)

def level2():
    Space_p.withdraw()
    leveltwo = Toplevel()
    leveltwo.title('2 level')
    leveltwo.minsize(800,800)
    leveltwo.resizable(width=NO,height=NO)






    #####CERRAR VENTANA##############
    def closelevel2():
        global ACTIVE
        ACTIVE=False 
        stop_sound()
        Space_p.deiconify()
        leveltwo.withdraw()
    #####Botones########
    B_closelevels = Button(leveltwo,bg='Red',text='Back and Close',font='Terminal',command=closelevel2)
    B_closelevels.place(x=0,y=0)
    leveltwo.protocol('WM_DELETE_WINDOW',closelevel2)



def level3():
    Space_p.withdraw()
    levelthree = Toplevel()
    levelthree.title('3 level')
    levelthree.minsize(800,800)
    levelthree.resizable(width=NO,height=NO)







    #####CERRAR VENTANA##############
    def closelevel3():
        global ACTIVE
        ACTIVE=False 
        stop_sound()
        Space_p.deiconify()
        levelthree.withdraw()
    #####Botones########
    B_closelevels = Button(levelthree,bg='Red',text='Back and Close',font='Terminal',command=closelevel3)
    B_closelevels.place(x=0,y=0)
    levelthree.protocol('WM_DELETE_WINDOW',closelevel3)


















#Funciones de apoyo
#Cargar imagenes con path
#cargar audio con vlc
def img_load(name):
    direction= path.join('assests',name)
    img= PhotoImage(file=direction)
    return img 
############################################
#############################################
##Reproductor de sonido###VLC################
sound_player = vlc.MediaPlayer()
def sound_load(name): #Ruta del .MP3
    return path.join('assets\\music',name)
def player_music(MP3): # Reproductor de Musica
    global sound_player
    stop_sound()
    sound_player = vlc.MediaPlayer(MP3)
    sound_player.audio_set_volume(40)
    sound_player.play()
def player_fx(MP3): #Reproductor de efectos 
    vlc.MediaPlayer(MP3).play()
def stop_sound(): #Para sonidos, aunque se usa para parar la musica, los efectos se paran solos. 
    global sound_player
    if(isinstance(sound_player,vlc.MediaPlayer)):
        sound_player.stop()
################################
#Funcion para cerrar el programa
def close():
    global Space_p
    stop_sound()
    ACTIVE=False
    Space_p.destroy()

###############################
###############################



#########Canvas pantalla Principal###################
P_space= Canvas(Space_p,bg='White',width=800,height=800)
P_space.place(x=0,y=0)
P_space.fonde= img_load('fonde.png')
fonde = P_space.create_image(0,0, anchor=NW, image=P_space.fonde)
#Botones
#Botones pantalla principal
ship= img_load('ship_player\\tile001.png')

B_credits=Button(Space_p,bg='#41036e',text='Credits',font='Terminal',command=credits)
B_credits.place(x=0,y=770)
B_highscore=Button(Space_p,bg='#41036e',text='Score',font='Terminal',command=highscore)
B_highscore.place(x=730,y=770)



B_closegame=Button(Space_p,bg='#870601',text='X',font='Terminal',command=close)
B_closegame.place(x=770,y=0)

#Botones pantalla principal niveles 

B_level1= Button(Space_p,bg='#41036e',text='Level 1',font='Terminal',command=level1) 
B_level1.place(x=350,y=400)
B_level2= Button(Space_p,bg='#41036e',text='Level 2',font='Terminal',command=level2)
B_level2.place(x=350,y=450)
B_level3= Button(Space_p,bg='#41036e',text='Level 3',font='Terminal',command=level3)
B_level3.place(x=350,y=500)


Space_p.protocol('WM_DELETE_WINDOW',close)
Space_p.mainloop() 














