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

        btn_productos=ttk.Button(self.frame_left,text='Productos',width=15, command=self.ventana_productos)
        btn_productos.grid(row=0,column=0,padx=10,pady=10)
        btn_ventas=ttk.Button(self.frame_left,text='Ventas',width=15,command=self.ventana_ventas)
        btn_ventas.grid(row=1,column=0,padx=10,pady=10)
        btn_clientes=ttk.Button(self.frame_left,text='Clientes',width=15, command=self.ventana_clientes)
        btn_clientes.grid(row=2,column=0,padx=10,pady=10)
        btn_compras=ttk.Button(self.frame_left,text='Compras',width=15)
        btn_compras.grid(row=3,column=0,padx=10,pady=10)
        btn_usuarios=ttk.Button(self.frame_left,text='Usuarios',width=15,command=self.ventana_lista_usuarios)
        btn_usuarios.grid(row=4,column=0,padx=10,pady=10)
        btn_reportes=ttk.Button(self.frame_left,text='Reportes',width=15)
        btn_reportes.grid(row=5,column=0,padx=10,pady=10)
        btn_backup=ttk.Button(self.frame_left,text='Backup',width=15)
        btn_backup.grid(row=6,column=0,padx=10,pady=10)
        btn_restaurabd=ttk.Button(self.frame_left,text='Restaurar BD',width=15)
        btn_restaurabd.grid(row=7,column=0,padx=10,pady=10)


        lbl2=Label(self.frame_center,text='Aqui Pondremos las ventanas que creemos')
        lbl2.grid(row=0,column=0,padx=10,pady=10)

        lbl3=Label(self.frame_right,text='Aqui Pondremos las busquedas para la ventana')
        lbl3.grid(row=0,column=0,padx=10,pady=10)

    def logueo(self):
        self.frame_login.pack_forget()#Ocultar la ventana de Login
        self.ventana_menu()#abrir ventana de menu


