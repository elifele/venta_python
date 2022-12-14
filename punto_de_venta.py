from tkinter import *

ventas = Tk()
ventas.title("Punto de ventas con python")
ventas.geometry("1350x700")
ventas.config(bg="azure3")
titulo = Label(ventas, text="Punto de ventas con python", 
bd=5, relief=FLAT,font=("Arial black", 20), bg="gray8",fg="white").pack(fill=X)

datos_cliente = LabelFrame(ventas, text="Informacion del cliente", 
    font=("Arial black",12),bg="gray11",fg="white",relief=FLAT, bd=10, )
datos_cliente.place(x=0, y=80, relwidth=1)

nombre = Label(datos_cliente,text="Nombre", font=("Arial black", 14), bg="azure4",
fg="white").grid(row=0,column=0,padx=8)
nombre_entry = Entry(datos_cliente,borderwidth=4,width=21).grid(row=0,column=1,padx=8)

apellido = Label(datos_cliente,text="Apellido", font=("Arial black", 14),bg="azure4",
fg="white").grid(row=0,column=2,padx=8)
apellido_entry = Entry(datos_cliente,borderwidth=4,width=21).grid(row=0,column=3,padx=8)

direccion = Label(datos_cliente,text="Direccion", font=("Arial black", 14),bg="azure4",
fg="white").grid(row=0,column=4,padx=8)
direccion_entry = Entry(datos_cliente,borderwidth=4,width=21).grid(row=0,column=5,padx=8)

telefono = Label(datos_cliente,text="Telefono", font=("Arial black", 14),bg="azure4",
fg="white").grid(row=0,column=6,padx=8)
telefono_entry = Entry(datos_cliente,borderwidth=4,width=21).grid(row=0,column=7,padx=8)

correo = Label(datos_cliente,text="Correo", font=("Arial black", 14), bg="azure4",
fg="white").grid(row=0,column=8,padx=8)
correo_entry = Entry(datos_cliente, borderwidth=4,width=21).grid(row=0, column=9,padx=8)

tabla_productos = Label(ventas,text="Tabla de Productos",
    font=("Arial black", 15), bg="gray8",fg="white", relief=FLAT, borderwidth=10)
tabla_productos.place(x=12, y=180, width=1327)

informatica = LabelFrame(ventas,text="Productos de Informatica",
    font=("Arial black", 12), bg="gray10", fg="white", relief=FLAT, borderwidth=10)
informatica.place(x=5,y=250, height=380, width=325)

ferreteria = LabelFrame(ventas,text="Productos de Ferreteria",
    font=("Arial black", 12),bg="gray10", fg="white", relief=FLAT, borderwidth=10)
ferreteria.place(x=500,y=250,height=380,width=325)

frame = Frame(ventas, bd=10, relief=FLAT, bg="gray10")
frame.place(x=1012, y=250, width=330, height=380)

factura = Label(frame,text="Factura",font=("Arial black", 14),
bd=2,relief=FLAT, bg="gray10",fg="#ffffff").pack(fill=X)

scroll = Scrollbar(frame, orient=VERTICAL)
texarea = Text(frame, yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=texarea.yview)
texarea.pack(fill=BOTH, expand=1)

lapto = Label(informatica, text="lapto", font=("Arial black",11),
bg="gray10",fg="#ffffff").grid(row=1,column=0,pady=11)
lapto_entry = Entry(informatica, borderwidth=2,width=20).grid(row=1,column=1,padx=10)

impresora = Label(informatica, text="Impresora",font=("Arial black",11),
bg="gray10", fg="#ffffff").grid(row=2,column=0,pady=11)
impresora_entry = Entry(informatica, borderwidth=2, width=20).grid(row=2,column=1,padx=10)

mouse =  Label(informatica, text="Mouse",font=("Arial black",11),
bg="gray10",fg="#ffffff").grid(row=3,column=0,pady=11)
mouse_entry = Entry(informatica, borderwidth=2, width=20).grid(row=3,column=1,padx=10)

teclado =  Label(informatica, text="Teclado",font=("Arial black",11),
bg="gray10",fg="#ffffff").grid(row=4,column=0,pady=11)
teclado_entry = Entry(informatica, borderwidth=2, width=20).grid(row=4,column=1,padx=10)

