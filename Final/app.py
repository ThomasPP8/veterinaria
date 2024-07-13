from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb #Acceder estilos de bootstrap
import sqlite3 as sql #Libreria de SQLittle
import random

class Ventana(tb.Window): #Aqui cambia el "TK" por "tb.Window"
    def __init__(self):
        super().__init__()
        self.ventana_login()
        self.icon_image = PhotoImage(file='Logo.png')
        self.iconphoto(False, self.icon_image)

    #VENTANA Log in
    def ventana_login(self):
        self.frame_login=Frame(self)
        self.frame_login.pack()

        self.lblframe__login=LabelFrame(self.frame_login, text='Acceso') #Panel e input Acceso
        self.lblframe__login.pack(padx=10,pady=10)

        lbltitulo=Label(self.lblframe__login,text='inicio de sesion', font=('Arial',18)) #Etiqueta titulo
        lbltitulo.pack(padx=10,pady=35)

        txt_usuario=ttk.Entry(self.lblframe__login, width=40, justify=CENTER) #Entry para campo de texto
        txt_usuario.pack(padx=10,pady=10)
        txt_clave=ttk.Entry(self.lblframe__login,width=40, justify=CENTER)
        txt_clave.pack(padx=10,pady=10)
        txt_clave.configure(show='*') #Censurar clave
        btn_acceso=ttk.Button(self.lblframe__login,text='Log in',command=self.logueo)
        btn_acceso.pack(padx=10,pady=10)
        
    #VENTANA Menu
    def ventana_menu(self):
        self.frame_left=Frame(self,width=200)
        self.frame_left.grid(row=0,column=0,sticky=NSEW)
        self.frame_center=Frame(self)
        self.frame_center.grid(row=0,column=1,sticky=NSEW)
        self.frame_right=Frame(self,width=400)
        self.frame_right.grid(row=0,column=2,sticky=NSEW)

        btn_productos=ttk.Button(self.frame_left,text='Clientes',width=15, command=self.ventana_lista_clientes)
        btn_productos.grid(row=0,column=0,padx=10,pady=10)
        btn_ventas=ttk.Button(self.frame_left,text='Mascotas',width=15,command=self.ventana_lista_mascotas)
        btn_ventas.grid(row=1,column=0,padx=10,pady=10)
        btn_clientes=ttk.Button(self.frame_left,text='Empleados',width=15, command=self.ventana_lista_empleados)
        btn_clientes.grid(row=2,column=0,padx=10,pady=10)
        btn_compras=ttk.Button(self.frame_left,text='Diagnosticos',width=15, command=self.ventana_lista_diagnosticos)
        btn_compras.grid(row=3,column=0,padx=10,pady=10)
        btn_usuarios=ttk.Button(self.frame_left,text='Facturas',width=15,command=self.ventana_lista_facturas)
        btn_usuarios.grid(row=4,column=0,padx=10,pady=10)


        # lbl2=Label(self.frame_center,text='Aqui Pondremos las ventanas que creemos')
        # lbl2.grid(row=0,column=0,padx=10,pady=10)

        # lbl3=Label(self.frame_right,text='Aqui Pondremos las busquedas para la ventana')
        # lbl3.grid(row=0,column=0,padx=10,pady=10)

    def logueo(self):
        self.frame_login.pack_forget()#Ocultar la ventana de Login
        self.ventana_menu()#abrir ventana de menu


