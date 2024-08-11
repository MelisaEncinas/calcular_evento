import tkinter as tk
from datetime import datetime
import pytz

def calcular_tiempo_faltante(fecha_evento_str):
    try:
        try:
            fecha_evento = datetime.strptime(fecha_evento_str, "%d/%m/%Y")
        except ValueError:
            try:
                fecha_evento = datetime.strptime(fecha_evento_str, "%m/%d/%Y")
            except ValueError:
                return "Formato de fecha no válido. Por favor ingrese una fecha válida en formato dd/mm/yyyy"

        if fecha_evento.tzinfo is None:
            fecha_evento = pytz.utc.localize(fecha_evento)

        ahora = datetime.now(pytz.utc)

        diferencia = fecha_evento - ahora

        if diferencia.total_seconds() < 0:
            return "El evento ya ha pasado."

        dias = diferencia.days
        segundos_restantes = diferencia.seconds
        horas = segundos_restantes // 3600
        minutos = (segundos_restantes % 3600) // 60
        segundos = segundos_restantes % 60

        return f"Faltan {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos para el GRAN DIA."

    except Exception as e:
        return f"Error: {str(e)}"

# Función que se ejecuta al  clic en el botón
def mostrar_resultado():
    fecha_evento_str = entrada_fecha.get()
    resultado = calcular_tiempo_faltante(fecha_evento_str)
    mensaje.config(text=resultado)

root = tk.Tk()
root.title("¿Cuanto falta para el evento? ")

etiqueta = tk.Label(root, text="Ingrese la fecha del evento (dd/mm/aaaa ):")
etiqueta.pack(pady=10)

entrada_fecha = tk.Entry(root)
entrada_fecha.pack(pady=10)

boton_calcular = tk.Button(root, text="Calcular", command=mostrar_resultado)
boton_calcular.pack(pady=10)

mensaje = tk.Label(root, text="")
mensaje.pack(pady=10)

root.mainloop()

