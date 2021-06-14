about="""

    País de producción Costa Rica
    Tecnológico de Costa , ingeniería en Computadores
    Proyecto 1: From mars to saturn, Año 2021, Grupo 02
    Profesor Milton Villegas Lemus
    Versión del programa 1.0
    Autores: Angelo Fabian Ceciliano Ortega, Sebastian Chaves Ruiz
    Autores de algunos módulos utilizados: José Fernando Morales    
    """

import time
from tkinter import *
from typing import get_origin
import vlc 
from os import path
from threading import Thread
import glob 
import random 
from time import sleep

#FLAG para cerrar hilos y parar procesos
ACTIVE=TRUE

Score=0
ship_life=50

#Ventana principal
Space_p = Tk()
Space_p.title('SPACE INVADER')
Space_p.minsize(800,800)
Space_p.resizable(width=NO, height=NO)
##Reproductor de sonido###VLC################
sound_player = vlc.MediaPlayer()
#########Canvas pantalla Principal###################
P_space= Canvas(Space_p,bg='White',width=800,height=800)
P_space.place(x=0,y=0)


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
def img_load(name):
    direction= path.join('assests',name)
    img= PhotoImage(file=direction)
    return img
################################
def load_sprite(patron):
        frames = glob.glob('assests\\ship_player\\' + patron)
        frames.sort()
        return load_Simage(frames,[])

def load_Simage(input,list_result):
    if(input == []):
        return list_result
    else:
        list_result.append(PhotoImage(file=input[0]))
    return load_Simage(input[1:],list_result) 

P_space.fonde= img_load('fonde.png')
fonde = P_space.create_image(0,0, anchor=NW, image=P_space.fonde)
  
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
    
E_Nombre = Entry(Space_p,font=("Comic Sans MS",10))
E_Nombre.place(x=115,y=400)

def Validar1():#Se verifica que la entrada tenga algun texto
    global E_Nombre
    nombre_usuario = E_Nombre.get()
    if (nombre_usuario!=""):
        return level1()


        