usb = Label(informatica, text="USB", font=("Arial black", 11),
bg="gray10",fg="#ffffff").grid(row=5,column=0,pady=11)
usb_entry = Entry(informatica, borderwidth=2, width=20).grid(row=5,column=1,padx=10) 

disco_duro = Label(informatica, text="Disco Duro", font=("Arial black", 11),
bg="gray10",fg="#ffffff").grid(row=6,column=0,pady=11)
disco_duro_entry = Entry(informatica, borderwidth=2, width=20).grid(row=6,column=1,padx=10)

martillo = Label(ferreteria, text="Martillo", font=("Arial black", 11),
bg="gray10",fg="#ffffff").grid(row=1,column=0,pady=11)
martillo_entry = Entry(ferreteria, borderwidth=2, width=20).grid(row=1,column=1,padx=10) 

taladro = Label(ferreteria, text="Taladro", font=("Arial black", 11),
bg="gray10",fg="#ffffff").grid(row=2,column=0,pady=11)
taladro_entry = Entry(ferreteria, borderwidth=2, width=20).grid(row=2,column=1,padx=10)

pinzas = Label(ferreteria, text="pinzas", font=("Arial black", 11),
bg="gray10",fg="#ffffff").grid(row=3,column=0,pady=11)
pinzas_entry = Entry(ferreteria, borderwidth=2, width=20).grid(row=3,column=1,padx=10)

alicate = Label(ferreteria, text="Alicate", font=("Arial black", 11),
bg="gray10",fg="#ffffff").grid(row=4,column=0,pady=11)
alicate_entry = Entry(ferreteria, borderwidth=2, width=20).grid(row=4,column=1,padx=10)

destornillador = Label(ferreteria, text="Destornillador", font=("Arial black", 11),
bg="gray10",fg="#ffffff").grid(row=5,column=0,pady=11)
destornillador_entry = Entry(ferreteria, borderwidth=2, width=20).grid(row=5,column=1,padx=10)

cable_electrico = Label(ferreteria, text="Cable Electrico", font=("Arial black", 11),
bg="gray10",fg="#ffffff").grid(row=6,column=0,pady=11)
cable_electrico_entry = Entry(ferreteria, borderwidth=2, width=20).grid(row=6,column=1,padx=10)

titulo = LabelFrame(ventas, text="Resumen de compra",font=("Arial Black",11), 
relief=FLAT, bd=5, bg="azure4", fg="white")
titulo.place(x=0, y=570, relwidth=1, height=137)

infor_label = Label(titulo, text="Informatica", font=("Arial black", 11), 
bg="azure4",fg="white").grid(row=0,column=0,)
infor_entry = Entry(titulo, width=30, borderwidth=2, ).grid(row=0, column=1, padx=10, pady=15)

ferre_label = Label(titulo, text="Ferreteria", font=("Arial black", 11), 
bg="azure4",fg="white").grid(row=2,column=0,)
ferre_entry = Entry(titulo, width=30, borderwidth=2, ).grid(row=2, column=1, padx=10, pady=15)

button_frame = Frame(titulo, bd=7, relief=FLAT, bg="gray13")
button_frame.place(x=500, width=800, height=95)

button_factura = Button(button_frame, text="Factura", width=15, font=("Arial black", 12),
pady=10, bg="azure4", fg="#ffffff").grid(row=0, column=0, padx=12, pady=12)

button_imprimir = Button(button_frame, text="Imprimir", width=15, font=("Arial black", 12),
pady=10, bg="azure4", fg="#ffffff").grid(row=0, column=1, padx=10, pady=6)

button_limpiar = Button(button_frame, text="Limpiar", width=15, font=("Arial black", 12),
pady=10, bg="azure4", fg="#ffffff").grid(row=0, column=2, padx=10, pady=6)

button_salir = Button(button_frame, text="Salir",width=15, font=("Arial black", 12),
pady=10, bg="azure4", fg="#ffffff").grid(row=0, column=3, padx=10, pady=6)


ventas.mainloop()
 