#VENTANAS ********************************
    def ventana_lista_usuarios(self):
        self.frame_lista_usuarios=Frame(self.frame_center)
        self.frame_lista_usuarios.grid(row=0,column=0,columnspan=2,sticky=NSEW)

        self.lblframe_botones_listusu=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_botones_listusu.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

        btn_nuevo_usuario=tb.Button(self.lblframe_botones_listusu,text='Nuevo',width=15,bootstyle="success")
        btn_nuevo_usuario.grid(row=0,column=0,padx=5,pady=5)
        btn_modificar_usuario=tb.Button(self.lblframe_botones_listusu,text='Modificar',width=15,bootstyle="warning")
        btn_modificar_usuario.grid(row=0,column=1,padx=5,pady=5)
        btn_eliminar_usuario=tb.Button(self.lblframe_botones_listusu,text='Eliminar',width=15,bootstyle="danger")
        btn_eliminar_usuario.grid(row=0,column=2,padx=5,pady=5)

        self.lblframe_busqueda_listusu=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_busqueda_listusu.grid(row=1,column=0,padx=10,pady=10,sticky=NSEW)

        txt_busqueda_usuarios=ttk.Entry(self.lblframe_busqueda_listusu,width=90)
        txt_busqueda_usuarios.grid(row=0,column=0,padx=5,pady=5)

        #====================Treeview=====================================

        self.lblframe_tree_listusu=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_tree_listusu.grid(row=2,column=0,padx=10,pady=10,sticky=NSEW)
        
        columnas=("codigo","nombre","clave","rol")

        self.tree_lista_usuarios=tb.Treeview(self.lblframe_tree_listusu,columns=columnas,
                                        height=17,show='headings',bootstyle='dark')
        self.tree_lista_usuarios.grid(row=0,column=0)

        self.tree_lista_usuarios.heading("codigo",text="Codigo",anchor=W)
        self.tree_lista_usuarios.heading("nombre",text="Nombre",anchor=W)
        self.tree_lista_usuarios.heading("clave",text="Clave",anchor=W)
        self.tree_lista_usuarios.heading("rol",text="Rol",anchor=W)
        self.tree_lista_usuarios['displaycolumns']=("codigo","nombre","rol") #Ocultar columna clave

        #Crear Scrolbar
        tree_scroll_listausu=tb.Scrollbar(self.frame_lista_usuarios,bootstyle='round-success')
        tree_scroll_listausu.grid(row=2,column=1)
        #configurar scrolbar
        tree_scroll_listausu.config(command=self.tree_lista_usuarios.yview)

        #Llamamos a nuestra funcion mostrar usuarios
        self.mostrar_usuarios()
    
    def ventana_productos(self):
        self.frame_productos = Frame(self.frame_center)
        self.frame_productos.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        self.lblframe_botones_productos = LabelFrame(self.frame_productos)
        self.lblframe_botones_productos.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

        btn_nuevo_producto = tb.Button(self.lblframe_botones_productos, text='Nuevo', width=15, bootstyle="success", command=self.show_new_product_form)
        btn_nuevo_producto.grid(row=0, column=0, padx=5, pady=5)
        btn_modificar_producto = tb.Button(self.lblframe_botones_productos, text='Modificar', width=15, bootstyle="warning")
        btn_modificar_producto.grid(row=0, column=1, padx=5, pady=5)
        btn_eliminar_producto = tb.Button(self.lblframe_botones_productos, text='Eliminar', width=15, bootstyle="danger")
        btn_eliminar_producto.grid(row=0, column=2, padx=5, pady=5)

        self.lblframe_lista_productos = LabelFrame(self.frame_productos)
        self.lblframe_lista_productos.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

        columnas = ("id_producto", "nombre", "descripcion", "precio", "stock")
        self.tree_lista_productos = tb.Treeview(self.lblframe_lista_productos, columns=columnas,
                                                height=17, show='headings', bootstyle='dark')
        self.tree_lista_productos.grid(row=0, column=0)

        self.tree_lista_productos.heading("id_producto", text="ID Producto", anchor=W)
        self.tree_lista_productos.heading("nombre", text="Nombre", anchor=W)
        self.tree_lista_productos.heading("descripcion", text="Descripción", anchor=W)
        self.tree_lista_productos.heading("precio", text="Precio", anchor=W)
        self.tree_lista_productos.heading("stock", text="Stock", anchor=W)

        tree_scroll_productos = tb.Scrollbar(self.frame_productos, bootstyle='round-success')
        tree_scroll_productos.grid(row=1, column=1)
        tree_scroll_productos.config(command=self.tree_lista_productos.yview)

        self.mostrar_productos()
    
    def ventana_ventas(self):
        self.frame_ventas = Frame(self.frame_center)
        self.frame_ventas.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        self.lblframe_botones_ventas = LabelFrame(self.frame_ventas)
        self.lblframe_botones_ventas.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

        btn_nueva_venta = tb.Button(self.lblframe_botones_ventas, text='Registrar Venta', width=15, bootstyle="success")
        btn_nueva_venta.grid(row=0, column=0, padx=5, pady=5)

        self.lblframe_lista_ventas = LabelFrame(self.frame_ventas)
        self.lblframe_lista_ventas.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

        columnas = ("id_venta", "producto", "cliente", "cantidad", "fecha")
        self.tree_lista_ventas = tb.Treeview(self.lblframe_lista_ventas, columns=columnas,
                                            height=17, show='headings', bootstyle='dark')
        self.tree_lista_ventas.grid(row=0, column=0)

        self.tree_lista_ventas.heading("id_venta", text="ID Venta", anchor=W)
        self.tree_lista_ventas.heading("producto", text="Producto", anchor=W)
        self.tree_lista_ventas.heading("cliente", text="Cliente", anchor=W)
        self.tree_lista_ventas.heading("cantidad", text="Cantidad", anchor=W)
        self.tree_lista_ventas.heading("fecha", text="Fecha", anchor=W)

        tree_scroll_ventas = tb.Scrollbar(self.frame_ventas, bootstyle='round-success')
        tree_scroll_ventas.grid(row=1, column=1)
        tree_scroll_ventas.config(command=self.tree_lista_ventas.yview)

        self.mostrar_ventas()
    
    def ventana_clientes(self):
        self.frame_clientes = Frame(self.frame_center)
        self.frame_clientes.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        self.lblframe_botones_clientes = LabelFrame(self.frame_clientes)
        self.lblframe_botones_clientes.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

        btn_nuevo_cliente = tb.Button(self.lblframe_botones_clientes, text='Nuevo', width=15, bootstyle="success")
        btn_nuevo_cliente.grid(row=0, column=0, padx=5, pady=5)
        btn_modificar_cliente = tb.Button(self.lblframe_botones_clientes, text='Modificar', width=15, bootstyle="warning")
        btn_modificar_cliente.grid(row=0, column=1, padx=5, pady=5)
        btn_eliminar_cliente = tb.Button(self.lblframe_botones_clientes, text='Eliminar', width=15, bootstyle="danger")
        btn_eliminar_cliente.grid(row=0, column=2, padx=5, pady=5)

        self.lblframe_lista_clientes = LabelFrame(self.frame_clientes)
        self.lblframe_lista_clientes.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

        columnas = ("id_cliente", "nombre", "telefono", "email")
        self.tree_lista_clientes = tb.Treeview(self.lblframe_lista_clientes, columns=columnas,
                                            height=17, show='headings', bootstyle='dark')
        self.tree_lista_clientes.grid(row=0, column=0)

        self.tree_lista_clientes.heading("id_cliente", text="ID Cliente", anchor=W)
        self.tree_lista_clientes.heading("nombre", text="Nombre", anchor=W)
        self.tree_lista_clientes.heading("telefono", text="Teléfono", anchor=W)
        self.tree_lista_clientes.heading("email", text="Email", anchor=W)

        tree_scroll_clientes = tb.Scrollbar(self.frame_clientes, bootstyle='round-success')
        tree_scroll_clientes.grid(row=1, column=1)
        tree_scroll_clientes.config(command=self.tree_lista_clientes.yview)

        self.mostrar_clientes()