#VENTANAS ********************************
    def ventana_lista_clientes(self):
        self.frame_lista_clientes=Frame(self.frame_center)
        self.frame_lista_clientes.grid(row=0,column=0,columnspan=2,sticky=NSEW)

        self.lblframe_botones_listclient=LabelFrame(self.frame_lista_clientes)
        self.lblframe_botones_listclient.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

        btn_nuevo_cliente=tb.Button(self.lblframe_botones_listclient,text='Nuevo',width=15,bootstyle="success", command=self.nuevo_cliente)
        btn_nuevo_cliente.grid(row=0,column=0,padx=5,pady=5)
        btn_modificar_cliente=tb.Button(self.lblframe_botones_listclient,text='Modificar',width=15,bootstyle="warning")
        btn_modificar_cliente.grid(row=0,column=1,padx=5,pady=5)
        btn_eliminar_cliente=tb.Button(self.lblframe_botones_listclient,text='Eliminar',width=15,bootstyle="danger")
        btn_eliminar_cliente.grid(row=0,column=2,padx=5,pady=5)

        self.lblframe_busqueda_listclient=LabelFrame(self.frame_lista_clientes)
        self.lblframe_busqueda_listclient.grid(row=1,column=0,padx=10,pady=10,sticky=NSEW)

        txt_busqueda_clientes=ttk.Entry(self.lblframe_busqueda_listclient,width=90)
        txt_busqueda_clientes.grid(row=0,column=0,padx=5,pady=5)

        #====================Treeview=====================================

        self.lblframe_tree_listclient=LabelFrame(self.frame_lista_clientes)
        self.lblframe_tree_listclient.grid(row=2,column=0,padx=10,pady=10,sticky=NSEW)
        
        columnas=("ClienteID","TipoDocumento", "#Documento", "TipoPersona", "Nombre", "Telefono", "Correo", "DireccionCliente")

        self.tree_lista_clientes=tb.Treeview(self.lblframe_tree_listclient,columns=columnas,
                                        height=17,show='headings',bootstyle='dark')
        self.tree_lista_clientes.grid(row=0,column=0)

        self.tree_lista_clientes.heading("ClienteID",text="ClienteID",anchor=W)
        self.tree_lista_clientes.heading("TipoDocumento",text="TipoDocumento",anchor=W)
        self.tree_lista_clientes.heading("#Documento",text="Numero Documento",anchor=W)
        self.tree_lista_clientes.heading("TipoPersona",text="TipoPersona",anchor=W)
        self.tree_lista_clientes.heading("Nombre",text="Nombre",anchor=W)
        self.tree_lista_clientes.heading("Telefono",text="Telefono",anchor=W)
        self.tree_lista_clientes.heading("Correo",text="Correo",anchor=W)
        self.tree_lista_clientes.heading("DireccionCliente",text="DireccionCliente",anchor=W)
        self.tree_lista_clientes['displaycolumns']=("TipoDocumento", "#Documento", "TipoPersona", "Nombre", "Telefono", "Correo", "DireccionCliente") #Ocultar columna clave

        #Crear Scrolbar
        tree_scroll_listaclient=tb.Scrollbar(self.frame_lista_clientes,bootstyle='round-success')
        tree_scroll_listaclient.grid(row=2,column=1)
        #configurar scrolbar
        tree_scroll_listaclient.config(command=self.tree_lista_clientes.yview)

        #Llamamos a nuestra funcion mostrar usuarios
        self.mostrar_clientes()
    
    def ventana_lista_mascotas(self):
        self.frame_lista_mascotas = Frame(self.frame_center)
        self.frame_lista_mascotas.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        self.lblframe_botones_listpet = LabelFrame(self.frame_lista_mascotas)
        self.lblframe_botones_listpet.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

        btn_nueva_mascota = tb.Button(self.lblframe_botones_listpet, text='Nueva', width=15, bootstyle="success", command=self.nuevo_mascota)
        btn_nueva_mascota.grid(row=0, column=0, padx=5, pady=5)
        btn_modificar_mascota = tb.Button(self.lblframe_botones_listpet, text='Modificar', width=15, bootstyle="warning")
        btn_modificar_mascota.grid(row=0, column=1, padx=5, pady=5)
        btn_eliminar_mascota = tb.Button(self.lblframe_botones_listpet, text='Eliminar', width=15, bootstyle="danger")
        btn_eliminar_mascota.grid(row=0, column=2, padx=5, pady=5)

        self.lblframe_busqueda_listpet = LabelFrame(self.frame_lista_mascotas)
        self.lblframe_busqueda_listpet.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

        txt_busqueda_mascotas = ttk.Entry(self.lblframe_busqueda_listpet, width=90)
        txt_busqueda_mascotas.grid(row=0, column=0, padx=5, pady=5)

        #====================Treeview=====================================

        self.lblframe_tree_listpet = LabelFrame(self.frame_lista_mascotas)
        self.lblframe_tree_listpet.grid(row=2, column=0, padx=10, pady=10, sticky=NSEW)
        
        columnas = ("MascotaID", "CodigoMascota", "Raza", "Nombre", "Edad", "NumeroIdentidadDueno", "Descripcion")

        self.tree_lista_mascotas = tb.Treeview(self.lblframe_tree_listpet, columns=columnas,
                                            height=17, show='headings', bootstyle='dark')
        self.tree_lista_mascotas.grid(row=0, column=0, sticky='nsew')

        # Configuración de encabezados de columnas
        self.tree_lista_mascotas.heading("MascotaID", text="MascotaID", anchor=W)
        self.tree_lista_mascotas.heading("CodigoMascota", text="CodigoMascota", anchor=W)
        self.tree_lista_mascotas.heading("Raza", text="Raza", anchor=W)
        self.tree_lista_mascotas.heading("Nombre", text="Nombre", anchor=W)
        self.tree_lista_mascotas.heading("Edad", text="Edad", anchor=W)
        self.tree_lista_mascotas.heading("NumeroIdentidadDueno", text="Documento Dueño", anchor=W)
        self.tree_lista_mascotas.heading("Descripcion", text="Descripcion", anchor=W)

        # Mostrar solo las columnas necesarias
        self.tree_lista_mascotas['displaycolumns'] = ("CodigoMascota", "Raza", "Nombre", "Edad", "NumeroIdentidadDueno", "Descripcion")

        # Crear Scrollbar
        tree_scroll_listapet = tb.Scrollbar(self.lblframe_tree_listpet, orient="vertical", command=self.tree_lista_mascotas.yview, bootstyle='round-success')
        tree_scroll_listapet.grid(row=0, column=1, sticky='ns')
        self.tree_lista_mascotas.configure(yscrollcommand=tree_scroll_listapet.set)

        # Llamamos a nuestra función mostrar mascotas
        self.mostrar_mascotas()

    def ventana_lista_empleados(self):
        self.frame_lista_empleados = Frame(self.frame_center)
        self.frame_lista_empleados.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        self.lblframe_botones_listemp = LabelFrame(self.frame_lista_empleados)
        self.lblframe_botones_listemp.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

        btn_nuevo_empleado = tb.Button(self.lblframe_botones_listemp, text='Nuevo', width=15, bootstyle="success")
        btn_nuevo_empleado.grid(row=0, column=0, padx=5, pady=5)
        btn_modificar_empleado = tb.Button(self.lblframe_botones_listemp, text='Modificar', width=15, bootstyle="warning")
        btn_modificar_empleado.grid(row=0, column=1, padx=5, pady=5)
        btn_eliminar_empleado = tb.Button(self.lblframe_botones_listemp, text='Eliminar', width=15, bootstyle="danger")
        btn_eliminar_empleado.grid(row=0, column=2, padx=5, pady=5)

        self.lblframe_busqueda_listemp = LabelFrame(self.frame_lista_empleados)
        self.lblframe_busqueda_listemp.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

        txt_busqueda_empleados = ttk.Entry(self.lblframe_busqueda_listemp, width=90)
        txt_busqueda_empleados.grid(row=0, column=0, padx=5, pady=5)

        #====================Treeview=====================================

        self.lblframe_tree_listemp = LabelFrame(self.frame_lista_empleados)
        self.lblframe_tree_listemp.grid(row=2, column=0, padx=10, pady=10, sticky=NSEW)
        
        columnas = ("EmpleadoID", "TipoDocumento", "NumeroDocumento", "DireccionVivienda", "NumeroTelefono", "NombreCompleto", "CorreoElectronico", "FechaContratacion", "CargoEnClinica")

        self.tree_lista_empleados = tb.Treeview(self.lblframe_tree_listemp, columns=columnas,
                                                height=17, show='headings', bootstyle='dark')
        self.tree_lista_empleados.grid(row=0, column=0, sticky='nsew')

        # Configuración de encabezados de columnas
        self.tree_lista_empleados.heading("EmpleadoID", text="EmpleadoID", anchor=W)
        self.tree_lista_empleados.heading("TipoDocumento", text="Tipo Documento", anchor=W)
        self.tree_lista_empleados.heading("NumeroDocumento", text="Número Documento", anchor=W)
        self.tree_lista_empleados.heading("DireccionVivienda", text="Dirección Vivienda", anchor=W)
        self.tree_lista_empleados.heading("NumeroTelefono", text="Número Teléfono", anchor=W)
        self.tree_lista_empleados.heading("NombreCompleto", text="Nombre Completo", anchor=W)
        self.tree_lista_empleados.heading("CorreoElectronico", text="Correo Electrónico", anchor=W)
        self.tree_lista_empleados.heading("FechaContratacion", text="Fecha Contratación", anchor=W)
        self.tree_lista_empleados.heading("CargoEnClinica", text="Cargo en Clínica", anchor=W)

        # Mostrar solo las columnas necesarias
        self.tree_lista_empleados['displaycolumns'] = ("TipoDocumento", "NumeroDocumento", "DireccionVivienda", "NumeroTelefono", "NombreCompleto", "CorreoElectronico", "FechaContratacion", "CargoEnClinica")

        # Crear Scrollbar
        tree_scroll_listaemp = tb.Scrollbar(self.lblframe_tree_listemp, orient="vertical", command=self.tree_lista_empleados.yview, bootstyle='round-success')
        tree_scroll_listaemp.grid(row=0, column=1, sticky='ns')
        self.tree_lista_empleados.configure(yscrollcommand=tree_scroll_listaemp.set)

        # Llamamos a nuestra función mostrar empleados
        self.mostrar_empleados()

    def ventana_lista_facturas(self):
        self.frame_lista_facturas = Frame(self.frame_center)
        self.frame_lista_facturas.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        self.lblframe_botones_listfac = LabelFrame(self.frame_lista_facturas)
        self.lblframe_botones_listfac.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

        btn_nueva_factura = tb.Button(self.lblframe_botones_listfac, text='Nueva', width=15, bootstyle="success")
        btn_nueva_factura.grid(row=0, column=0, padx=5, pady=5)
        btn_modificar_factura = tb.Button(self.lblframe_botones_listfac, text='Modificar', width=15, bootstyle="warning")
        btn_modificar_factura.grid(row=0, column=1, padx=5, pady=5)
        btn_eliminar_factura = tb.Button(self.lblframe_botones_listfac, text='Eliminar', width=15, bootstyle="danger")
        btn_eliminar_factura.grid(row=0, column=2, padx=5, pady=5)

        self.lblframe_busqueda_listfac = LabelFrame(self.frame_lista_facturas)
        self.lblframe_busqueda_listfac.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

        txt_busqueda_facturas = ttk.Entry(self.lblframe_busqueda_listfac, width=90)
        txt_busqueda_facturas.grid(row=0, column=0, padx=5, pady=5)

        #====================Treeview=====================================

        self.lblframe_tree_listfac = LabelFrame(self.frame_lista_facturas)
        self.lblframe_tree_listfac.grid(row=2, column=0, padx=10, pady=10, sticky=NSEW)
        
        columnas = ("FacturaID", "DiagnosticoID", "DescripcionDelServicio", "CostoDelServicio")

        self.tree_lista_facturas = tb.Treeview(self.lblframe_tree_listfac, columns=columnas,
                                            height=17, show='headings', bootstyle='dark')
        self.tree_lista_facturas.grid(row=0, column=0, sticky='nsew')

        # Configuración de encabezados de columnas
        self.tree_lista_facturas.heading("FacturaID", text="FacturaID", anchor=W)
        self.tree_lista_facturas.heading("DiagnosticoID", text="Diagnóstico ID", anchor=W)
        self.tree_lista_facturas.heading("DescripcionDelServicio", text="Descripción del Servicio", anchor=W)
        self.tree_lista_facturas.heading("CostoDelServicio", text="Costo del Servicio", anchor=W)

        # Mostrar solo las columnas necesarias
        self.tree_lista_facturas['displaycolumns'] = ("DiagnosticoID", "DescripcionDelServicio", "CostoDelServicio")

        # Crear Scrollbar
        tree_scroll_listafac = tb.Scrollbar(self.lblframe_tree_listfac, orient="vertical", command=self.tree_lista_facturas.yview, bootstyle='round-success')
        tree_scroll_listafac.grid(row=0, column=1, sticky='ns')
        self.tree_lista_facturas.configure(yscrollcommand=tree_scroll_listafac.set)

        # Llamamos a nuestra función mostrar facturas
        self.mostrar_facturas()

    def ventana_lista_diagnosticos(self):
        self.frame_lista_diagnosticos = Frame(self.frame_center)
        self.frame_lista_diagnosticos.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        self.lblframe_botones_listdiag = LabelFrame(self.frame_lista_diagnosticos)
        self.lblframe_botones_listdiag.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

        btn_nuevo_diagnostico = tb.Button(self.lblframe_botones_listdiag, text='Nuevo', width=15, bootstyle="success")
        btn_nuevo_diagnostico.grid(row=0, column=0, padx=5, pady=5)
        btn_modificar_diagnostico = tb.Button(self.lblframe_botones_listdiag, text='Modificar', width=15, bootstyle="warning")
        btn_modificar_diagnostico.grid(row=0, column=1, padx=5, pady=5)
        btn_eliminar_diagnostico = tb.Button(self.lblframe_botones_listdiag, text='Eliminar', width=15, bootstyle="danger")
        btn_eliminar_diagnostico.grid(row=0, column=2, padx=5, pady=5)

        self.lblframe_busqueda_listdiag = LabelFrame(self.frame_lista_diagnosticos)
        self.lblframe_busqueda_listdiag.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

        txt_busqueda_diagnosticos = ttk.Entry(self.lblframe_busqueda_listdiag, width=90)
        txt_busqueda_diagnosticos.grid(row=0, column=0, padx=5, pady=5)

        #====================Treeview=====================================

        self.lblframe_tree_listdiag = LabelFrame(self.frame_lista_diagnosticos)
        self.lblframe_tree_listdiag.grid(row=2, column=0, padx=10, pady=10, sticky=NSEW)
        
        columnas = ("DiagnosticoID", "MascotaID", "Fecha", "TipoServicio", "EmpleadoID")

        self.tree_lista_diagnosticos = tb.Treeview(self.lblframe_tree_listdiag, columns=columnas,
                                                height=17, show='headings', bootstyle='dark')
        self.tree_lista_diagnosticos.grid(row=0, column=0, sticky='nsew')

        # Configuración de encabezados de columnas
        self.tree_lista_diagnosticos.heading("DiagnosticoID", text="Diagnóstico ID", anchor=W)
        self.tree_lista_diagnosticos.heading("MascotaID", text="Mascota ID", anchor=W)
        self.tree_lista_diagnosticos.heading("Fecha", text="Fecha", anchor=W)
        self.tree_lista_diagnosticos.heading("TipoServicio", text="Tipo de Servicio", anchor=W)
        self.tree_lista_diagnosticos.heading("EmpleadoID", text="Empleado ID", anchor=W)

        # Mostrar solo las columnas necesarias
        self.tree_lista_diagnosticos['displaycolumns'] = ("DiagnosticoID", "MascotaID", "Fecha", "TipoServicio", "EmpleadoID")

        # Crear Scrollbar
        tree_scroll_listadiag = tb.Scrollbar(self.lblframe_tree_listdiag, orient="vertical", command=self.tree_lista_diagnosticos.yview, bootstyle='round-success')
        tree_scroll_listadiag.grid(row=0, column=1, sticky='ns')
        self.tree_lista_diagnosticos.configure(yscrollcommand=tree_scroll_listadiag.set)

        # Llamamos a nuestra función mostrar diagnósticos
        self.mostrar_diagnosticos()

