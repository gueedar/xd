from PIL import ImageTk, Image

def leer_imagen (path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.Resampling.LANCZOS))

def centrar_ventana (ventana, aplicacion_ancho, apliccaion_largo):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()
    x = int((pantalla_ancho / 2) - aplicacion_ancho / 2)
    y = int((pantalla_largo / 2) - (pantalla_largo / 2))
    return ventana.geometry(f"{aplicacion_ancho}x{apliccaion_largo}+{x}+{y}")