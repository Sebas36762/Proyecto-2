about="""

    País de producción Costa Rica
    Tecnológico de Costa , ingeniería en Computadores
    Proyecto 1: From mars to saturn, Año 2021, Grupo 02
    Profesor Milton Villegas Lemus
    Versión del programa 1.0    
    Autores: Angelo Fabian Ceciliano Ortega, Sebastian Chaves Ruiz
    Autores de algunos módulos utilizados: José Fernando Morales    
    """

from tkinter import *
from os import path, write
import glob
import time                             
from time import sleep
import vlc
from threading import Thread, Timer
import random

#FLAG para cerrar hilos y parar procesos
ACTIVE=TRUE

Score=0
ship_life=3

#Ventana principal
Space_p = Tk()
Space_p.title('SPACE INVADER')
Space_p.minsize(800,800)
Space_p.resizable(width=NO, height=NO)
##Reproductor de sonido###VLC################
reproductor=vlc.MediaPlayer()
#########Canvas pantalla Principal###################
P_space= Canvas(Space_p,bg='White',width=800,height=800)
P_space.place(x=0,y=0)


def cargarMP3(nombre):# Cargar la musica en formato Mp3
    return path.join('Música', nombre)#Se carga la ruta donde esta la música
def reproducir_cancion(archivoMP3):
    global reproductor
    reproductor = vlc.MediaPlayer(archivoMP3)
    reproductor.audio_set_volume(30)
    reproductor.play() 

def reproducir_fx(archivoMP3):#Reproductor de música
    vlc.MediaPlayer(archivoMP3).play()

def stop_sound(): #Para sonidos, aunque se usa para parar la musica, los efectos se paran solos. 
    global reproductor
    if(isinstance(reproductor,vlc.MediaPlayer)):
        reproductor.stop()


reproductor.music = cargarMP3('yu-gi-oh-duel-links-kalin-kessler-theme.mp3')
music = reproducir_cancion(reproductor.music)






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
    global ACTIVE,Space_p, img_load
    Space_p.withdraw()
    credit = Toplevel()
    credit.title('About')
    credit.minsize(800,800)
    credit.resizable(width=NO,height=NO)
    about="""

    País de producción Costa Rica
    Tecnológico de Costa , ingeniería en Computadores
    Proyecto 1: From mars to saturn, Año 2021, Grupo 02
    Profesor Milton Villegas Lemus
    Versión del programa 1.0    
    Autores: Angelo Fabian Ceciliano Ortega, Sebastian Chaves Ruiz
    Autores de algunos módulos utilizados: José Fernando Morales    


        Controles:
                • Flecha Arriba    = Arriba
                • Flecha Abajo     = Abajo
                • Flecha Derecha   = Derecha
                • Flecha Izquierda = Izquierda


        Foto de los Autores:


   Angelo Fabian Ceciliano Oterga       Sebastián Chaves Ruiz
    """


    C_credit= Canvas(credit,bg='White',width=800,height=800)
    
    C_credit.fonde= img_load('credist.png')
    fonde = C_credit.create_image(0,0, anchor=NW, image=C_credit.fonde)

    C_credit.create_text(0,0,text=about,fill='Yellow',font='Terminal', anchor=NW)
    C_credit.place(x=0,y=0)

    Sebas=PhotoImage(file="assests\Sebas.png")
    L_Foto1=Label(credit,image=Sebas).place(x=425,y=375)

    Angelo=PhotoImage(file="assests\Angelo.png")
    L_Foto2=Label(credit,image=Angelo).place(x=40,y=375)



    def close_credits():
        global Space_p,ACTIVE
        ACTIVE=False
        credit.withdraw()
        Space_p.deiconify()  
    B_close=Button(credit,bg='Red',text='Volver',command=close_credits)
    B_close.place(x=0,y=0)
    
    credit.protocol('WM_DELETE_WINDOW',close_credits)
    credit.mainloop()

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
        stop_sound()
        return level1()


        