#FUNCIONES MOSTRAR DATOS ==================
    def mostrar_usuarios(self):
        #Capturador errores
        try:
            #Establecer la conexion
            miConexion=sql.connect('Ventas.db')
            #Crear Cursor
            miCursor=miConexion.cursor()
            #Limpiamos nuetro treeview
            registros=self.tree_lista_usuarios.get_children()
            #Recorremos cada registro
            for elementos in registros:
                self.tree_lista_usuarios.delete(elementos)
            #Consultar nuetra base de datos
            miCursor.execute("SELECT * FROM Usuarios")
            #con esto traemos todos los registros y lo guardamos en "datos"
            datos=miCursor.fetchall()
            #Recorremos cada fila encontrada
            for row in datos:
                self.tree_lista_usuarios.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3]))
            #Aplicamos Cambios
            miConexion.commit()
            #Cerramos la conexion
            miConexion.close()

        except:
            #Mensaje error
            messagebox.showerror("Lista de Usuario","Ocurrio un error al mostrar las listas de usuario")

    def mostrar_productos(self):
        try:
            miConexion = sql.connect('tshopDB.db')
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM productos")
            datos = miCursor.fetchall()
            for row in datos:
                self.tree_lista_productos.insert("", 0, text=row[0], values=(row[0], row[1], row[2], row[3], row[4]))
            miConexion.commit()
        except Exception as e:
            messagebox.showerror("Lista de Productos", f"Ocurrió un error al mostrar las listas de productos: {e}")
        finally:
            if miConexion:
                miConexion.close()
    
    def mostrar_ventas(self):
        try:
            miConexion = sql.connect('tshopDB.db')
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM Ventas")
            datos = miCursor.fetchall()
            for row in datos:
                self.tree_lista_ventas.insert("", 0, text=row[0], values=(row[0], row[1], row[2], row[3], row[4]))
            miConexion.commit()
            miConexion.close()
        except:
            messagebox.showerror("Lista de Ventas", "Ocurrió un error al mostrar las listas de ventas")

    def mostrar_clientes(self):
        try:
            miConexion = sql.connect('tshopDB.db')
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM Clientes")
            datos = miCursor.fetchall()
            for row in datos:
                self.tree_lista_clientes.insert("", 0, text=row[0], values=(row[0], row[1], row[2], row[3]))
            miConexion.commit()
            miConexion.close()
        except:
            messagebox.showerror("Lista de Clientes", "Ocurrió un error al mostrar las listas de cliente")


# ===================FUNCIONES AGREGAR DATOS======================
    def show_new_product_form(self):
        # Limpiar el frame derecho
        for widget in self.frame_right.winfo_children():
            widget.destroy()

        # Campos del formulario
        Label(self.frame_right, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        name_entry = Entry(self.frame_right)
        name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        Label(self.frame_right, text="Descripción").grid(row=1, column=0, padx=10, pady=10)
        description_entry = Entry(self.frame_right)
        description_entry.grid(row=1, column=1, padx=10, pady=10)
        
        Label(self.frame_right, text="Precio").grid(row=2, column=0, padx=10, pady=10)
        price_entry = Entry(self.frame_right)
        price_entry.grid(row=2, column=1, padx=10, pady=10)
        
        Label(self.frame_right, text="Stock").grid(row=3, column=0, padx=10, pady=10)
        stock_entry = Entry(self.frame_right)
        stock_entry.grid(row=3, column=1, padx=10, pady=10)
        
        # Botón para guardar el nuevo producto
        def save_product():
            name = name_entry.get()
            description = description_entry.get()
            price = price_entry.get()
            stock = stock_entry.get()
            
            # Validaciones
            if not name:
                messagebox.showerror("Error", "El nombre es obligatorio")
                return
            if not description:
                messagebox.showerror("Error", "La descripción es obligatoria")
                return
            try:
                price = float(price)
            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número válido")
                return
            try:
                stock = int(stock)
            except ValueError:
                messagebox.showerror("Error", "El stock debe ser un número entero")
                return

            conn = sql.connect("tshopDB.db")
            cursor = conn.cursor()
            
            cursor.execute(
                '''
                INSERT INTO productos (nombre, descripcion, precio, stock)
                VALUES (?, ?, ?, ?)
                ''', (name, description, price, stock)
            )
            
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Información", "Producto agregado exitosamente")
            self.show_new_product_form()  # Limpiar formulario después de agregar
        
        Button(self.frame_right, text="Guardar", command=save_product).grid(row=4, column=0, columnspan=2, pady=20)



def main():
    app=Ventana()
    app.title('Sistema de ventas') #Titulo de la ventana
    app.state('zoomed') #zoomed inicia la ventana maximizada
    tb.Style('solar') #Themes: solar, superhero, darkly, cyborg, vapor - https://ttkbootstrap.readthedocs.io/en/latest/themes/dark/
    app.mainloop()

if __name__=='__main__':
        #createDB()
        #createTable()
        #insert_values()
        main()