#FUNCIONES MOSTRAR DATOS ==================
    def mostrar_clientes(self):
        #Capturador errores
        try:
            #Establecer la conexion
            miConexion=sql.connect('DataBase.db')
            #Crear Cursor
            miCursor=miConexion.cursor()
            #Limpiamos nuetro treeview
            registros=self.tree_lista_clientes.get_children()
            #Recorremos cada registro
            for elementos in registros:
                self.tree_lista_clientes.delete(elementos)
            #Consultar nuetra base de datos
            miCursor.execute("SELECT * FROM Cliente")
            #con esto traemos todos los registros y lo guardamos en "datos"
            datos=miCursor.fetchall()
            #Recorremos cada fila encontrada
            for row in datos:
                self.tree_lista_clientes.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
            #Aplicamos Cambios
            miConexion.commit()
            #Cerramos la conexion
            miConexion.close()

        except:
            #Mensaje error
            messagebox.showerror("Lista de Usuario","Ocurrio un error al mostrar las listas de usuario")

    def mostrar_mascotas(self):
        try:
            # Establecer la conexión
            miConexion = sql.connect('DataBase.db')
            # Crear Cursor
            miCursor = miConexion.cursor()
            # Limpiar nuestro treeview
            registros = self.tree_lista_mascotas.get_children()
            # Recorrer cada registro
            for elementos in registros:
                self.tree_lista_mascotas.delete(elementos)
            # Consultar nuestra base de datos
            miCursor.execute("SELECT MascotaID, CodigoMascota, Raza, Nombre, Edad, NumeroIdentidadDueno, Descripcion FROM Mascota")
            # Traer todos los registros y guardarlos en "datos"
            datos = miCursor.fetchall()
            # Recorrer cada fila encontrada
            for row in datos:
                self.tree_lista_mascotas.insert("", 0, text=row[0], values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            # Aplicar cambios
            miConexion.commit()
            # Cerrar la conexión
            miConexion.close()

        except Exception as e:
            # Mensaje de error
            messagebox.showerror("Lista de Mascotas", f"Ocurrió un error al mostrar la lista de mascotas: {str(e)}")

    def mostrar_empleados(self):
        try:
            # Establecer la conexión
            miConexion = sql.connect('DataBase.db')
            # Crear Cursor
            miCursor = miConexion.cursor()
            # Limpiar nuestro treeview
            registros = self.tree_lista_empleados.get_children()
            # Recorrer cada registro
            for elementos in registros:
                self.tree_lista_empleados.delete(elementos)
            # Consultar nuestra base de datos
            miCursor.execute("SELECT EmpleadoID, TipoDocumento, NumeroDocumento, DireccionVivienda, NumeroTelefono, NombreCompleto, CorreoElectronico, FechaContratacion, CargoEnClinica FROM Empleado")
            # Traer todos los registros y guardarlos en "datos"
            datos = miCursor.fetchall()
            # Recorrer cada fila encontrada
            for row in datos:
                self.tree_lista_empleados.insert("", 0, text=row[0], values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            # Aplicar cambios
            miConexion.commit()
            # Cerrar la conexión
            miConexion.close()

        except Exception as e:
            # Mensaje de error
            messagebox.showerror("Lista de Empleados", f"Ocurrió un error al mostrar la lista de empleados: {str(e)}")

    def mostrar_facturas(self):
        try:
            # Establecer la conexión
            miConexion = sql.connect('DataBase.db')
            # Crear Cursor
            miCursor = miConexion.cursor()
            # Limpiar nuestro treeview
            registros = self.tree_lista_facturas.get_children()
            # Recorrer cada registro
            for elementos in registros:
                self.tree_lista_facturas.delete(elementos)
            # Consultar nuestra base de datos
            miCursor.execute("SELECT FacturaID, DiagnosticoID, DescripcionDelServicio, CostoDelServicio FROM Factura")
            # Traer todos los registros y guardarlos en "datos"
            datos = miCursor.fetchall()
            # Recorrer cada fila encontrada
            for row in datos:
                self.tree_lista_facturas.insert("", 0, text=row[0], values=(row[0], row[1], row[2], row[3]))
            # Aplicar cambios
            miConexion.commit()
            # Cerrar la conexión
            miConexion.close()

        except Exception as e:
            # Mensaje de error
            messagebox.showerror("Lista de Facturas", f"Ocurrió un error al mostrar la lista de facturas: {str(e)}")

    def mostrar_diagnosticos(self):
        try:
            # Establecer la conexión
            miConexion = sql.connect('DataBase.db')
            # Crear Cursor
            miCursor = miConexion.cursor()
            # Limpiar nuestro treeview
            registros = self.tree_lista_diagnosticos.get_children()
            # Recorrer cada registro
            for elementos in registros:
                self.tree_lista_diagnosticos.delete(elementos)
            # Consultar nuestra base de datos
            miCursor.execute("SELECT DiagnosticoID, MascotaID, Fecha, TipoServicio, EmpleadoID FROM Diagnostico")
            # Traer todos los registros y guardarlos en "datos"
            datos = miCursor.fetchall()
            # Recorrer cada fila encontrada
            for row in datos:
                self.tree_lista_diagnosticos.insert("", 0, text=row[0], values=(row[0], row[1], row[2], row[3], row[4]))
            # Aplicar cambios
            miConexion.commit()
            # Cerrar la conexión
            miConexion.close()

        except Exception as e:
            # Mensaje de error
            messagebox.showerror("Lista de Diagnósticos", f"Ocurrió un error al mostrar la lista de diagnósticos: {str(e)}")

# # ===================FUNCIONES AGREGAR DATOS======================

    def nuevo_cliente(self):
        # Limpiar el frame derecho antes de agregar el formulario
        for widget in self.frame_right.winfo_children():
            widget.destroy()

        # Etiquetas y campos de entrada del formulario
        lbl_id_cliente = tb.Label(self.frame_right, text="ID Cliente")
        lbl_id_cliente.grid(row=0, column=0, padx=10, pady=10)
        self.id_cliente = tk.StringVar(value=str(random.randint(1000, 9999)))
        entry_id_cliente = tb.Entry(self.frame_right, textvariable=self.id_cliente, state='readonly')
        entry_id_cliente.grid(row=0, column=1, padx=10, pady=10)

        lbl_tipo_documento = tb.Label(self.frame_right, text="Tipo de Documento")
        lbl_tipo_documento.grid(row=1, column=0, padx=10, pady=10)
        self.tipo_documento = tk.StringVar()
        cb_tipo_documento = tb.Combobox(self.frame_right, textvariable=self.tipo_documento)
        cb_tipo_documento['values'] = ('CC', 'CE', 'PS', 'PEP', 'PPT')
        cb_tipo_documento.grid(row=1, column=1, padx=10, pady=10)

        lbl_documento = tb.Label(self.frame_right, text="Documento")
        lbl_documento.grid(row=2, column=0, padx=10, pady=10)
        self.entry_documento = tb.Entry(self.frame_right)
        self.entry_documento.grid(row=2, column=1, padx=10, pady=10)

        lbl_tipo_persona = tb.Label(self.frame_right, text="Tipo de Persona")
        lbl_tipo_persona.grid(row=3, column=0, padx=10, pady=10)
        self.tipo_persona = tk.StringVar()
        cb_tipo_persona = tb.Combobox(self.frame_right, textvariable=self.tipo_persona)
        cb_tipo_persona['values'] = ('Natural', 'Jurídica')
        cb_tipo_persona.grid(row=3, column=1, padx=10, pady=10)

        lbl_nombre = tb.Label(self.frame_right, text="Nombre")
        lbl_nombre.grid(row=4, column=0, padx=10, pady=10)
        self.entry_nombre = tb.Entry(self.frame_right)
        self.entry_nombre.grid(row=4, column=1, padx=10, pady=10)

        lbl_telefono = tb.Label(self.frame_right, text="Teléfono")
        lbl_telefono.grid(row=5, column=0, padx=10, pady=10)
        self.entry_telefono = tb.Entry(self.frame_right)
        self.entry_telefono.grid(row=5, column=1, padx=10, pady=10)

        lbl_correo = tb.Label(self.frame_right, text="Correo")
        lbl_correo.grid(row=6, column=0, padx=10, pady=10)
        self.entry_correo = tb.Entry(self.frame_right)
        self.entry_correo.grid(row=6, column=1, padx=10, pady=10)

        lbl_direccion = tb.Label(self.frame_right, text="Dirección")
        lbl_direccion.grid(row=7, column=0, padx=10, pady=10)
        self.entry_direccion = tb.Entry(self.frame_right)
        self.entry_direccion.grid(row=7, column=1, padx=10, pady=10)

        # Botón Guardar
        btn_guardar = tb.Button(self.frame_right, text='Guardar', bootstyle="success", command=self.guardar_cliente)
        btn_guardar.grid(row=8, column=0, columnspan=2, pady=10)

    def guardar_cliente(self):
        # Obtener los datos del formulario
        id_cliente = self.id_cliente.get()
        tipo_documento = self.tipo_documento.get()
        documento = self.entry_documento.get()
        tipo_persona = self.tipo_persona.get()
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()
        correo = self.entry_correo.get()
        direccion = self.entry_direccion.get()

        # Guardar los datos en la base de datos
        try:
            conn = sql.connect("DataBase.db")
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO cliente (ClienteID, TipoDocumento, NumeroDocumento, TipoPersona, Nombre, Telefono, Correo, DireccionCliente)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (id_cliente, tipo_documento, documento, tipo_persona, nombre, telefono, correo, direccion))
            conn.commit()
            conn.close()
            messagebox.showinfo("Información", "Cliente registrado exitosamente")
            # Limpiar formulario
            self.nuevo_cliente()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al guardar el cliente: {e}")

# ************************

    def nuevo_mascota(self):
        # Limpiar el frame derecho antes de agregar el formulario
        for widget in self.frame_right.winfo_children():
            widget.destroy()

        # Etiquetas y campos de entrada del formulario
        lbl_id_mascota = tb.Label(self.frame_right, text="ID Mascota")
        lbl_id_mascota.grid(row=0, column=0, padx=10, pady=10)
        self.id_mascota = tk.StringVar(value=str(random.randint(1000, 9999)))
        entry_id_mascota = tb.Entry(self.frame_right, textvariable=self.id_mascota, state='readonly')
        entry_id_mascota.grid(row=0, column=1, padx=10, pady=10)

        lbl_codigo_mascota = tb.Label(self.frame_right, text="Código Mascota")
        lbl_codigo_mascota.grid(row=1, column=0, padx=10, pady=10)
        self.entry_codigo_mascota = tb.Entry(self.frame_right)
        self.entry_codigo_mascota.grid(row=1, column=1, padx=10, pady=10)

        lbl_raza = tb.Label(self.frame_right, text="Raza")
        lbl_raza.grid(row=2, column=0, padx=10, pady=10)
        self.entry_raza = tb.Entry(self.frame_right)
        self.entry_raza.grid(row=2, column=1, padx=10, pady=10)

        lbl_nombre = tb.Label(self.frame_right, text="Nombre")
        lbl_nombre.grid(row=3, column=0, padx=10, pady=10)
        self.entry_nombre_mascota = tb.Entry(self.frame_right)
        self.entry_nombre_mascota.grid(row=3, column=1, padx=10, pady=10)

        lbl_edad = tb.Label(self.frame_right, text="Edad")
        lbl_edad.grid(row=4, column=0, padx=10, pady=10)
        self.entry_edad = tb.Entry(self.frame_right)
        self.entry_edad.grid(row=4, column=1, padx=10, pady=10)

        lbl_numero_identidad_dueno = tb.Label(self.frame_right, text="Número Identidad Dueño")
        lbl_numero_identidad_dueno.grid(row=5, column=0, padx=10, pady=10)
        self.entry_numero_identidad_dueno = tb.Entry(self.frame_right)
        self.entry_numero_identidad_dueno.grid(row=5, column=1, padx=10, pady=10)

        lbl_descripcion = tb.Label(self.frame_right, text="Descripción")
        lbl_descripcion.grid(row=6, column=0, padx=10, pady=10)
        self.entry_descripcion = tb.Entry(self.frame_right)
        self.entry_descripcion.grid(row=6, column=1, padx=10, pady=10)

        # Botón Guardar
        btn_guardar = tb.Button(self.frame_right, text='Guardar', bootstyle="success", command=self.guardar_mascota)
        btn_guardar.grid(row=7, column=0, columnspan=2, pady=10)

    def guardar_mascota(self):
        # Obtener los datos del formulario
        id_mascota = self.id_mascota.get()
        codigo_mascota = self.entry_codigo_mascota.get()
        raza = self.entry_raza.get()
        nombre = self.entry_nombre_mascota.get()
        edad = self.entry_edad.get()
        numero_identidad_dueno = self.entry_numero_identidad_dueno.get()
        descripcion = self.entry_descripcion.get()

        # Guardar los datos en la base de datos
        try:
            conn = sql.connect("DataBase.db")
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Mascota (MascotaID, CodigoMascota, Raza, Nombre, Edad, NumeroIdentidadDueno, Descripcion)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (id_mascota, codigo_mascota, raza, nombre, edad, numero_identidad_dueno, descripcion))
            conn.commit()
            conn.close()
            messagebox.showinfo("Información", "Mascota registrada exitosamente")
            # Limpiar formulario
            self.nuevo_mascota()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al guardar la mascota: {e}")