def level1():
    global ACTIVE, Score, ship_life, E_Nombre, reproductor
    ship_life=3
    Score=0    
    ACTIVE=True 
    Space_p.withdraw()
    nombre_usuario = E_Nombre.get()
    reproductor.music = cargarMP3('yu-gi-oh-duel-links-yuma-astral-theme.mp3')
    music = reproducir_cancion(reproductor.music)
    levelone = Toplevel()
    levelone.title('Level 1')
    levelone.minsize(800,800)
    levelone.resizable(width=NO,height=NO)

    C_level1 = Canvas(levelone,bg='White',width=1700,height=1700)
    C_level1.place(x=0,y=0)
    C_level1.fondo = img_load('Fondo1.png')
    Fondo1 = C_level1.create_image(0,0,anchor=NW, image=C_level1.fondo)
    
    Name_L = Label(levelone,text='Player:'+ str(nombre_usuario),bg="#161d2f",fg="white")
    Name_L.place(x=25,y=750)


    def Reloj(seg,minu):#Se crea un reloj con recursividad para determinar el tiempo de la partida   
        global Score, ACTIVE
        if (ACTIVE):
            sleep(1)#Cada segundo, le suma 1 a la variable seg
            Score+=1
            seg+=1
            if seg==60:#Si la variable seg es 60, la variable minu le suma 1
                minu+=1
                seg=0
                if minu==1:
                    Reloj_L.config(text="Exit")
                    final= Label(levelone, text="You win the level",font='Terminal',bg="#161d2f", fg="white")
                    final.place(x=300, y=250)
                    Reintentar_L=Button(levelone, text='Reintentar',font=("Comic Sans MS",10),command=Reintentar, width=10, height=2,bg="#1e0238",fg="white")
                    Reintentar_L.place(x=360, y=350)
                    Siguiente_L=Button(levelone, text='Siguiente Nivel',font=("Comic Sans MS",10),command=lvl2_win, width=10, height=2,bg="#1e0238",fg="white")
                    Siguiente_L.place(x=360, y=450)
                    ACTIVE=False 
            Reloj_L.config(text="Tiempo:"+str(minu)+":"+str(seg))
            Score_L.config(text="Puntos:" + str(Score))
            Reloj(seg,minu)
        
    Thread(target=Reloj,args=[0,0]).start()

    def lvl2_win():
        stop_sound()
        levelone.destroy()
        return level2()

    images= load_sprite('tile*.png')
    ship = C_level1.create_image(400,400, tags='ship')
    
    def recursive_animation(i):
        nonlocal images
        if(i==3):
            i=0
        if(ACTIVE):
            C_level1.itemconfig('ship',image=images[i])
            time.sleep(0.1)
            Thread(target=recursive_animation,args=(i+1,)).start()
    Thread(target=recursive_animation,args=(0,)).start()    

    def move_ship(event):
        if(ACTIVE):
            if event.keysym =='Up':
                if C_level1.coords(ship)[1]>65:
                    C_level1.move(ship,0,-15)
            elif event.keysym =='Down':
                if C_level1.coords(ship)[1]<754:
                    C_level1.move(ship,0,15)
            elif event.keysym =='Left':
                if C_level1.coords(ship)[0]>43:
                    C_level1.move(ship,-15,0)
            elif event.keysym =='Right':
                if C_level1.coords(ship)[0]<741:
                    C_level1.move(ship,15,0)

    C_level1.bind_all('<KeyPress-Up>',move_ship)
    C_level1.bind_all('<KeyPress-Down>',move_ship)
    C_level1.bind_all('<KeyPress-Left>',move_ship)
    C_level1.bind_all('<KeyPress-Right>',move_ship)
    
    rock= img_load('rock.png')
    Roca0 = C_level1.create_image(random.randint(0,400),random.randint(-10,0),anchor=NW,image=rock)
    Roca1 = C_level1.create_image(random.randint(400,800),random.randint(800,850),anchor=NW,image=rock)
    Roca2 = C_level1.create_image(random.randint(10,500),random.randint(800,850),anchor=NW,image=rock)
    
    Flag2=True
    def temporizador1():
        if(ACTIVE):
            nonlocal Flag2
            if Flag2 == True:
                time.sleep(26)
                Salida_Rocas()
                temporizador1()
    Thread(target = temporizador1).start()

    def move_rockx(rock,x):
        global ship_life
        Cor_rock= C_level1.coords(rock)
        Roca_box= C_level1.bbox(rock)
        Ship_box= C_level1.bbox(ship)
        if(ACTIVE):
            if Cor_rock[0]>=740:
                C_level1.move(rock,-10,0)
                C_level1.after(50,move_rockx,rock,-10)
            elif Cor_rock[0]<-10:
                C_level1.move(rock,10,0)
                C_level1.after(50,move_rockx,rock,10)
            elif Roca_box[0]<Ship_box[2] and Roca_box[2]>Ship_box[0] and Roca_box[1]<Ship_box[3]<Roca_box[3] and Roca_box[3] > Roca_box[1]:
                C_level1.delete(rock)
                reproducir_fx(cargarMP3('golpe.mp3'))
                if ship_life!=0:
                    ship_life-=1
                    Nave_life_l1.config(text="❤:" + str(ship_life))   
            else:
                C_level1.move(rock,x,0)
                C_level1.after(63,move_rockx,rock,x)
    
    
    def move_rocky(rock,y):
        global ship_life
        Cor_rock= C_level1.coords(rock)
        Roca_box= C_level1.bbox(rock)
        Ship_box= C_level1.bbox(ship)
        if(ACTIVE):
            if Cor_rock[1]>740:
                C_level1.move(rock,0,-10)  
                C_level1.after(50,move_rocky,rock,-10)
            elif Cor_rock[1]<-10:
                C_level1.move(rock,0,10)
                C_level1.after(50,move_rocky,rock,10)
            elif Roca_box[0]<Ship_box[2] and Roca_box[2]>Ship_box[0] and Roca_box[1]<Ship_box[3]<Roca_box[3] and Roca_box[3] > Roca_box[1]:
                C_level1.delete(rock)
                reproducir_fx(cargarMP3('golpe.mp3'))
                if ship_life!=0:
                    ship_life-=1
                    Nave_life_l1.config(text="❤:" + str(ship_life)) 
            else:
                C_level1.move(rock,0,y)
                C_level1.after(63,move_rocky,rock,y)
    
    def Salida_Rocas():
        Aleatorio1= random.randint(400,700)
        Aleatorio2= random.randint(700,1100)
        if (ACTIVE):
            coords= C_level1.coords(ship)
            Roca1 = C_level1.create_image(coords[0]+Aleatorio2,coords[1]-Aleatorio1,anchor=NW,image=rock)
            Roca2 = C_level1.create_image(coords[0]-Aleatorio2,coords[1]-Aleatorio2,anchor=NW,image=rock)
            Roca3 = C_level1.create_image(coords[0]-Aleatorio1,coords[1]+Aleatorio1,anchor=NW,image=rock)
            Thread(target=move_rockx,args=(Roca1,10,)).start()
            Thread(target=move_rocky,args=(Roca1,10,)).start()
            Thread(target=move_rockx,args=(Roca2,10,)).start()
            Thread(target=move_rocky,args=(Roca2,10,)).start()
            Thread(target=move_rockx,args=(Roca3,10,)).start()
            Thread(target=move_rocky,args=(Roca3,10,)).start()
            


    Thread(target=move_rockx,args=(Roca0,10,)).start()
    Thread(target=move_rocky,args=(Roca0,10,)).start()
    Thread(target=move_rockx,args=(Roca1,10,)).start()
    Thread(target=move_rocky,args=(Roca1,10,)).start()
    Thread(target=move_rockx,args=(Roca2,10,)).start()
    Thread(target=move_rocky,args=(Roca2,10,)).start()



   




    def Restart1():
        global ship_life,ACTIVE
        if ship_life==0:
            Perdiste_L=Label(levelone,text="Perdiste",font=("Comic Sans MS",15), width=10, height=2,bg="#1e0238",fg="white")
            Perdiste_L.place(x=340, y=200)
            ACTIVE=False
     
            Reintentar_L=Button(levelone, text='Reintentar',font=("Comic Sans MS",10),command=Reintentar, width=10, height=2,bg="#1e0238",fg="white")
            Reintentar_L.place(x=360, y=350)
        else:
            C_level1.after(100,Restart1)
                   
    Thread(target=Restart1).start()

    def Reintentar():
        stop_sound()
        global Score, ship_life
        Score=0
        ship_life=3
        levelone.destroy()
        level1()




    Nave_life_l1 = Label(levelone, text="❤:" + str(ship_life),bg="#161d2f", fg="white")
    Nave_life_l1.place(x=25, y=700)
    Score_L = Label(levelone, text="Puntos:" + str(Score),bg="#161d2f", fg="white")
    Score_L.place(x=740, y=10)
    Reloj_L= Label(levelone, text="Tiempo:0:0",bg="#161d2f", fg="white")
    Reloj_L.place(x=650, y=10)

    #####CERRAR VENTANA##############
    def closelevel1():
        global ACTIVE, Score, ship_life
        ACTIVE=False
        Score=0
        ship_life=3 
        stop_sound()
        Space_p.deiconify()
        levelone.destroy()
    #####Botones########
    B_closelevels = Button(levelone,bg='Red',text='Cerrar y Volver',font='Terminal',command=closelevel1)
    B_closelevels.place(x=0,y=0)
    levelone.protocol('WM_DELETE_WINDOW',closelevel1)

    levelone.mainloop()



