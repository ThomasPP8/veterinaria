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
        btn_modificar_cliente=tb.Button(self.lblframe_botones_listclient,text='Modificar',width=15,bootstyle="warning", command=self.modificar_cliente)
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
        btn_modificar_mascota = tb.Button(self.lblframe_botones_listpet, text='Modificar', width=15, bootstyle="warning", command=self.modificar_mascota)
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

        btn_nuevo_empleado = tb.Button(self.lblframe_botones_listemp, text='Nuevo', width=15, bootstyle="success", command=self.nuevo_empleado)
        btn_nuevo_empleado.grid(row=0, column=0, padx=5, pady=5)
        btn_modificar_empleado = tb.Button(self.lblframe_botones_listemp, text='Modificar', width=15, bootstyle="warning", command=self.modificar_empleado)
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

        btn_nueva_factura = tb.Button(self.lblframe_botones_listfac, text='Nueva', width=15, bootstyle="success", command=self.nuevo_factura)
        btn_nueva_factura.grid(row=0, column=0, padx=5, pady=5)
        btn_modificar_factura = tb.Button(self.lblframe_botones_listfac, text='Modificar', width=15, bootstyle="warning", command=self.modificar_factura)
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

        btn_nuevo_diagnostico = tb.Button(self.lblframe_botones_listdiag, text='Nuevo', width=15, bootstyle="success", command=self.nuevo_diagnostico)
        btn_nuevo_diagnostico.grid(row=0, column=0, padx=5, pady=5)
        btn_modificar_diagnostico = tb.Button(self.lblframe_botones_listdiag, text='Modificar', width=15, bootstyle="warning", command=self.modificar_diagnostico)
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

# ***********************

    def nuevo_mascota(self):
        # Limpiar el frame derecho antes de agregar el formulario
        for widget in self.frame_right.winfo_children():
            widget.destroy()

        # Generar código de mascota aleatorio
        codigo_mascota = f"M{random.randint(100, 999)}"

        # Etiquetas y campos de entrada del formulario
        lbl_id_mascota = tb.Label(self.frame_right, text="ID Mascota")
        lbl_id_mascota.grid(row=0, column=0, padx=10, pady=10)
        self.id_mascota = tk.StringVar(value=str(random.randint(1000, 9999)))
        entry_id_mascota = tb.Entry(self.frame_right, textvariable=self.id_mascota, state='readonly')
        entry_id_mascota.grid(row=0, column=1, padx=10, pady=10)

        lbl_codigo_mascota = tb.Label(self.frame_right, text="Código Mascota")
        lbl_codigo_mascota.grid(row=1, column=0, padx=10, pady=10)
        self.entry_codigo_mascota = tk.StringVar(value=codigo_mascota)
        entry_codigo_mascota = tb.Entry(self.frame_right, textvariable=self.entry_codigo_mascota, state='readonly')
        entry_codigo_mascota.grid(row=1, column=1, padx=10, pady=10)

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

