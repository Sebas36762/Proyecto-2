about="""

    País de producción Costa Rica
    Tecnológico de Costa Rica, ingeniería en Computadores
    Proyecto 1: From mars to saturn, Año 2021, Grupo 02
    Profesor Milton Villegas Lemus
    Versión del programa 1.0
    Autores: Angelo Fabian Ceciliano Ortega, Sebastian Chaves Ruiz
    Autores de algunos módulos utilizados: José Fernando Morales    
    """

from ctypes import create_unicode_buffer
import time
from tkinter import *
from typing import get_origin
import vlc 
from os import path
from threading import Thread, ThreadError
import glob 
import random 
from time import sleep

#FLAG para cerrar hilos y parar procesos
ACTIVE=TRUE

#Ventana principal
Space_p = Tk()
Space_p.title('SPACE INVADER')
Space_p.minsize(800,800)
Space_p.resizable(width=NO, height=NO)
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
    ACTIVE=True 
    Space_p.withdraw()
    
    levelone = Toplevel()
    levelone.title('1 level')
    levelone.minsize(800,800)
    levelone.resizable(width=NO,height=NO)

    C_level1 = Canvas(levelone,bg='White',width=800,height=800)
    C_level1.place(x=0,y=0)

    

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
    #C_level1.bind_all('<KeyRelease-space>',fire)




    C_level1.rock0 = img_load('rock.png')
    C_level1.rock1 = img_load('rock.png')
    

    
    
  
    """
    def move_rockx(Rock):
        Cor_rock= C_level1.coords(Rock)
        if(ACTIVE):
            if Cor_rock[0]>=700:
                C_level1.move(Rock,-5,0)
                C_level1.after(15,move_rockx,-5)
            elif Cor_rock[0]<2:
                C_level1.move(Rock,5,0)
                C_level1.after(15,move_rockx,5)   
            else:
                C_level1.move(Rock,Rock,0)
                C_level1.after(15,move_rockx,Rock)
    Thread(target=move_rockx,args=(5,)).start()
    
    def move_rocky(Rock):
         Cor_rock= C_level1.coords(rock00)
         if(ACTIVE):
            if Cor_rock[1]>780:
                C_level1.move(rock00,0,-5)  
                C_level1.after(15,move_rocky,-5)
            elif Cor_rock[1]<0:
                C_level1.move(rock00,0,5)
                C_level1.after(15,move_rocky,5)
            else:
                C_level1.move(rock00,0,Rock)
                C_level1.after(15,move_rocky,Rock)
    Thread(target=move_rocky,args=(5,)).start()
    """
    def selector():
        if(ACTIVE):
            sleep(0.5)
            rocks_s()
            sleep(0,7)
            selector()
    Thread(target=selector).start()


    def move_rock(rock):
        coords_rock= C_level1.coords(rock)
        if(ACTIVE):
            if coords_rock[0]>830 or coords_rock[0]<-15 or coords_rock[1]>830 or coords_rock[1]<-15:
                C_level1.delete(rock)
        
        else:
            C_level1.move(rock,5,5)
            C_level1.after(10,move_rock,rock)
    
    def rocks_s():
        if(ACTIVE):
            coords = C_level1.coords(0,0)
            rock1 = C_level1.create_image(x=0,y=800, anchor=NW, image=C_level1.rock0) 
            rock2 = C_level1.create_image(x=0,y=0,anchor=NW,image=C_level1.rock1)
            Thread(target=move_rock,args=(rock1,)).start()
            Thread(target=move_rock,args=(rock2,)).start()
            
    
    
    """
    Bullet = cargar_img2('Bullet2.png')

    Flag2=True
    def temporizador2():
        nonlocal Flag2
        if Flag2 == True:
            time.sleep(1)
            DisparoJefe()
            temporizador2()
    Thread(target = temporizador2).start() 

    def MovimientoD(Bala):
        global Boss_life, reproducir_fx, Score, Nave_life, FlagA
        Bala_box= Canv_Pantalla2.bbox(Bala)
        Aliadobox= Canv_Pantalla2.bbox(Aliado_Canv)
        if FlagA==True:
            if Canv_Pantalla2.coords(Bala)[1]>700: #Limite hasta donde llega la bala
                Canv_Pantalla2.delete(Bala)
            elif Aliadobox[0]<Bala_box[2] and Aliadobox[2]>Bala_box[0] and Aliadobox[1]<Bala_box[3]<Aliadobox[3] and Aliadobox[3] > Aliadobox[1]:
                Canv_Pantalla2.delete(Bala)
                if Nave_life!=0:
                    Nave_life-=3
                    Nave_life_l2.config(text="❤:" + str(Nave_life))
                if Nave_life==2:
                    Nave_life-=2
                    Nave_life_l2.config(text="❤:" + str(Nave_life))
            else:
                Canv_Pantalla2.move(Bala,0,3) #El disparo avanza en el eje Y
                Canv_Pantalla2.after(15,MovimientoD,Bala)

    def DisparoJefe():
        global FlagA
        if FlagA==True:
            coords= Canv_Pantalla2.coords(Jefe2_E)
            Bala1 = Canv_Pantalla2.create_image(coords[0]+80,coords[1]-55,anchor=NW,image=Bullet)
            Bala2 = Canv_Pantalla2.create_image(coords[0]-100,coords[1]-55,anchor=NW,image=Bullet)
            Bala3 = Canv_Pantalla2.create_image(coords[0]-35,coords[1]+50,anchor=NW,image=Bullet)
            reproducir_fx(cargarMP3('SE_01.wav'))
            Thread(target=MovimientoD, args=(Bala1,)).start()
            Thread(target=MovimientoD, args=(Bala2,)).start()
            Thread(target=MovimientoD, args=(Bala3,)).start()
        
       

        """


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
#B_level2= Button(Space_p,bg='#41036e',text='Level 2',font='Terminal',command=#level2)
#B_level2.place(x=350,y=450)
#B_level3= Button(Space_p,bg='#41036e',text='Level 3',font='Terminal',command=#level3)
#B_level3.place(x=350,y=500)


Space_p.protocol('WM_DELETE_WINDOW',close)
Space_p.mainloop() 














