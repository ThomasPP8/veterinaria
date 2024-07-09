from tkinter import *
from tkinter import ttk, messagebox
import ttkbootstrap as tb #Acceder estilos de bootstrap
import sqlite3 as sql #Libreria de SQLittle

class Ventana(tb.Window): #Aqui cambia el "TK" por "tb.Window"
    def __init__(self):
        super().__init__()
        self.ventana_login()

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
        btn_clientes=ttk.Button(self.frame_left,text='Empleados',width=15, command=self.ventana_lista_clientes)
        btn_clientes.grid(row=2,column=0,padx=10,pady=10)
        btn_compras=ttk.Button(self.frame_left,text='Diagnosticos',width=15, command=self.ventana_lista_clientes)
        btn_compras.grid(row=3,column=0,padx=10,pady=10)
        btn_usuarios=ttk.Button(self.frame_left,text='Facturas',width=15,command=self.ventana_lista_clientes)
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

        btn_nuevo_cliente=tb.Button(self.lblframe_botones_listclient,text='Nuevo',width=15,bootstyle="success")
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

        btn_nueva_mascota = tb.Button(self.lblframe_botones_listpet, text='Nueva', width=15, bootstyle="success")
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




    
#     def ventana_ventas(self):
#         self.frame_ventas = Frame(self.frame_center)
#         self.frame_ventas.grid(row=0, column=0, columnspan=2, sticky=NSEW)

#         self.lblframe_botones_ventas = LabelFrame(self.frame_ventas)
#         self.lblframe_botones_ventas.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

#         btn_nueva_venta = tb.Button(self.lblframe_botones_ventas, text='Registrar Venta', width=15, bootstyle="success",command=self.show_new_sale_form)
#         btn_nueva_venta.grid(row=0, column=0, padx=5, pady=5)

#         self.lblframe_lista_ventas = LabelFrame(self.frame_ventas)
#         self.lblframe_lista_ventas.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

#         columnas = ("id_venta", "producto", "cliente", "cantidad", "fecha")
#         self.tree_lista_ventas = tb.Treeview(self.lblframe_lista_ventas, columns=columnas,
#                                             height=17, show='headings', bootstyle='dark')
#         self.tree_lista_ventas.grid(row=0, column=0)

#         self.tree_lista_ventas.heading("id_venta", text="ID Venta", anchor=W)
#         self.tree_lista_ventas.heading("producto", text="Producto", anchor=W)
#         self.tree_lista_ventas.heading("cliente", text="Cliente", anchor=W)
#         self.tree_lista_ventas.heading("cantidad", text="Cantidad", anchor=W)
#         self.tree_lista_ventas.heading("fecha", text="Fecha", anchor=W)

#         tree_scroll_ventas = tb.Scrollbar(self.frame_ventas, bootstyle='round-success')
#         tree_scroll_ventas.grid(row=1, column=1)
#         tree_scroll_ventas.config(command=self.tree_lista_ventas.yview)

#         self.mostrar_ventas()
    
#     def ventana_clientes(self):
#         self.frame_clientes = Frame(self.frame_center)
#         self.frame_clientes.grid(row=0, column=0, columnspan=2, sticky=NSEW)

#         self.lblframe_botones_clientes = LabelFrame(self.frame_clientes)
#         self.lblframe_botones_clientes.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

#         btn_nuevo_cliente = tb.Button(self.lblframe_botones_clientes, text='Nuevo', width=15, bootstyle="success")
#         btn_nuevo_cliente.grid(row=0, column=0, padx=5, pady=5)
#         btn_modificar_cliente = tb.Button(self.lblframe_botones_clientes, text='Modificar', width=15, bootstyle="warning")
#         btn_modificar_cliente.grid(row=0, column=1, padx=5, pady=5)
#         btn_eliminar_cliente = tb.Button(self.lblframe_botones_clientes, text='Eliminar', width=15, bootstyle="danger")
#         btn_eliminar_cliente.grid(row=0, column=2, padx=5, pady=5)

#         self.lblframe_lista_clientes = LabelFrame(self.frame_clientes)
#         self.lblframe_lista_clientes.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

#         columnas = ("id_cliente", "nombre", "telefono", "email")
#         self.tree_lista_clientes = tb.Treeview(self.lblframe_lista_clientes, columns=columnas,
#                                             height=17, show='headings', bootstyle='dark')
#         self.tree_lista_clientes.grid(row=0, column=0)

#         self.tree_lista_clientes.heading("id_cliente", text="ID Cliente", anchor=W)
#         self.tree_lista_clientes.heading("nombre", text="Nombre", anchor=W)
#         self.tree_lista_clientes.heading("telefono", text="Teléfono", anchor=W)
#         self.tree_lista_clientes.heading("email", text="Email", anchor=W)

#         tree_scroll_clientes = tb.Scrollbar(self.frame_clientes, bootstyle='round-success')
#         tree_scroll_clientes.grid(row=1, column=1)
#         tree_scroll_clientes.config(command=self.tree_lista_clientes.yview)

#         self.mostrar_clientes()

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


# # ===================FUNCIONES AGREGAR DATOS======================
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

#             conn = sql.connect("tshopDB.db")
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

#             conn = sql.connect("tshopDB.db")
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

#             conn = sql.connect("tshopDB.db")
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
#     def delete_product(self):
        # selected_item = self.tree_lista_productos.selection()
        # if not selected_item:
        #     messagebox.showerror("Error", "Selecciona un producto para eliminar")
        #     return

        # item = self.tree_lista_productos.item(selected_item)
        # product_id = item['values'][0]

        # # Confirmación antes de eliminar
        # confirm = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este producto?")
        # if not confirm:
        #     return

        # try:
        #     conn = sql.connect("tshopDB.db")
        #     cursor = conn.cursor()
            
        #     cursor.execute(
        #         '''
        #         DELETE FROM productos
        #         WHERE id_producto = ?
        #         ''', (product_id,)
        #     )
            
        #     conn.commit()
        #     conn.close()
            
        #     messagebox.showinfo("Información", "Producto eliminado exitosamente")
        #     self.mostrar_productos()
        # except Exception as e:
        #     messagebox.showerror("Error", f"Ocurrió un error al eliminar el producto: {e}")


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