# ***********************

    def nuevo_empleado(self):
        # Limpiar el frame derecho antes de agregar el formulario
        for widget in self.frame_right.winfo_children():
            widget.destroy()

        # Etiquetas y campos de entrada del formulario
        lbl_id_empleado = tb.Label(self.frame_right, text="ID Empleado")
        lbl_id_empleado.grid(row=0, column=0, padx=10, pady=10)
        self.id_empleado = tk.StringVar(value=str(random.randint(1000, 9999)))
        entry_id_empleado = tb.Entry(self.frame_right, textvariable=self.id_empleado, state='readonly')
        entry_id_empleado.grid(row=0, column=1, padx=10, pady=10)

        lbl_tipo_documento = tb.Label(self.frame_right, text="Tipo de Documento")
        lbl_tipo_documento.grid(row=1, column=0, padx=10, pady=10)
        self.tipo_documento = tk.StringVar()
        cb_tipo_documento = tb.Combobox(self.frame_right, textvariable=self.tipo_documento)
        cb_tipo_documento['values'] = ('CC', 'CE', 'PS', 'PEP', 'PPT')
        cb_tipo_documento.grid(row=1, column=1, padx=10, pady=10)

        lbl_numero_documento = tb.Label(self.frame_right, text="Número de Documento")
        lbl_numero_documento.grid(row=2, column=0, padx=10, pady=10)
        self.entry_numero_documento = tb.Entry(self.frame_right)
        self.entry_numero_documento.grid(row=2, column=1, padx=10, pady=10)

        lbl_direccion_vivienda = tb.Label(self.frame_right, text="Dirección de Vivienda")
        lbl_direccion_vivienda.grid(row=3, column=0, padx=10, pady=10)
        self.entry_direccion_vivienda = tb.Entry(self.frame_right)
        self.entry_direccion_vivienda.grid(row=3, column=1, padx=10, pady=10)

        lbl_numero_telefono = tb.Label(self.frame_right, text="Número de Teléfono")
        lbl_numero_telefono.grid(row=4, column=0, padx=10, pady=10)
        self.entry_numero_telefono = tb.Entry(self.frame_right)
        self.entry_numero_telefono.grid(row=4, column=1, padx=10, pady=10)

        lbl_nombre_completo = tb.Label(self.frame_right, text="Nombre Completo")
        lbl_nombre_completo.grid(row=5, column=0, padx=10, pady=10)
        self.entry_nombre_completo = tb.Entry(self.frame_right)
        self.entry_nombre_completo.grid(row=5, column=1, padx=10, pady=10)

        lbl_correo_electronico = tb.Label(self.frame_right, text="Correo Electrónico")
        lbl_correo_electronico.grid(row=6, column=0, padx=10, pady=10)
        self.entry_correo_electronico = tb.Entry(self.frame_right)
        self.entry_correo_electronico.grid(row=6, column=1, padx=10, pady=10)

        lbl_fecha_contratacion = tb.Label(self.frame_right, text="Fecha de Contratación")
        lbl_fecha_contratacion.grid(row=7, column=0, padx=10, pady=10)
        self.entry_fecha_contratacion = tb.Entry(self.frame_right)
        self.entry_fecha_contratacion.grid(row=7, column=1, padx=10, pady=10)

        lbl_cargo_en_clinica = tb.Label(self.frame_right, text="Cargo en Clínica")
        lbl_cargo_en_clinica.grid(row=8, column=0, padx=10, pady=10)
        self.entry_cargo_en_clinica = tb.Entry(self.frame_right)
        self.entry_cargo_en_clinica.grid(row=8, column=1, padx=10, pady=10)

        # Botón Guardar
        btn_guardar = tb.Button(self.frame_right, text='Guardar', bootstyle="success", command=self.guardar_empleado)
        btn_guardar.grid(row=9, column=0, columnspan=2, pady=10)

    def guardar_empleado(self):
        # Obtener los datos del formulario
        id_empleado = self.id_empleado.get()
        tipo_documento = self.tipo_documento.get()
        numero_documento = self.entry_numero_documento.get()
        direccion_vivienda = self.entry_direccion_vivienda.get()
        numero_telefono = self.entry_numero_telefono.get()
        nombre_completo = self.entry_nombre_completo.get()
        correo_electronico = self.entry_correo_electronico.get()
        fecha_contratacion = self.entry_fecha_contratacion.get()
        cargo_en_clinica = self.entry_cargo_en_clinica.get()

        # Guardar los datos en la base de datos
        try:
            conn = sql.connect("DataBase.db")
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Empleado (EmpleadoID, TipoDocumento, NumeroDocumento, DireccionVivienda, NumeroTelefono, NombreCompleto, CorreoElectronico, FechaContratacion, CargoEnClinica)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (id_empleado, tipo_documento, numero_documento, direccion_vivienda, numero_telefono, nombre_completo, correo_electronico, fecha_contratacion, cargo_en_clinica))
            conn.commit()
            conn.close()
            messagebox.showinfo("Información", "Empleado registrado exitosamente")
            # Limpiar formulario
            self.nuevo_empleado()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al guardar el empleado: {e}")