#     def show_new_product_form(self):
#         # Limpiar el frame derecho
#         for widget in self.frame_right.winfo_children():
#             widget.destroy()

#         # Campos del formulario
#         Label(self.frame_right, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
#         name_entry = Entry(self.frame_right)
#         name_entry.grid(row=0, column=1, padx=10, pady=10)
        
#         Label(self.frame_right, text="Descripción").grid(row=1, column=0, padx=10, pady=10)
#         description_entry = Entry(self.frame_right)
#         description_entry.grid(row=1, column=1, padx=10, pady=10)
        
#         Label(self.frame_right, text="Precio").grid(row=2, column=0, padx=10, pady=10)
#         price_entry = Entry(self.frame_right)
#         price_entry.grid(row=2, column=1, padx=10, pady=10)
        
#         Label(self.frame_right, text="Stock").grid(row=3, column=0, padx=10, pady=10)
#         stock_entry = Entry(self.frame_right)
#         stock_entry.grid(row=3, column=1, padx=10, pady=10)
        
#         # Botón para guardar el nuevo producto
#         def save_product():
#             name = name_entry.get()
#             description = description_entry.get()
#             price = price_entry.get()
#             stock = stock_entry.get()
            
#             # Validaciones
#             if not name:
#                 messagebox.showerror("Error", "El nombre es obligatorio")
#                 return
#             if not description:
#                 messagebox.showerror("Error", "La descripción es obligatoria")
#                 return
#             try:
#                 price = float(price)
#             except ValueError:
#                 messagebox.showerror("Error", "El precio debe ser un número válido")
#                 return
#             try:
#                 stock = int(stock)
#             except ValueError:
#                 messagebox.showerror("Error", "El stock debe ser un número entero")
#                 return