#Funcion para cerrar el programa
def close():
    global Space_p
    stop_sound()
    ACTIVE=False
    Space_p.destroy()

###############################
def Validar2():#Se verifica que la entrada tenga algun texto
    global E_Nombre
    nombre_usuario = E_Nombre.get()
    if (nombre_usuario!=""):
        stop_sound()
        return level2()


        
def level2():
    global ACTIVE, Score, ship_life, E_Nombre, reproductor
    if Score!=0:
        pass
    else:
        Score=0
    if ship_life!=0:
            pass
    else:
        ship_life=3   
    ACTIVE=True 
    Space_p.withdraw()
    nombre_usuario = E_Nombre.get()
    reproductor.music = cargarMP3('yu-gi-oh-duel-links-aigami-theme.mp3')
    music = reproducir_cancion(reproductor.music)
    levelone = Toplevel()
    levelone.title('Level 2')
    levelone.minsize(800,800)
    levelone.resizable(width=NO,height=NO)

    C_level1 = Canvas(levelone,bg='White',width=1700,height=1700)
    C_level1.place(x=0,y=0)
    C_level1.fondo = img_load('Fondo2.png')
    Fondo1 = C_level1.create_image(0,0,anchor=NW, image=C_level1.fondo)
    
    Name_L = Label(levelone,text='Player:'+ str(nombre_usuario),bg="#161d2f",fg="white")
    Name_L.place(x=25,y=750)


    def Reloj(seg,minu):#Se crea un reloj con recursividad para determinar el tiempo de la partida   
        global Score, ACTIVE
        if (ACTIVE):
            sleep(1)#Cada segundo, le suma 1 a la variable seg
            Score+=3
            seg+=1
            if seg==60:#Si la variable seg es 60, la variable minu le suma 1
                minu+=1
                seg=0
                if minu==1:
                    Reloj_L.config(text="Exit")
                    final= Label(levelone, text="You win the level",font='Terminal',bg="#161d2f", fg="white")
                    final.place(x=300, y=250)
                    Reintentar_L=Button(levelone, text='Reintentar',font=("Comic Sans MS",10),command=Reintentar, width=10, height=2,bg="#1e0238",fg="white")
                    Reintentar_L.place(x=360, y=350)
                    Siguiente_L=Button(levelone, text='Siguiente Nivel',font=("Comic Sans MS",10),command=lvl2_win, width=10, height=2,bg="#1e0238",fg="white")
                    Siguiente_L.place(x=360, y=450)
                    ACTIVE=False 
            Reloj_L.config(text="Tiempo:"+str(minu)+":"+str(seg))
            Score_L.config(text="Puntos:" + str(Score))
            Reloj(seg,minu)
        
    Thread(target=Reloj,args=[0,0]).start()
    
    def lvl2_win():
        stop_sound()
        levelone.destroy()
        return level3()

    

    images= load_sprite('tile*.png')
    ship = C_level1.create_image(400,400, tags='ship')
    
    def recursive_animation(i):
        nonlocal images
        if(i==3):
            i=0
        if(ACTIVE):
            C_level1.itemconfig('ship',image=images[i])
            time.sleep(0.1)
            Thread(target=recursive_animation,args=(i+1,)).start()
    Thread(target=recursive_animation,args=(0,)).start()    

    def move_ship(event):
        if(ACTIVE):
            if event.keysym =='Up':
                if C_level1.coords(ship)[1]>65:
                    C_level1.move(ship,0,-15)
            elif event.keysym =='Down':
                if C_level1.coords(ship)[1]<754:
                    C_level1.move(ship,0,15)
            elif event.keysym =='Left':
                if C_level1.coords(ship)[0]>43:
                    C_level1.move(ship,-15,0)
            elif event.keysym =='Right':
                if C_level1.coords(ship)[0]<741:
                    C_level1.move(ship,15,0)

    C_level1.bind_all('<KeyPress-Up>',move_ship)
    C_level1.bind_all('<KeyPress-Down>',move_ship)
    C_level1.bind_all('<KeyPress-Left>',move_ship)
    C_level1.bind_all('<KeyPress-Right>',move_ship)
    
    rock= img_load('rock.png')
    Roca0 = C_level1.create_image(random.randint(0,400),random.randint(-10,0),anchor=NW,image=rock)
    Roca1 = C_level1.create_image(random.randint(400,800),random.randint(800,850),anchor=NW,image=rock)
    Roca2 = C_level1.create_image(random.randint(10,500),random.randint(800,850),anchor=NW,image=rock)
    
    Flag2=True
    def temporizador1():
        if(ACTIVE):
            nonlocal Flag2
            if Flag2 == True:
                time.sleep(21)
                Salida_Rocas()
                temporizador1()
    Thread(target = temporizador1).start()

    def move_rockx(rock,x):
        global ship_life
        Cor_rock= C_level1.coords(rock)
        Roca_box= C_level1.bbox(rock)
        Ship_box= C_level1.bbox(ship)
        if(ACTIVE):
            if Cor_rock[0]>=740:
                C_level1.move(rock,-10,0)
                C_level1.after(50,move_rockx,rock,-10)
            elif Cor_rock[0]<-10:
                C_level1.move(rock,10,0)
                C_level1.after(50,move_rockx,rock,10)
            elif Roca_box[0]<Ship_box[2] and Roca_box[2]>Ship_box[0] and Roca_box[1]<Ship_box[3]<Roca_box[3] and Roca_box[3] > Roca_box[1]:
                C_level1.delete(rock)
                reproducir_fx(cargarMP3('golpe.mp3'))
                if ship_life!=0:
                    ship_life-=1
                    Nave_life_l1.config(text="❤:" + str(ship_life))   
            else:
                C_level1.move(rock,x,0)
                C_level1.after(57,move_rockx,rock,x)
    
    
    def move_rocky(rock,y):
        global ship_life
        Cor_rock= C_level1.coords(rock)
        Roca_box= C_level1.bbox(rock)
        Ship_box= C_level1.bbox(ship)
        if(ACTIVE):
            if Cor_rock[1]>740:
                C_level1.move(rock,0,-10)  
                C_level1.after(50,move_rocky,rock,-10)
            elif Cor_rock[1]<-10:
                C_level1.move(rock,0,10)
                C_level1.after(50,move_rocky,rock,10)
            elif Roca_box[0]<Ship_box[2] and Roca_box[2]>Ship_box[0] and Roca_box[1]<Ship_box[3]<Roca_box[3] and Roca_box[3] > Roca_box[1]:
                C_level1.delete(rock)
                reproducir_fx(cargarMP3('golpe.mp3'))
                if ship_life!=0:
                    ship_life-=1
                    Nave_life_l1.config(text="❤:" + str(ship_life)) 
            else:
                C_level1.move(rock,0,y)
                C_level1.after(57,move_rocky,rock,y)
    
    def Salida_Rocas():
        Aleatorio1= random.randint(400,700)
        Aleatorio2= random.randint(700,1100)
        if (ACTIVE):
            coords= C_level1.coords(ship)
            Roca1 = C_level1.create_image(coords[0]+Aleatorio2,coords[1]-Aleatorio1,anchor=NW,image=rock)
            Roca2 = C_level1.create_image(coords[0]-Aleatorio2,coords[1]-Aleatorio2,anchor=NW,image=rock)
            Roca3 = C_level1.create_image(coords[0]-Aleatorio1,coords[1]+Aleatorio1,anchor=NW,image=rock)
            Thread(target=move_rockx,args=(Roca1,10,)).start()
            Thread(target=move_rocky,args=(Roca1,10,)).start()
            Thread(target=move_rockx,args=(Roca2,10,)).start()
            Thread(target=move_rocky,args=(Roca2,10,)).start()
            Thread(target=move_rockx,args=(Roca3,10,)).start()
            Thread(target=move_rocky,args=(Roca3,10,)).start()
            


    Thread(target=move_rockx,args=(Roca0,10,)).start()
    Thread(target=move_rocky,args=(Roca0,10,)).start()
    Thread(target=move_rockx,args=(Roca1,10,)).start()
    Thread(target=move_rocky,args=(Roca1,10,)).start()
    Thread(target=move_rockx,args=(Roca2,10,)).start()
    Thread(target=move_rocky,args=(Roca2,10,)).start()



   




    def Restart1():
        global ship_life,ACTIVE
        if ship_life==0:
            Perdiste_L=Label(levelone,text="Perdiste",font=("Comic Sans MS",15), width=10, height=2,bg="#1e0238",fg="white")
            Perdiste_L.place(x=340, y=200)
            ACTIVE=False
     
            Reintentar_L=Button(levelone, text='Reintentar',font=("Comic Sans MS",10),command=Reintentar, width=10, height=2,bg="#1e0238",fg="white")
            Reintentar_L.place(x=360, y=350)
        else:
            C_level1.after(100,Restart1)
                   
    Thread(target=Restart1).start()

    def Reintentar():
        stop_sound()
        global Score, ship_life
        Score=0
        ship_life=3
        levelone.destroy()
        level2()




    Nave_life_l1 = Label(levelone, text="❤:" + str(ship_life),bg="#161d2f", fg="white")
    Nave_life_l1.place(x=25, y=700)
    Score_L = Label(levelone, text="Puntos:" + str(Score),bg="#161d2f", fg="white")
    Score_L.place(x=740, y=10)
    Reloj_L= Label(levelone, text="Tiempo:0:0",bg="#161d2f", fg="white")
    Reloj_L.place(x=650, y=10)

    #####CERRAR VENTANA##############
    def closelevel1():
        global ACTIVE, Score, ship_life
        ship_life=3
        Score=0
        ACTIVE=False 
        stop_sound()
        Space_p.deiconify()
        levelone.destroy()
    #####Botones########
    B_closelevels = Button(levelone,bg='Red',text='Cerrar y Volver',font='Terminal',command=closelevel1)
    B_closelevels.place(x=0,y=0)
    levelone.protocol('WM_DELETE_WINDOW',closelevel1)

    levelone.mainloop()



