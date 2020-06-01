from tkinter import*
from tkinter import ttk
import json


root = Tk()
root.geometry('500x900')
root.resizable(0,0)

with open('diputados.json', encoding='utf-8') as file_diputados, \
        open('viajes.json', encoding='utf-8') as file_viajes:

    lst_diputados = json.load(file_diputados)
    lst_viajes = json.load(file_viajes)

#Funciones
def Diputados_x_provincia():
    contador = 0
    for diputado in lst_diputados:
        if diputado[str(lst_diputados.index(diputado)+1)]['diputado_distrito']==Provinc_entr_var.get():
            contador+=1
            print(contador)
            print(diputado[str(lst_diputados.index(diputado)+1)]['diputado_distrito'])
    cantidad_1_var.set(contador)


#GUI
    #Frame_Diputados_por_provincia
Dip_x_provincia = Frame(root, width=500, height=200, relief=SUNKEN, bd=20)
Dip_x_provincia.pack()
Provinc_ = Label(Dip_x_provincia, text='Provincia: ').place(x=20, y=30)
Provinc_entr_var = StringVar(Dip_x_provincia)
Provinc_entr = Entry(Dip_x_provincia, textvariable=Provinc_entr_var)
Provinc_entr.place(x=80, y=30)
Calc_btn_1 = Button(Dip_x_provincia, text='Calcular', command=Diputados_x_provincia).place(x=180, y=120)
Cantidad_1_lbl = Label(Dip_x_provincia, text='Cantidad: ').place(x=230, y=60)
cantidad_1_var = StringVar(Dip_x_provincia)
Cantidad_1_entr = Entry(Dip_x_provincia, textvariable=cantidad_1_var)
Cantidad_1_entr.place(x=300, y= 60)
    #Frame_Diputados_por_Bloque_Político
Dip_x_bloque = Frame(root, width=500, height=200, relief=SUNKEN, bd=20)
Dip_x_bloque.pack()
bloque_ = Label(Dip_x_bloque, text='Bloque: ').place(x=20, y=30)
bloque_entr_var = StringVar(Dip_x_bloque)
bloque_entr = Entry(Dip_x_bloque, textvariable=bloque_entr_var)
bloque_entr.place(x=80, y=30)
Calc_btn_1 = Button(Dip_x_bloque, text='Calcular').place(x=180, y=120)
Hombres_lbl = Label(Dip_x_bloque, text='Hombres: ').place(x=230, y=60)
Mujeres_lbl = Label(Dip_x_bloque, text='Mujeres: ').place(x=230, y=90)
hombres_var = StringVar(Dip_x_bloque)
mujeres_var = StringVar(Dip_x_bloque)
hombres_entr = Entry(Dip_x_bloque, textvariable=hombres_var)
hombres_entr.place(x=300, y= 60)
mujeres_entr = Entry(Dip_x_bloque, textvariable=mujeres_var)
mujeres_entr.place(x=300, y= 90)
    #Frame_Cantidad_Viajes
Cantidad_Viajes_F = Frame(root, width=500, height=200, relief=SUNKEN, bd=20)
Cantidad_Viajes_F.pack()
Origen_ = Label(Cantidad_Viajes_F, text='Origen: ').place(x=20, y=30)
Destino_ = Label(Cantidad_Viajes_F, text='Destino: ').place(x=20, y=60)
origen_var = StringVar(Cantidad_Viajes_F)
origen_entr = Entry(Cantidad_Viajes_F, textvariable=origen_var)
origen_entr.place(x=80, y=30)
destino_var = StringVar(Cantidad_Viajes_F)
destino_entr = Entry(Cantidad_Viajes_F, textvariable=destino_var)
destino_entr.place(x=80, y=60)
Calc_btn_1 = Button(Cantidad_Viajes_F, text='Calcular').place(x=180, y=120)
Cantidad_2_lbl = Label(Cantidad_Viajes_F, text='Cantidad: ').place(x=230, y=60)
cantidad_2_var = StringVar(Cantidad_Viajes_F)
Cantidad_2_entr = Entry(Cantidad_Viajes_F, textvariable=cantidad_2_var)
Cantidad_2_entr.place(x=300, y= 60)
    #Frame_Buscador_Diputados
Buscador_diputados = Frame(root, width=500, height=300, relief=SUNKEN, bd=20)
Buscador_diputados.pack()
Diputado_id = Label(Buscador_diputados, text='Diputado ID: ').place(x=20, y=30)
diputado_entr_var = StringVar(Buscador_diputados)
diputado_entr = Entry(Buscador_diputados, textvariable=Buscador_diputados)
diputado_entr.place(x=120, y=30)

Buscar_btn = Button(Buscador_diputados, text='Buscar').place(x=300, y=30)

Nombre_completo_lbl = Label(Buscador_diputados, text='Nombre completo: ').place(x=20, y=60)
Nombre_completo_entr_var = StringVar(Buscador_diputados)
Nombre_completo_entr = Entry(Buscador_diputados, textvariable=Buscador_diputados)
Nombre_completo_entr.place(x=150, y=60)

Provincia_buscador_lbl = Label(Buscador_diputados, text='Provincia: ').place(x=20, y=90)
Provincia_buscador_entr_var = StringVar(Buscador_diputados)
Provincia_buscador_entr = Entry(Buscador_diputados, textvariable=Buscador_diputados)
Provincia_buscador_entr.place(x=150, y=90)

cantidad_viajes_2_lbl = Label(Buscador_diputados, text='Cantidad de Viajes: ').place(x=20, y=120)
cantidad_viajes_2_entr_var = StringVar(Buscador_diputados)
cantidad_viajes_2_entr = Entry(Buscador_diputados, textvariable=cantidad_viajes_2_entr_var)
cantidad_viajes_2_entr.place(x=150, y=120)

bloque_2_lbl = Label(Buscador_diputados, text='Bloque: ').place(x=20, y=150)
bloque_2_entr_var = StringVar(Buscador_diputados)
bloque_2_entr = Entry(Buscador_diputados, textvariable=bloque_2_entr_var)
bloque_2_entr.place(x=150, y=150)

año_inicio_lbl = Label(Buscador_diputados, text='Año inicio: ').place(x=20, y=180)
año_inicio_entr_var = StringVar(Buscador_diputados)
año_inicio_entr = Entry(Buscador_diputados, textvariable=año_inicio_entr_var)
año_inicio_entr.place(x=150, y=180)


root.mainloop()