#             conn = sql.connect("DataBase.db")
#             cursor = conn.cursor()
            
#             cursor.execute(
#                 '''
#                 INSERT INTO productos (nombre, descripcion, precio, stock)
#                 VALUES (?, ?, ?, ?)
#                 ''', (name, description, price, stock)
#             )
            
#             conn.commit()
#             conn.close()
            
#             messagebox.showinfo("Información", "Producto agregado exitosamente")
#             self.show_new_product_form()  # Limpiar formulario después de agregar
        
#         Button(self.frame_right, text="Guardar", command=save_product).grid(row=4, column=0, columnspan=2, pady=20)

#     def show_new_sale_form(self):
#         # Limpiar el frame derecho
#         for widget in self.frame_right.winfo_children():
#             widget.destroy()

#         # Campos del formulario
#         Label(self.frame_right, text="ID Cliente").grid(row=0, column=0, padx=10, pady=10)
#         id_cliente_entry = Entry(self.frame_right)
#         id_cliente_entry.grid(row=0, column=1, padx=10, pady=10)
        
#         Label(self.frame_right, text="ID Producto").grid(row=1, column=0, padx=10, pady=10)
#         id_producto_entry = Entry(self.frame_right)
#         id_producto_entry.grid(row=1, column=1, padx=10, pady=10)
        
