import time
from tkinter import *
import random
from PIL import Image, ImageTk


#-----------------------------------------------------------------------------
# Created by @Pacsoda
# Credit @jenja-pa
#-----------------------------------------------------------------------------

tk = Tk()
tk.title = "Sea War"

canvas = Canvas(tk, width=500, height=500)
canvas.pack()

sprite_ghost = PhotoImage(file = "resource/sprite_ghost_1_up2.png")

def draw_gun(c_x):
    canvas.create_rectangle(c_x-60, 480, c_x+60, 500, fill="black")
    canvas.create_rectangle(c_x-10, 460, c_x+10, 480, fill="black")

proyectil = []
shots = 10 #Municion
txt_municion = None

#-----------------------------------------------------------------------------
#shots
#-----------------------------------------------------------------------------
def ball(event):
    global shots, proyectil, txt_municion
    if shots > 0:
        shots -= 1
        msj_muncion("Munición: " + str(shots),"black")
        proyectil.append([canvas.create_image(242, 460, anchor = NW, image = sprite_ghost)])
    else:
        msj_muncion("Munición agotada!","red")        
#-----------------------------------------------------------------------------
#Msj Game
#-----------------------------------------------------------------------------
def msj_muncion(msj, color):
    global txt_municion
    if txt_municion is not None:
            canvas.delete(txt_municion)
    txt_municion = canvas.create_text(420, 100, text=msj, fill=color)

canvas.bind_all("<space>", ball)

ship_image = PhotoImage(file = "resource/ship.gif")


#Load an image in the script
image = Image.open("resource/pixel-explosion.png")

#Resize the Image using resize method
resized_image = image.resize((70,40), Image.ANTIALIAS)
pixel_explosion = ImageTk.PhotoImage(resized_image)

draw_gun(250)

#-----------------------------------------------------------------------------
#Logic Game
#-----------------------------------------------------------------------------
explocion = 0
for z in range(10):
    barco = canvas.create_image(500, 10, anchor = NW, image = ship_image)
    v = random.randint(2, 5)
    for y in range(300):
        len_proyectil = len(proyectil) #cantidad de proyectiles en ejecución
        if barco is not None:
            canvas.move(barco, -v, 0)
            ax0, ay0, ax1, ay1 = canvas.bbox(barco) #Coordenadas del barco
        if len_proyectil > 0:
            remove_proyectil = 0
            for i in range(len_proyectil):
                print(str(len_proyectil))
                if remove_proyectil == 0:
                    canvas.move(proyectil[i], 0, -5)
                    bx0, by0, bx1, by1 = canvas.bbox(proyectil[i]) #Coordenadas de los proyectiles
                else:
                    #Se removieron proyectiles
                    canvas.move(proyectil[i-remove_proyectil], 0, -5)
                    bx0, by0, bx1, by1 = canvas.bbox(proyectil[i-remove_proyectil]) #Coordenadas de los proyectiles
                if ax0 <= 240 and ax0 >= 170 and by0 <= 40 and by0 >= 1:
                    explocion = canvas.create_image(ax0, 0, anchor = NW, image = pixel_explosion)
                    shots += 1 #add municion
                    msj_muncion("[+1] Munición: " + str(shots),"blue")
                    if barco is not None:
                        canvas.delete(barco) # remove barco canvas
                        barco = None
                        ax0 = 0 #Clear coordenadas
                    canvas.after(500, lambda x=explocion: canvas.delete(x))
                if by0 <= 0:
                    canvas.delete(proyectil[i]) #remove proyectil canvas
                    del proyectil[i] #remove proyectil in list
                    remove_proyectil+=1 #numero de proyectiles removidos
                    print("remove proyectil")
        tk.update()
        time.sleep(0.02)
    if barco is not None:
        canvas.delete(barco) # remove barco canvas
        print("remove barco")
tk.mainloop()