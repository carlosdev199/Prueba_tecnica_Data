'''Descifra un mensaje cifrado, Se utiliza el algoritmo César.'''

import tkinter as tk

def descifrar_mensaje(mensaje_cifrado):

    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    mensaje_descifrado = ""
    desplazamiento = 2

  
    for char in mensaje_cifrado:

        # Comprueba si el carácter es una letra.
        if char.isalpha():

            # Obtiene la posición del carácter en el alfabeto.
            index_letra = alfabeto.index(char.lower())

            # Calcula la dirección de desplazamiento.
            direccion = -1 if desplazamiento % 2 == 0 else 1

            # Obtiene la letra descifrada.
            letra_descifrada = alfabeto[(index_letra + direccion * desplazamiento) % 26]

            # Si el carácter era mayúscula, la letra descifrada también lo es.
            if char.isupper():
                letra_descifrada = letra_descifrada.upper()

            # Agrega la letra descifrada al mensaje descifrado.
            mensaje_descifrado += letra_descifrada
            desplazamiento += 1

        else:
            # Si el carácter no es una letra, lo agrega al mensaje descifrado sin cambios.
            mensaje_descifrado += char

    return mensaje_descifrado

def actualizar_resultado():

    # Obtiene el mensaje cifrado del widget de entrada de texto.
    mensaje_cifrado = entrada_texto.get()

    # Descifra el mensaje cifrado.
    resultado_descifrado = descifrar_mensaje(mensaje_cifrado)

    # Actualiza el texto de la etiqueta de resultado.
    etiqueta_resultado.config(text=resultado_descifrado)


def limpiar():

    # Elimina el texto del widget de entrada de texto.
    entrada_texto.delete(0, tk.END)
    etiqueta_resultado.config(text="")


def salir():
    # Cierra la ventana.
    ventana.destroy()


# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Desencriptar Código Enigma")

# Configuración del widget de entrada de texto
entrada_texto = tk.Entry(ventana, width=40, font=("Arial", 12), justify="center")
entrada_texto.pack(pady=10)

# Configuración del botón de descifrado
boton_descifrar = tk.Button(ventana, text="Descifrar", command=actualizar_resultado, font=("Arial", 12))
boton_descifrar.pack(pady=5)

# Configuración del botón de limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar, font=("Arial", 12))
boton_limpiar.pack(pady=5)

# Configuración del botón de salir
boton_salir = tk.Button(ventana, text="Salir", command=salir, font=("Arial", 12))
boton_salir.pack(pady=5)

# Configuración de la etiqueta de resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 16), wraplength=400, justify="center")
etiqueta_resultado.pack(pady=10)

# Ejecución de la interfaz gráfica
ventana.mainloop()