# ***********************

    def nuevo_diagnostico(self):
        # Limpiar el frame derecho antes de agregar el formulario
        for widget in self.frame_right.winfo_children():
            widget.destroy()

        # Etiquetas y campos de entrada del formulario
        lbl_id_diagnostico = tb.Label(self.frame_right, text="ID Diagnóstico")
        lbl_id_diagnostico.grid(row=0, column=0, padx=10, pady=10)
        self.id_diagnostico = tk.StringVar(value=str(random.randint(1000, 9999)))
        entry_id_diagnostico = tb.Entry(self.frame_right, textvariable=self.id_diagnostico, state='readonly')
        entry_id_diagnostico.grid(row=0, column=1, padx=10, pady=10)

        lbl_mascota_id = tb.Label(self.frame_right, text="ID Mascota")
        lbl_mascota_id.grid(row=1, column=0, padx=10, pady=10)
        self.entry_mascota_id = tb.Entry(self.frame_right)
        self.entry_mascota_id.grid(row=1, column=1, padx=10, pady=10)

        lbl_fecha = tb.Label(self.frame_right, text="Fecha")
        lbl_fecha.grid(row=2, column=0, padx=10, pady=10)
        self.entry_fecha = tb.Entry(self.frame_right)
        self.entry_fecha.grid(row=2, column=1, padx=10, pady=10)

        lbl_tipo_servicio = tb.Label(self.frame_right, text="Tipo de Servicio")
        lbl_tipo_servicio.grid(row=3, column=0, padx=10, pady=10)
        self.entry_tipo_servicio = tb.Entry(self.frame_right)
        self.entry_tipo_servicio.grid(row=3, column=1, padx=10, pady=10)

        lbl_empleado_id = tb.Label(self.frame_right, text="ID Empleado")
        lbl_empleado_id.grid(row=4, column=0, padx=10, pady=10)
        self.entry_empleado_id = tb.Entry(self.frame_right)
        self.entry_empleado_id.grid(row=4, column=1, padx=10, pady=10)

        # Botón Guardar
        btn_guardar = tb.Button(self.frame_right, text='Guardar', bootstyle="success", command=self.guardar_diagnostico)
        btn_guardar.grid(row=5, column=0, columnspan=2, pady=10)

    def guardar_diagnostico(self):
        # Obtener los datos del formulario
        id_diagnostico = self.id_diagnostico.get()
        mascota_id = self.entry_mascota_id.get()
        fecha = self.entry_fecha.get()
        tipo_servicio = self.entry_tipo_servicio.get()
        empleado_id = self.entry_empleado_id.get()

        # Verificar si el ID de mascota y empleado existen
        try:
            conn = sql.connect("DataBase.db")
            cursor = conn.cursor()
            
            # Verificar existencia de mascota
            cursor.execute("SELECT COUNT(*) FROM Mascota WHERE MascotaID=?", (mascota_id,))
            if cursor.fetchone()[0] == 0:
                messagebox.showerror("Error", "El ID de mascota no existe.")
                conn.close()
                return
            
            # Verificar existencia de empleado
            cursor.execute("SELECT COUNT(*) FROM Empleado WHERE EmpleadoID=?", (empleado_id,))
            if cursor.fetchone()[0] == 0:
                messagebox.showerror("Error", "El ID de empleado no existe.")
                conn.close()
                return

            # Guardar los datos en la base de datos
            cursor.execute('''
                INSERT INTO Diagnostico (DiagnosticoID, MascotaID, Fecha, TipoServicio, EmpleadoID)
                VALUES (?, ?, ?, ?, ?)
            ''', (id_diagnostico, mascota_id, fecha, tipo_servicio, empleado_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Información", "Diagnóstico registrado exitosamente")
            # Limpiar formulario
            self.nuevo_diagnostico()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al guardar el diagnóstico: {e}")

# ***********************

    def nuevo_factura(self):
        # Limpiar el frame derecho antes de agregar el formulario
        for widget in self.frame_right.winfo_children():
            widget.destroy()

        # Etiquetas y campos de entrada del formulario
        lbl_id_factura = tb.Label(self.frame_right, text="ID Factura")
        lbl_id_factura.grid(row=0, column=0, padx=10, pady=10)
        self.id_factura = tk.StringVar(value=str(random.randint(1000, 9999)))
        entry_id_factura = tb.Entry(self.frame_right, textvariable=self.id_factura, state='readonly')
        entry_id_factura.grid(row=0, column=1, padx=10, pady=10)

        lbl_diagnostico_id = tb.Label(self.frame_right, text="ID Diagnóstico")
        lbl_diagnostico_id.grid(row=1, column=0, padx=10, pady=10)
        self.entry_diagnostico_id = tb.Entry(self.frame_right)
        self.entry_diagnostico_id.grid(row=1, column=1, padx=10, pady=10)

        lbl_descripcion_servicio = tb.Label(self.frame_right, text="Descripción del Servicio")
        lbl_descripcion_servicio.grid(row=2, column=0, padx=10, pady=10)
        self.entry_descripcion_servicio = tb.Entry(self.frame_right)
        self.entry_descripcion_servicio.grid(row=2, column=1, padx=10, pady=10)

        lbl_costo_servicio = tb.Label(self.frame_right, text="Costo del Servicio")
        lbl_costo_servicio.grid(row=3, column=0, padx=10, pady=10)
        self.entry_costo_servicio = tb.Entry(self.frame_right)
        self.entry_costo_servicio.grid(row=3, column=1, padx=10, pady=10)

        # Botón Guardar
        btn_guardar = tb.Button(self.frame_right, text='Guardar', bootstyle="success", command=self.guardar_factura)
        btn_guardar.grid(row=4, column=0, columnspan=2, pady=10)

    def guardar_factura(self):
        # Obtener los datos del formulario
        id_factura = self.id_factura.get()
        diagnostico_id = self.entry_diagnostico_id.get()
        descripcion_servicio = self.entry_descripcion_servicio.get()
        costo_servicio = self.entry_costo_servicio.get()

        # Verificar si el ID de diagnóstico existe
        try:
            conn = sql.connect("DataBase.db")
            cursor = conn.cursor()
            
            # Verificar existencia de diagnóstico
            cursor.execute("SELECT COUNT(*) FROM Diagnostico WHERE DiagnosticoID=?", (diagnostico_id,))
            if cursor.fetchone()[0] == 0:
                messagebox.showerror("Error", "El ID de diagnóstico no existe.")
                conn.close()
                return

            # Guardar los datos en la base de datos
            cursor.execute('''
                INSERT INTO Factura (FacturaID, DiagnosticoID, DescripcionDelServicio, CostoDelServicio)
                VALUES (?, ?, ?, ?)
            ''', (id_factura, diagnostico_id, descripcion_servicio, costo_servicio))
            conn.commit()
            conn.close()
            messagebox.showinfo("Información", "Factura registrada exitosamente")
            # Limpiar formulario
            self.nuevo_factura()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al guardar la factura: {e}")

# # ================FUNCIONES MODIFICAR DATOS=======================

    def modificar_cliente(self):
        # Obtener la selección actual del Treeview
        selected_item = self.tree_lista_clientes.selection()
        if not selected_item:
            messagebox.showerror("Error", "Selecciona un cliente para modificar")
            return

        # Obtener los datos del cliente seleccionado
        item = self.tree_lista_clientes.item(selected_item)
        cliente_id = item['values'][0]

        # Obtener los datos del cliente desde la base de datos
        conn = sql.connect("DataBase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cliente WHERE ClienteID=?", (cliente_id,))
        cliente = cursor.fetchone()
        conn.close()

        if not cliente:
            messagebox.showerror("Error", "No se encontró el cliente")
            return

        # Limpiar el frame derecho antes de agregar el formulario
        for widget in self.frame_right.winfo_children():
            widget.destroy()

        # Etiquetas y campos de entrada del formulario
        self.cliente_id = cliente[0]

        lbl_tipo_documento = tb.Label(self.frame_right, text="Tipo de Documento")
        lbl_tipo_documento.grid(row=0, column=0, padx=10, pady=10)
        self.tipo_documento = tk.StringVar(value=cliente[1])
        cb_tipo_documento = tb.Combobox(self.frame_right, textvariable=self.tipo_documento)
        cb_tipo_documento['values'] = ('CC', 'CE', 'PS', 'PEP', 'PPT')
        cb_tipo_documento.grid(row=0, column=1, padx=10, pady=10)

        lbl_documento = tb.Label(self.frame_right, text="Número de Documento")
        lbl_documento.grid(row=1, column=0, padx=10, pady=10)
        self.entry_documento = tb.Entry(self.frame_right)
        self.entry_documento.grid(row=1, column=1, padx=10, pady=10)
        self.entry_documento.insert(0, cliente[2])

        lbl_tipo_persona = tb.Label(self.frame_right, text="Tipo de Persona")
        lbl_tipo_persona.grid(row=2, column=0, padx=10, pady=10)
        self.tipo_persona = tk.StringVar(value=cliente[3])
        cb_tipo_persona = tb.Combobox(self.frame_right, textvariable=self.tipo_persona)
        cb_tipo_persona['values'] = ('Natural', 'Jurídica')
        cb_tipo_persona.grid(row=2, column=1, padx=10, pady=10)

        lbl_nombre = tb.Label(self.frame_right, text="Nombre")
        lbl_nombre.grid(row=3, column=0, padx=10, pady=10)
        self.entry_nombre = tb.Entry(self.frame_right)
        self.entry_nombre.grid(row=3, column=1, padx=10, pady=10)
        self.entry_nombre.insert(0, cliente[4])

        lbl_telefono = tb.Label(self.frame_right, text="Teléfono")
        lbl_telefono.grid(row=4, column=0, padx=10, pady=10)
        self.entry_telefono = tb.Entry(self.frame_right)
        self.entry_telefono.grid(row=4, column=1, padx=10, pady=10)
        self.entry_telefono.insert(0, cliente[5])

        lbl_correo = tb.Label(self.frame_right, text="Correo")
        lbl_correo.grid(row=5, column=0, padx=10, pady=10)
        self.entry_correo = tb.Entry(self.frame_right)
        self.entry_correo.grid(row=5, column=1, padx=10, pady=10)
        self.entry_correo.insert(0, cliente[6])

        lbl_direccion = tb.Label(self.frame_right, text="Dirección")
        lbl_direccion.grid(row=6, column=0, padx=10, pady=10)
        self.entry_direccion = tb.Entry(self.frame_right)
        self.entry_direccion.grid(row=6, column=1, padx=10, pady=10)
        self.entry_direccion.insert(0, cliente[7])

        # Botón Guardar
        btn_guardar = tb.Button(self.frame_right, text='Guardar Cambios', bootstyle="success", command=self.guardar_cambios_cliente)
        btn_guardar.grid(row=7, column=0, columnspan=2, pady=10)

    def guardar_cambios_cliente(self):
        # Obtener los datos del formulario
        tipo_documento = self.tipo_documento.get()
        numero_documento = self.entry_documento.get()
        tipo_persona = self.tipo_persona.get()
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()
        correo = self.entry_correo.get()
        direccion = self.entry_direccion.get()

        # Actualizar los datos en la base de datos
        try:
            conn = sql.connect("DataBase.db")
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Cliente
                SET TipoDocumento = ?, NumeroDocumento = ?, TipoPersona = ?, Nombre = ?, Telefono = ?, Correo = ?, DireccionCliente = ?
                WHERE ClienteID = ?
            ''', (tipo_documento, numero_documento, tipo_persona, nombre, telefono, correo, direccion, self.cliente_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Información", "Cliente modificado exitosamente")
            # Actualizar la vista de la lista de clientes
            self.mostrar_clientes()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al modificar el cliente: {e}")

# =============

    def modificar_mascota(self):
        # Obtener la selección actual del Treeview
        selected_item = self.tree_lista_mascotas.selection()
        if not selected_item:
            messagebox.showerror("Error", "Selecciona una mascota para modificar")
            return

        # Obtener los datos de la mascota seleccionada
        item = self.tree_lista_mascotas.item(selected_item)
        mascota_id = item['values'][0]

        # Obtener los datos de la mascota desde la base de datos
        conn = sql.connect("DataBase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Mascota WHERE MascotaID=?", (mascota_id,))
        mascota = cursor.fetchone()
        conn.close()

        if not mascota:
            messagebox.showerror("Error", "No se encontró la mascota")
            return

        # Limpiar el frame derecho antes de agregar el formulario
        for widget in self.frame_right.winfo_children():
            widget.destroy()

        # Etiquetas y campos de entrada del formulario
        self.mascota_id = mascota[0]

        lbl_codigo_mascota = tb.Label(self.frame_right, text="Código Mascota")
        lbl_codigo_mascota.grid(row=0, column=0, padx=10, pady=10)
        self.codigo_mascota = tk.StringVar(value=mascota[1])
        entry_codigo_mascota = tb.Entry(self.frame_right, textvariable=self.codigo_mascota, state='readonly')
        entry_codigo_mascota.grid(row=0, column=1, padx=10, pady=10)

        lbl_raza = tb.Label(self.frame_right, text="Raza")
        lbl_raza.grid(row=1, column=0, padx=10, pady=10)
        self.entry_raza = tb.Entry(self.frame_right)
        self.entry_raza.grid(row=1, column=1, padx=10, pady=10)
        self.entry_raza.insert(0, mascota[2])

        lbl_nombre = tb.Label(self.frame_right, text="Nombre")
        lbl_nombre.grid(row=2, column=0, padx=10, pady=10)
        self.entry_nombre = tb.Entry(self.frame_right)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10)
        self.entry_nombre.insert(0, mascota[3])

        lbl_edad = tb.Label(self.frame_right, text="Edad")
        lbl_edad.grid(row=3, column=0, padx=10, pady=10)
        self.entry_edad = tb.Entry(self.frame_right)
        self.entry_edad.grid(row=3, column=1, padx=10, pady=10)
        self.entry_edad.insert(0, mascota[4])

        lbl_numero_identidad_dueno = tb.Label(self.frame_right, text="Número Identidad Dueño")
        lbl_numero_identidad_dueno.grid(row=4, column=0, padx=10, pady=10)
        self.entry_numero_identidad_dueno = tb.Entry(self.frame_right)
        self.entry_numero_identidad_dueno.grid(row=4, column=1, padx=10, pady=10)
        self.entry_numero_identidad_dueno.insert(0, mascota[5])

        lbl_descripcion = tb.Label(self.frame_right, text="Descripción")
        lbl_descripcion.grid(row=5, column=0, padx=10, pady=10)
        self.entry_descripcion = tb.Entry(self.frame_right)
        self.entry_descripcion.grid(row=5, column=1, padx=10, pady=10)
        self.entry_descripcion.insert(0, mascota[6])

        # Botón Guardar
        btn_guardar = tb.Button(self.frame_right, text='Guardar Cambios', bootstyle="success", command=self.guardar_cambios_mascota)
        btn_guardar.grid(row=6, column=0, columnspan=2, pady=10)

    def guardar_cambios_mascota(self):
        # Obtener los datos del formulario
        raza = self.entry_raza.get()
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        numero_identidad_dueno = self.entry_numero_identidad_dueno.get()
        descripcion = self.entry_descripcion.get()

        # Actualizar los datos en la base de datos
        try:
            conn = sql.connect("DataBase.db")
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Mascota
                SET Raza = ?, Nombre = ?, Edad = ?, NumeroIdentidadDueno = ?, Descripcion = ?
                WHERE MascotaID = ?
            ''', (raza, nombre, edad, numero_identidad_dueno, descripcion, self.mascota_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Información", "Mascota modificada exitosamente")
            # Actualizar la vista de la lista de mascotas
            self.mostrar_mascotas()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al modificar la mascota: {e}")

# =============

    def modificar_empleado(self):
        # Obtener la selección actual del Treeview
        selected_item = self.tree_lista_empleados.selection()
        if not selected_item:
            messagebox.showerror("Error", "Selecciona un empleado para modificar")
            return

        # Obtener los datos del empleado seleccionado
        item = self.tree_lista_empleados.item(selected_item)
        empleado_id = item['values'][0]

        # Obtener los datos del empleado desde la base de datos
        conn = sql.connect("DataBase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Empleado WHERE EmpleadoID=?", (empleado_id,))
        empleado = cursor.fetchone()
        conn.close()

        if not empleado:
            messagebox.showerror("Error", "No se encontró el empleado")
            return

        # Limpiar el frame derecho antes de agregar el formulario
        for widget in self.frame_right.winfo_children():
            widget.destroy()

        # Etiquetas y campos de entrada del formulario
        self.empleado_id = empleado[0]

        lbl_tipo_documento = tb.Label(self.frame_right, text="Tipo de Documento")
        lbl_tipo_documento.grid(row=0, column=0, padx=10, pady=10)
        self.tipo_documento = tk.StringVar(value=empleado[1])
        cb_tipo_documento = tb.Combobox(self.frame_right, textvariable=self.tipo_documento)
        cb_tipo_documento['values'] = ('CC', 'CE', 'PS', 'PEP', 'PPT')
        cb_tipo_documento.grid(row=0, column=1, padx=10, pady=10)

        lbl_numero_documento = tb.Label(self.frame_right, text="Número de Documento")
        lbl_numero_documento.grid(row=1, column=0, padx=10, pady=10)
        self.entry_numero_documento = tb.Entry(self.frame_right)
        self.entry_numero_documento.grid(row=1, column=1, padx=10, pady=10)
        self.entry_numero_documento.insert(0, empleado[2])

        lbl_direccion_vivienda = tb.Label(self.frame_right, text="Dirección de Vivienda")
        lbl_direccion_vivienda.grid(row=2, column=0, padx=10, pady=10)
        self.entry_direccion_vivienda = tb.Entry(self.frame_right)
        self.entry_direccion_vivienda.grid(row=2, column=1, padx=10, pady=10)
        self.entry_direccion_vivienda.insert(0, empleado[3])

        lbl_numero_telefono = tb.Label(self.frame_right, text="Número de Teléfono")
        lbl_numero_telefono.grid(row=3, column=0, padx=10, pady=10)
        self.entry_numero_telefono = tb.Entry(self.frame_right)
        self.entry_numero_telefono.grid(row=3, column=1, padx=10, pady=10)
        self.entry_numero_telefono.insert(0, empleado[4])

        lbl_nombre_completo = tb.Label(self.frame_right, text="Nombre Completo")
        lbl_nombre_completo.grid(row=4, column=0, padx=10, pady=10)
        self.entry_nombre_completo = tb.Entry(self.frame_right)
        self.entry_nombre_completo.grid(row=4, column=1, padx=10, pady=10)
        self.entry_nombre_completo.insert(0, empleado[5])

        lbl_correo_electronico = tb.Label(self.frame_right, text="Correo Electrónico")
        lbl_correo_electronico.grid(row=5, column=0, padx=10, pady=10)
        self.entry_correo_electronico = tb.Entry(self.frame_right)
        self.entry_correo_electronico.grid(row=5, column=1, padx=10, pady=10)
        self.entry_correo_electronico.insert(0, empleado[6])

        lbl_fecha_contratacion = tb.Label(self.frame_right, text="Fecha de Contratación")
        lbl_fecha_contratacion.grid(row=6, column=0, padx=10, pady=10)
        self.entry_fecha_contratacion = tb.Entry(self.frame_right)
        self.entry_fecha_contratacion.grid(row=6, column=1, padx=10, pady=10)
        self.entry_fecha_contratacion.insert(0, empleado[7])

        lbl_cargo_en_clinica = tb.Label(self.frame_right, text="Cargo en Clínica")
        lbl_cargo_en_clinica.grid(row=7, column=0, padx=10, pady=10)
        self.entry_cargo_en_clinica = tb.Entry(self.frame_right)
        self.entry_cargo_en_clinica.grid(row=7, column=1, padx=10, pady=10)
        self.entry_cargo_en_clinica.insert(0, empleado[8])

        # Botón Guardar
        btn_guardar = tb.Button(self.frame_right, text='Guardar Cambios', bootstyle="success", command=self.guardar_cambios_empleado)
        btn_guardar.grid(row=8, column=0, columnspan=2, pady=10)

    def guardar_cambios_empleado(self):
        # Obtener los datos del formulario
        tipo_documento = self.tipo_documento.get()
        numero_documento = self.entry_numero_documento.get()
        direccion_vivienda = self.entry_direccion_vivienda.get()
        numero_telefono = self.entry_numero_telefono.get()
        nombre_completo = self.entry_nombre_completo.get()
        correo_electronico = self.entry_correo_electronico.get()
        fecha_contratacion = self.entry_fecha_contratacion.get()
        cargo_en_clinica = self.entry_cargo_en_clinica.get()

        # Actualizar los datos en la base de datos
        try:
            conn = sql.connect("DataBase.db")
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Empleado
                SET TipoDocumento = ?, NumeroDocumento = ?, DireccionVivienda = ?, NumeroTelefono = ?, NombreCompleto = ?, CorreoElectronico = ?, FechaContratacion = ?, CargoEnClinica = ?
                WHERE EmpleadoID = ?
            ''', (tipo_documento, numero_documento, direccion_vivienda, numero_telefono, nombre_completo, correo_electronico, fecha_contratacion, cargo_en_clinica, self.empleado_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Información", "Empleado modificado exitosamente")
            # Actualizar la vista de la lista de empleados
            self.mostrar_empleados()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al modificar el empleado: {e}")

# ============

    def modificar_diagnostico(self):
        # Obtener la selección actual del Treeview
        selected_item = self.tree_lista_diagnosticos.selection()
        if not selected_item:
            messagebox.showerror("Error", "Selecciona un diagnóstico para modificar")
            return

        # Obtener los datos del diagnóstico seleccionado
        item = self.tree_lista_diagnosticos.item(selected_item)
        diagnostico_id = item['values'][0]

        # Obtener los datos del diagnóstico desde la base de datos
        conn = sql.connect("DataBase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Diagnostico WHERE DiagnosticoID=?", (diagnostico_id,))
        diagnostico = cursor.fetchone()
        conn.close()

        if not diagnostico:
            messagebox.showerror("Error", "No se encontró el diagnóstico")
            return

        # Limpiar el frame derecho antes de agregar el formulario
        for widget in self.frame_right.winfo_children():
            widget.destroy()

        # Etiquetas y campos de entrada del formulario
        self.diagnostico_id = diagnostico[0]

        lbl_mascota_id = tb.Label(self.frame_right, text="ID Mascota")
        lbl_mascota_id.grid(row=0, column=0, padx=10, pady=10)
        self.entry_mascota_id = tb.Entry(self.frame_right)
        self.entry_mascota_id.grid(row=0, column=1, padx=10, pady=10)
        self.entry_mascota_id.insert(0, diagnostico[1])

        lbl_fecha = tb.Label(self.frame_right, text="Fecha")
        lbl_fecha.grid(row=1, column=0, padx=10, pady=10)
        self.entry_fecha = tb.Entry(self.frame_right)
        self.entry_fecha.grid(row=1, column=1, padx=10, pady=10)
        self.entry_fecha.insert(0, diagnostico[2])

        lbl_tipo_servicio = tb.Label(self.frame_right, text="Tipo de Servicio")
        lbl_tipo_servicio.grid(row=2, column=0, padx=10, pady=10)
        self.entry_tipo_servicio = tb.Entry(self.frame_right)
        self.entry_tipo_servicio.grid(row=2, column=1, padx=10, pady=10)
        self.entry_tipo_servicio.insert(0, diagnostico[3])

        lbl_empleado_id = tb.Label(self.frame_right, text="ID Empleado")
        lbl_empleado_id.grid(row=3, column=0, padx=10, pady=10)
        self.entry_empleado_id = tb.Entry(self.frame_right)
        self.entry_empleado_id.grid(row=3, column=1, padx=10, pady=10)
        self.entry_empleado_id.insert(0, diagnostico[4])

        # Botón Guardar
        btn_guardar = tb.Button(self.frame_right, text='Guardar Cambios', bootstyle="success", command=self.guardar_cambios_diagnostico)
        btn_guardar.grid(row=4, column=0, columnspan=2, pady=10)

    def guardar_cambios_diagnostico(self):
        # Obtener los datos del formulario
        mascota_id = self.entry_mascota_id.get()
        fecha = self.entry_fecha.get()
        tipo_servicio = self.entry_tipo_servicio.get()
        empleado_id = self.entry_empleado_id.get()

        # Actualizar los datos en la base de datos
        try:
            conn = sql.connect("DataBase.db")
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Diagnostico
                SET MascotaID = ?, Fecha = ?, TipoServicio = ?, EmpleadoID = ?
                WHERE DiagnosticoID = ?
            ''', (mascota_id, fecha, tipo_servicio, empleado_id, self.diagnostico_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Información", "Diagnóstico modificado exitosamente")
            # Actualizar la vista de la lista de diagnósticos
            self.mostrar_diagnosticos()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al modificar el diagnóstico: {e}")

# ===========

    def modificar_factura(self):
        # Obtener la selección actual del Treeview
        selected_item = self.tree_lista_facturas.selection()
        if not selected_item:
            messagebox.showerror("Error", "Selecciona una factura para modificar")
            return

        # Obtener los datos de la factura seleccionada
        item = self.tree_lista_facturas.item(selected_item)
        factura_id = item['values'][0]

        # Obtener los datos de la factura desde la base de datos
        conn = sql.connect("DataBase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Factura WHERE FacturaID=?", (factura_id,))
        factura = cursor.fetchone()
        conn.close()

        if not factura:
            messagebox.showerror("Error", "No se encontró la factura")
            return

        # Limpiar el frame derecho antes de agregar el formulario
        for widget in self.frame_right.winfo_children():
            widget.destroy()

        # Etiquetas y campos de entrada del formulario
        self.factura_id = factura[0]

        lbl_diagnostico_id = tb.Label(self.frame_right, text="ID Diagnóstico")
        lbl_diagnostico_id.grid(row=0, column=0, padx=10, pady=10)
        self.entry_diagnostico_id = tb.Entry(self.frame_right)
        self.entry_diagnostico_id.grid(row=0, column=1, padx=10, pady=10)
        self.entry_diagnostico_id.insert(0, factura[1])

        lbl_descripcion_servicio = tb.Label(self.frame_right, text="Descripción del Servicio")
        lbl_descripcion_servicio.grid(row=1, column=0, padx=10, pady=10)
        self.entry_descripcion_servicio = tb.Entry(self.frame_right)
        self.entry_descripcion_servicio.grid(row=1, column=1, padx=10, pady=10)
        self.entry_descripcion_servicio.insert(0, factura[2])

        lbl_costo_servicio = tb.Label(self.frame_right, text="Costo del Servicio")
        lbl_costo_servicio.grid(row=2, column=0, padx=10, pady=10)
        self.entry_costo_servicio = tb.Entry(self.frame_right)
        self.entry_costo_servicio.grid(row=2, column=1, padx=10, pady=10)
        self.entry_costo_servicio.insert(0, factura[3])

        # Botón Guardar
        btn_guardar = tb.Button(self.frame_right, text='Guardar Cambios', bootstyle="success", command=self.guardar_cambios_factura)
        btn_guardar.grid(row=3, column=0, columnspan=2, pady=10)

    def guardar_cambios_factura(self):
        # Obtener los datos del formulario
        diagnostico_id = self.entry_diagnostico_id.get()
        descripcion_servicio = self.entry_descripcion_servicio.get()
        costo_servicio = self.entry_costo_servicio.get()

        # Actualizar los datos en la base de datos
        try:
            conn = sql.connect("DataBase.db")
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Factura
                SET DiagnosticoID = ?, DescripcionDelServicio = ?, CostoDelServicio = ?
                WHERE FacturaID = ?
            ''', (diagnostico_id, descripcion_servicio, costo_servicio, self.factura_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Información", "Factura modificada exitosamente")
            # Actualizar la vista de la lista de facturas
            self.mostrar_facturas()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al modificar la factura: {e}")


# # ==================FUNCIONES ELIMINAR DATOS=====================





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