#Funcion para cerrar el programa
def close():
    global Space_p
    stop_sound()
    ACTIVE=False
    Space_p.destroy()
###############################
def Validar3():#Se verifica que la entrada tenga algun texto
    global E_Nombre
    nombre_usuario = E_Nombre.get()
    if (nombre_usuario!=""):
        stop_sound()
        return level3()
def level3():
    global ACTIVE, Score, ship_life, E_Nombre
    if Score!=0:
        pass
    else:
        Score=0
    if ship_life!=0:
        pass
    else:
        ship_life=3   
    ACTIVE=True 
    Space_p.withdraw()
    nombre_usuario = E_Nombre.get()
    reproductor.music = cargarMP3('yu-gi-oh-duel-links-kite-tenjo-theme.mp3')
    music = reproducir_cancion(reproductor.music)
    levelone = Toplevel()
    levelone.title('Level 3')
    levelone.minsize(800,800)
    levelone.resizable(width=NO,height=NO)

    C_level1 = Canvas(levelone,bg='White',width=1700,height=1700)
    C_level1.place(x=0,y=0)
    C_level1.fondo = img_load('Fondo3.png')
    Fondo1 = C_level1.create_image(0,0,anchor=NW, image=C_level1.fondo)
    
    Name_L = Label(levelone,text='Player:'+ str(nombre_usuario),bg="#161d2f",fg="white")
    Name_L.place(x=25,y=750)


    def Reloj(seg,minu):#Se crea un reloj con recursividad para determinar el tiempo de la partida   
        global Score, ACTIVE
        if (ACTIVE):
            sleep(1)#Cada segundo, le suma 1 a la variable seg
            Score+=5
            seg+=1
            if seg==60:#Si la variable seg es 60, la variable minu le suma 1
                minu+=1
                seg=0
                if minu==1:
                    Reloj_L.config(text="Exit")
                    final= Label(levelone, text="You win the level",font='Terminal',bg="#161d2f", fg="white")
                    final.place(x=300, y=250)
                    Reintentar_L=Button(levelone, text='Reintentar',font=("Comic Sans MS",10),command=Reintentar, width=10, height=2,bg="#1e0238",fg="white")
                    Reintentar_L.place(x=360, y=350)
                    Siguiente_L=Button(levelone, text='Volver',font=("Comic Sans MS",10),command=lvl2_win, width=10, height=2,bg="#1e0238",fg="white")
                    Siguiente_L.place(x=360, y=450)
                    ACTIVE=False 
            Reloj_L.config(text="Tiempo:"+str(minu)+":"+str(seg))
            Score_L.config(text="Puntos:" + str(Score))
            Reloj(seg,minu)
        
    Thread(target=Reloj,args=[0,0]).start()
    
    def lvl2_win():
        levelone.destroy()
        stop_sound()
        return closelevel1()

    

    images= load_sprite('tile*.png')
    ship = C_level1.create_image(400,400, tags='ship')
    
    def recursive_animation(i):
        nonlocal images
        if(i==3):
            i=0
        if(ACTIVE):
            C_level1.itemconfig('ship',image=images[i])
            time.sleep(0.1)
            Thread(target=recursive_animation,args=(i+1,)).start()
    Thread(target=recursive_animation,args=(0,)).start()    

    def move_ship(event):
        if(ACTIVE):
            if event.keysym =='Up':
                if C_level1.coords(ship)[1]>65:
                    C_level1.move(ship,0,-15)
            elif event.keysym =='Down':
                if C_level1.coords(ship)[1]<754:
                    C_level1.move(ship,0,15)
            elif event.keysym =='Left':
                if C_level1.coords(ship)[0]>43:
                    C_level1.move(ship,-15,0)
            elif event.keysym =='Right':
                if C_level1.coords(ship)[0]<741:
                    C_level1.move(ship,15,0)

    C_level1.bind_all('<KeyPress-Up>',move_ship)
    C_level1.bind_all('<KeyPress-Down>',move_ship)
    C_level1.bind_all('<KeyPress-Left>',move_ship)
    C_level1.bind_all('<KeyPress-Right>',move_ship)
    
    rock= img_load('rock.png')
    Roca0 = C_level1.create_image(random.randint(0,400),random.randint(-10,0),anchor=NW,image=rock)
    Roca1 = C_level1.create_image(random.randint(400,800),random.randint(800,850),anchor=NW,image=rock)
    Roca2 = C_level1.create_image(random.randint(10,500),random.randint(800,850),anchor=NW,image=rock)
    
    Flag2=True
    def temporizador1():
        if(ACTIVE):
            nonlocal Flag2
            if Flag2 == True:
                time.sleep(17)
                Salida_Rocas()
                temporizador1()
    Thread(target = temporizador1).start()

    def move_rockx(rock,x):
        global ship_life
        Cor_rock= C_level1.coords(rock)
        Roca_box= C_level1.bbox(rock)
        Ship_box= C_level1.bbox(ship)
        if(ACTIVE):
            if Cor_rock[0]>=740:
                C_level1.move(rock,-10,0)
                C_level1.after(50,move_rockx,rock,-10)
            elif Cor_rock[0]<-10:
                C_level1.move(rock,10,0)
                C_level1.after(50,move_rockx,rock,10)
            elif Roca_box[0]<Ship_box[2] and Roca_box[2]>Ship_box[0] and Roca_box[1]<Ship_box[3]<Roca_box[3] and Roca_box[3] > Roca_box[1]:
                C_level1.delete(rock)
                reproducir_fx(cargarMP3('golpe.mp3'))
                if ship_life!=0:
                    ship_life-=1
                    Nave_life_l1.config(text="❤:" + str(ship_life))   
            else:
                C_level1.move(rock,x,0)
                C_level1.after(47,move_rockx,rock,x)
    
    
    def move_rocky(rock,y):
        global ship_life
        Cor_rock= C_level1.coords(rock)
        Roca_box= C_level1.bbox(rock)
        Ship_box= C_level1.bbox(ship)
        if(ACTIVE):
            if Cor_rock[1]>740:
                C_level1.move(rock,0,-10)  
                C_level1.after(50,move_rocky,rock,-10)
            elif Cor_rock[1]<-10:
                C_level1.move(rock,0,10)
                C_level1.after(50,move_rocky,rock,10)
            elif Roca_box[0]<Ship_box[2] and Roca_box[2]>Ship_box[0] and Roca_box[1]<Ship_box[3]<Roca_box[3] and Roca_box[3] > Roca_box[1]:
                C_level1.delete(rock)
                reproducir_fx(cargarMP3('golpe.mp3'))
                if ship_life!=0:
                    ship_life-=1
                    Nave_life_l1.config(text="❤:" + str(ship_life)) 
            else:
                C_level1.move(rock,0,y)
                C_level1.after(47,move_rocky,rock,y)
    
    def Salida_Rocas():
        Aleatorio1= random.randint(400,700)
        Aleatorio2= random.randint(700,1100)
        if (ACTIVE):
            coords= C_level1.coords(ship)
            Roca1 = C_level1.create_image(coords[0]+Aleatorio2,coords[1]-Aleatorio1,anchor=NW,image=rock)
            Roca2 = C_level1.create_image(coords[0]-Aleatorio2,coords[1]-Aleatorio2,anchor=NW,image=rock)
            Roca3 = C_level1.create_image(coords[0]-Aleatorio1,coords[1]+Aleatorio1,anchor=NW,image=rock)
            Thread(target=move_rockx,args=(Roca1,10,)).start()
            Thread(target=move_rocky,args=(Roca1,10,)).start()
            Thread(target=move_rockx,args=(Roca2,10,)).start()
            Thread(target=move_rocky,args=(Roca2,10,)).start()
            Thread(target=move_rockx,args=(Roca3,10,)).start()
            Thread(target=move_rocky,args=(Roca3,10,)).start()
            


    Thread(target=move_rockx,args=(Roca0,10,)).start()
    Thread(target=move_rocky,args=(Roca0,10,)).start()
    Thread(target=move_rockx,args=(Roca1,10,)).start()
    Thread(target=move_rocky,args=(Roca1,10,)).start()
    Thread(target=move_rockx,args=(Roca2,10,)).start()
    Thread(target=move_rocky,args=(Roca2,10,)).start()


    def Restart1():
        global ship_life,ACTIVE
        if ship_life==0:
            Perdiste_L=Label(levelone,text="Perdiste",font=("Comic Sans MS",15), width=10, height=2,bg="#1e0238",fg="white")
            Perdiste_L.place(x=340, y=200)
            ACTIVE=False
     
            Reintentar_L=Button(levelone, text='Reintentar',font=("Comic Sans MS",10),command=Reintentar, width=10, height=2,bg="#1e0238",fg="white")
            Reintentar_L.place(x=360, y=350)
        else:
            C_level1.after(100,Restart1)
                   
    Thread(target=Restart1).start()

    def Reintentar():
        global Score, ship_life
        Score=0
        stop_sound()
        ship_life=3
        levelone.destroy()
        level3()




    Nave_life_l1 = Label(levelone, text="❤:" + str(ship_life),bg="#161d2f", fg="white")
    Nave_life_l1.place(x=25, y=700)
    Score_L = Label(levelone, text="Puntos:" + str(Score),bg="#161d2f", fg="white")
    Score_L.place(x=740, y=10)
    Reloj_L= Label(levelone, text="Tiempo:0:0",bg="#161d2f", fg="white")
    Reloj_L.place(x=650, y=10)

    #####CERRAR VENTANA##############
    def closelevel1():
        global ACTIVE, Score, ship_life
        ship_life=3
        Score=0
        ACTIVE=False 
        stop_sound()
        Space_p.deiconify()
        levelone.destroy()
    #####Botones########
    B_closelevels = Button(levelone,bg='Red',text='Cerrar y Volver',font='Terminal',command=closelevel1)
    B_closelevels.place(x=0,y=0)
    levelone.protocol('WM_DELETE_WINDOW',closelevel1)

    levelone.mainloop()





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

B_level1= Button(Space_p,bg='#41036e',text='Fácil',font='Terminal',command=Validar1) 
B_level1.place(x=350,y=400)
B_level2= Button(Space_p,bg='#41036e',text='Intermedio',font='Terminal',command=Validar2)
B_level2.place(x=350,y=450)
B_level3= Button(Space_p,bg='#41036e',text='Difícil',font='Terminal',command=Validar3)
B_level3.place(x=350,y=500)


Space_p.protocol('WM_DELETE_WINDOW',close)
Space_p.mainloop()