#         Label(self.frame_right, text="Cantidad").grid(row=2, column=0, padx=10, pady=10)
#         cantidad_entry = Entry(self.frame_right)
#         cantidad_entry.grid(row=2, column=1, padx=10, pady=10)
        
#         Label(self.frame_right, text="Fecha (YYYY-MM-DD)").grid(row=3, column=0, padx=10, pady=10)
#         fecha_entry = Entry(self.frame_right)
#         fecha_entry.grid(row=3, column=1, padx=10, pady=10)
        
#         # Botón para guardar la nueva venta
#         def save_sale():
#             id_cliente = id_cliente_entry.get()
#             id_producto = id_producto_entry.get()
#             cantidad = cantidad_entry.get()
#             fecha = fecha_entry.get()
            
#             # Validaciones
#             if not id_cliente:
#                 messagebox.showerror("Error", "El ID del cliente es obligatorio")
#                 return
#             if not id_producto:
#                 messagebox.showerror("Error", "El ID del producto es obligatorio")
#                 return
#             try:
#                 cantidad = int(cantidad)
#             except ValueError:
#                 messagebox.showerror("Error", "La cantidad debe ser un número entero")
#                 return
#             if not fecha:
#                 messagebox.showerror("Error", "La fecha es obligatoria")
#                 return

