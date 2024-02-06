import tkinter as tk
from tkinter import END, messagebox
import pickle

def operacion(op):
    try:
        num1 = float(txtNumero1.get())
        num2 = float(txtNumero2.get())
        
        if op == "+":
            resultado = num1 + num2
        elif op == "-":
            resultado = num1 - num2
        elif op == "*":
            resultado = num1 * num2
        elif op == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                messagebox.showinfo(message="División por cero no permitida", title="Error")
                return
        else:
            messagebox.showinfo(message="Operación no válida", title="Error")
            return
        
        txtResultado.delete(0, END)
        txtResultado.insert(0, str(resultado))
        
    except ValueError:
        messagebox.showinfo(message="Entrada no válida", title="Error")

def limpiar():
    txtNumero1.delete(0, END)
    txtNumero2.delete(0, END)
    txtResultado.delete(0, END)

def guardar_estado():
    estado = {
        'txtNumero1': txtNumero1.get(),
        'txtNumero2': txtNumero2.get(),
        'txtResultado': txtResultado.get()
    }
    with open('estado_calculadora.pkl', 'wb') as archivo:
        pickle.dump(estado, archivo)
    messagebox.showinfo(message="Estado guardado correctamente", title="Guardado")

def cargar_estado():
    try:
        with open('estado_calculadora.pkl', 'rb') as archivo:
            estado = pickle.load(archivo)
        txtNumero1.delete(0, END)
        txtNumero1.insert(0, estado['txtNumero1'])
        txtNumero2.delete(0, END)
        txtNumero2.insert(0, estado['txtNumero2'])
        txtResultado.delete(0, END)
        txtResultado.insert(0, estado['txtResultado'])
        messagebox.showinfo(message="Estado cargado correctamente", title="Cargado")
    except FileNotFoundError:
        messagebox.showinfo(message="No se encontró el archivo de estado", title="Error")
    except Exception as e:
        messagebox.showinfo(message=f"Error al cargar el estado: {str(e)}", title="Error")

root = tk.Tk()
root.title("Calculadora")
root.config(width=250, height=300)

tk.Label(root, text="Numero 1:").place(x=10, y=30)
txtNumero1 = tk.Entry(root)
txtNumero1.place(x=80, y=30)

tk.Label(root, text="Numero 2:").place(x=10, y=50)
txtNumero2 = tk.Entry(root)
txtNumero2.place(x=80, y=50)

tk.Label(root, text="Resultado:").place(x=10, y=70)
txtResultado = tk.Entry(root)
txtResultado.place(x=80, y=70)

btnSuma = tk.Button(root, text=" + ", command=lambda: operacion("+"))
btnSuma.place(x=10, y=100)

btnResta = tk.Button(root, text=" - ", command=lambda: operacion("-"))
btnResta.place(x=50, y=100)

btnMultiplicacion = tk.Button(root, text=" * ", command=lambda: operacion("*"))
btnMultiplicacion.place(x=90, y=100)

btnDivision = tk.Button(root, text=" / ", command=lambda: operacion("/"))
btnDivision.place(x=130, y=100)

btnLimpiar = tk.Button(root, text="Limpiar", command=limpiar)
btnLimpiar.place(x=170, y=100)

btnGuardar = tk.Button(root, text="Guardar Estado", command=guardar_estado)
btnGuardar.place(x=10, y=150)

btnCargar = tk.Button(root, text="Cargar Estado", command=cargar_estado)
btnCargar.place(x=120, y=150)

root.mainloop()