def level1():
    global ACTIVE, Score, ship_life
    ship_life
    Score=0    
    ACTIVE=True 
    Space_p.withdraw()
    
    levelone = Toplevel()
    levelone.title('1 level')
    levelone.minsize(800,800)
    levelone.resizable(width=NO,height=NO)

    C_level1 = Canvas(levelone,bg='White',width=1700,height=1700)
    C_level1.place(x=0,y=0)
    C_level1.fondo = img_load('Fondo1.png')
    Fondo1 = C_level1.create_image(0,0,anchor=NW, image=C_level1.fondo)

    def Reloj(seg,minu):#Se crea un reloj con recursividad para determinar el tiempo de la partida
        if (ACTIVE):
            sleep(1)#Cada segundo, le suma 1 a la variable seg
            seg+=1
            if seg==59:#Si la variable seg es 60, la variable minu le suma 1
                minu+=1
                seg=0
            Reloj_L.config(text="Tiempo:"+str(minu)+":"+str(seg))
            Reloj(seg,minu)
    Thread(target=Reloj,args=(0,0)).start()

    Reloj_L= Label(levelone, text="Tiempo:0:0",bg="#161d2f", fg="white")
    Reloj_L.place(x=730, y=60)

    images= load_sprite('tile*.png')
    ship = C_level1.create_image(350,700, tags='ship')
    
    def recursive_animation(i):
        nonlocal images
        if(i==3):
            i=0
        if(ACTIVE==True):
            C_level1.itemconfig('ship',image=images[i])
            time.sleep(0.1)
            Thread(target=recursive_animation,args=(i+1,)).start()
    Thread(target=recursive_animation,args=(0,)).start()    

    def move_ship(event):
        if event.keysym =='Up':
            if C_level1.coords(ship)[1]>0:
                C_level1.move(ship,0,-13)
        elif event.keysym =='Down':
            if C_level1.coords(ship)[1]<780:
                C_level1.move(ship,0,13)
        elif event.keysym =='Left':
            if C_level1.coords(ship)[0]>30:
                C_level1.move(ship,-13,0)
        elif event.keysym =='Right':
            if C_level1.coords(ship)[0]<780:
                C_level1.move(ship,13,0)

    C_level1.bind_all('<KeyPress-Up>',move_ship)
    C_level1.bind_all('<KeyPress-Down>',move_ship)
    C_level1.bind_all('<KeyPress-Left>',move_ship)
    C_level1.bind_all('<KeyPress-Right>',move_ship)
    
    C_level1.rock= img_load('rock.png')
    rock00 = C_level1.create_image(random.randint(100,500),random.randint(-10,0),anchor=NW,image=C_level1.rock)
    rock01= C_level1.create_image(random.randint(-10,0),random.randint(800,850), anchor=NW,image=C_level1.rock)
    rock02 = C_level1.create_image(random.randint(800,850),random.randint(0,800), anchor=NW,image=C_level1.rock)
    

    def move_rockx(rock,x):
        Cor_rock= C_level1.coords(rock)
        if(ACTIVE):
            if Cor_rock[0]>=700:
                C_level1.move(rock,-10,0)
                C_level1.after(30,move_rockx,rock,-10)
            elif Cor_rock[0]<2:
                C_level1.move(rock,10,0)
                C_level1.after(30,move_rockx,rock,10)   
            else:
                C_level1.move(rock,x,0)
                C_level1.after(30,move_rockx,rock,x)
    
    
    def move_rocky(rock,x):
         Cor_rock= C_level1.coords(rock)
         if(ACTIVE):
            if Cor_rock[1]>780:
                C_level1.move(rock,0,-10)  
                C_level1.after(30,move_rocky,rock,-10)
            elif Cor_rock[1]<0:
                C_level1.move(rock,0,10)
                C_level1.after(30,move_rocky,rock,10)
            else:
                C_level1.move(rock,0,x)
                C_level1.after(30,move_rocky,rock,x)
    
    
    Thread(target=move_rockx,args=(rock00,10,)).start()
    Thread(target=move_rocky,args=(rock00,10,)).start()

    Thread(target=move_rockx,args=(rock01,10,)).start()
    Thread(target=move_rocky,args=(rock01,10,)).start()

    Thread(target=move_rockx,args=(rock02,10,)).start()
    Thread(target=move_rocky,args=(rock02,10,)).start()


   









    Nave_life_l1 = Label(levelone, text="❤:" + str(ship_life),bg="#161d2f", fg="white")
    Nave_life_l1.place(x=25, y=700)
    Score_L = Label(levelone, text="Puntos:" + str(Score),bg="#161d2f", fg="white")
    Score_L.place(x=740, y=10)

    #####CERRAR VENTANA##############
    def closelevel1():
        global ACTIVE
        ACTIVE=False 
        stop_sound()
        Space_p.deiconify()
        levelone.destroy()
    #####Botones########
    B_closelevels = Button(levelone,bg='Red',text='Back and Close',font='Terminal',command=closelevel1)
    B_closelevels.place(x=0,y=0)
    levelone.protocol('WM_DELETE_WINDOW',closelevel1)





#Funcion para cerrar el programa
def close():
    global Space_p
    stop_sound()
    ACTIVE=False
    Space_p.destroy()

###############################
###############################






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

B_level1= Button(Space_p,bg='#41036e',text='Level 1',font='Terminal',command=Validar1) 
B_level1.place(x=350,y=400)
B_level2= Button(Space_p,bg='#41036e',text='Level 2',font='Terminal',command="level2")
B_level2.place(x=350,y=450)
B_level3= Button(Space_p,bg='#41036e',text='Level 3',font='Terminal',command="level3")
B_level3.place(x=350,y=500)


Space_p.protocol('WM_DELETE_WINDOW',close)
Space_p.mainloop() 