#             conn = sql.connect("DataBase.db")
#             cursor = conn.cursor()
            
#             cursor.execute(
#                 '''
#                 INSERT INTO ventas (id_cliente, id_producto, cantidad, fecha_venta)
#                 VALUES (?, ?, ?, ?)
#                 ''', (id_cliente, id_producto, cantidad, fecha)
#             )
            
#             conn.commit()
#             conn.close()
            
#             messagebox.showinfo("Información", "Venta registrada exitosamente")
#             self.show_new_sale_form()  # Limpiar formulario después de agregar
        
#         Button(self.frame_right, text="Guardar", command=save_sale).grid(row=4, column=0, columnspan=2, pady=20)


# # ================FUNCIONES MODIFICAR DATOS=======================
#     def show_modify_product_form(self):
#         selected_item = self.tree_lista_productos.selection()
#         if not selected_item:
#             messagebox.showerror("Error", "Selecciona un producto para modificar")
#             return

#         item = self.tree_lista_productos.item(selected_item)
#         product_id = item['values'][0]
#         product_name = item['values'][1]
#         product_description = item['values'][2]
#         product_price = item['values'][3]
#         product_stock = item['values'][4]

#         # Limpiar el frame derecho
#         for widget in self.frame_right.winfo_children():
#             widget.destroy()

