import PyPDF2 #Lib de manejo PDF
from pathlib import Path #pos los path
import tkinter as tk #UI
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog

def seleccionar_archivos(): #Func para elegir los archivos a combinar
    archivos = filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")]) #Esto es para que por defecto solo se muestren pdf, si fueran words por ejemplo seria con terminacion .docx, se esta usando con filedialog para abrir el exp de windows y se guarda en una tupla (XXXX)
    if archivos: #Si archivos no es null
        ruta_guardado = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")]) #Se solicita la ruta de guardado y se esta especificando que debe ser .pdf
        if ruta_guardado:  # Si se selecciona una ruta válida
            merger = PyPDF2.PdfMerger() #Se llama a la biblioteca de PyPDF2
            try:
                for archivo in archivos: ##Para los archivos en archivos
                    merger.append(archivo) #Combina el archivo, es basicamente una iteracion de la tupla archivos a merger
                merger.write(ruta_guardado) #Escribe los archivos en merger en la ruta de guardado
                merger.close() #Se acaba el proceso de merger
                estado_label.config(text="PDFs combinados con éxito.")
            except Exception as e:
                estado_label.config(text=f"Error: {str(e)}") #Error generico LOLOLOL
        else:
            estado_label.config(text="Operación cancelada. No se guardó el archivo.") #Si das cancelar a la pestaña
    else:
        estado_label.config(text="No se seleccionaron archivos.") #Si se tiene los archivos en blanco/Null
#UI, usando Tkinter Designer
OUTPUT_PATH = Path(__file__).parent #Ruta de los assents
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Usuario\Documents\pitinis\PresentacionPythonGrupo1\CombinarPDF\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk() #Se incia la ventana
window.title("Unir PDF") #nombre ventana

window.geometry("300x200") #Tamaño ventana
window.configure(bg = "#F4F4F4") #Color ventana


canvas = Canvas(
    window,
    bg = "#F4F4F4",
    height = 200,
    width = 300,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    300.0,
    33.0,
    fill="#00237C",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    156.0,
    154.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    163.0,
    154.0,
    image=image_image_2
)

canvas.create_text(
    16.0,
    5.0,
    anchor="nw",
    text="Combinar PDF’S",
    fill="#FFFFFF",
    font=("SourceSerifPro SemiBold", 16 * -1)
)

estado_label = tk.Label(window, text="") #Esti es para el estado, las que estan arribas como estado_label
estado_label.pack(pady=50) #10px pad

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=seleccionar_archivos,
    relief="flat"
)
button_1.place(
    x=88.0,
    y=89.0,
    width=124.0,
    height=22.0
)
window.resizable(False, False)
window.mainloop()