#         # Campos del formulario con valores existentes
#         Label(self.frame_right, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
#         name_entry = Entry(self.frame_right)
#         name_entry.grid(row=0, column=1, padx=10, pady=10)
#         name_entry.insert(0, product_name)
        
#         Label(self.frame_right, text="Descripción").grid(row=1, column=0, padx=10, pady=10)
#         description_entry = Entry(self.frame_right)
#         description_entry.grid(row=1, column=1, padx=10, pady=10)
#         description_entry.insert(0, product_description)
        
#         Label(self.frame_right, text="Precio").grid(row=2, column=0, padx=10, pady=10)
#         price_entry = Entry(self.frame_right)
#         price_entry.grid(row=2, column=1, padx=10, pady=10)
#         price_entry.insert(0, product_price)
        
#         Label(self.frame_right, text="Stock").grid(row=3, column=0, padx=10, pady=10)
#         stock_entry = Entry(self.frame_right)
#         stock_entry.grid(row=3, column=1, padx=10, pady=10)
#         stock_entry.insert(0, product_stock)
        
#         # Botón para guardar los cambios del producto
#         def save_modified_product():
#             name = name_entry.get()
#             description = description_entry.get()
#             price = price_entry.get()
#             stock = stock_entry.get()
            
#             # Validaciones
#             if not name:
#                 messagebox.showerror("Error", "El nombre es obligatorio")
#                 return
#             if not description:
#                 messagebox.showerror("Error", "La descripción es obligatoria")
#                 return
#             try:
#                 price = float(price)
#             except ValueError:
#                 messagebox.showerror("Error", "El precio debe ser un número válido")
#                 return
#             try:
#                 stock = int(stock)
#             except ValueError:
#                 messagebox.showerror("Error", "El stock debe ser un número entero")
#                 return

#             conn = sql.connect("DataBase.db")
#             cursor = conn.cursor()
            
#             cursor.execute(
#                 '''
#                 UPDATE productos
#                 SET nombre = ?, descripcion = ?, precio = ?, stock = ?
#                 WHERE id_producto = ?
#                 ''', (name, description, price, stock, product_id)
#             )
            
#             conn.commit()
#             conn.close()
            
#             messagebox.showinfo("Información", "Producto modificado exitosamente")
#             self.mostrar_productos()
#             self.frame_right.destroy()  # Ocultar el formulario después de modificar
        
#         Button(self.frame_right, text="Guardar", command=save_modified_product).grid(row=4, column=0, columnspan=2, pady=20)

# # ==================FUNCIONES ELIMINAR DATOS=====================
    # def delete_product(self):
    #     selected_item = self.tree_lista_productos.selection()
    #     if not selected_item:
    #         messagebox.showerror("Error", "Selecciona un producto para eliminar")
    #         return

    #     item = self.tree_lista_productos.item(selected_item)
    #     product_id = item['values'][0]

    #     # Confirmación antes de eliminar
    #     confirm = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este producto?")
    #     if not confirm:
    #         return

    #     try:
    #         conn = sql.connect("DataBase.db")
    #         cursor = conn.cursor()
            
    #         cursor.execute(
    #             '''
    #             DELETE FROM productos
    #             WHERE id_producto = ?
    #             ''', (product_id,)
    #         )
            
    #         conn.commit()
    #         conn.close()
            
    #         messagebox.showinfo("Información", "Producto eliminado exitosamente")
    #         self.mostrar_productos()
    #     except Exception as e:
    #         messagebox.showerror("Error", f"Ocurrió un error al eliminar el producto: {e}")


#Gestiones DB
    
#Creacion BD


# ******************************** Inicio ********************
def main():
    app=Ventana()
    app.title('Mascotas Felices') #Titulo de la ventana
    app.state('zoomed') #zoomed inicia la ventana maximizada
    tb.Style('superhero') #Themes: solar, superhero, darkly, cyborg, vapor - https://ttkbootstrap.readthedocs.io/en/latest/themes/dark/
    app.mainloop()

    

if __name__=='__main__':
        #createDB()
        #createTable()
        #insert_values()
        main()