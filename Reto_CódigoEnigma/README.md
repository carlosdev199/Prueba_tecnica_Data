# RETO: Desencriptar Código Enigma - prueba Tecnica

Este programa en Python utiliza la biblioteca `tkinter` para crear una aplicación que descifra mensajes encriptados siguiendo un patrón específico de desplazamiento en el alfabeto.

## Creador
Creado por: [CARLOS IBAÑEZ]

## Funciones Principales

### `descifrar_mensaje(mensaje_cifrado)`
Esta función toma un mensaje cifrado como entrada y lo descifra según el patrón de desplazamiento en el alfabeto. Devuelve el mensaje descifrado.

### `actualizar_resultado()`
Esta función se ejecuta cuando se hace clic en el botón "Descifrar". Obtiene el mensaje cifrado del campo de entrada de texto, utiliza la función `descifrar_mensaje` para obtener el mensaje descifrado y actualiza el texto de la etiqueta de resultado con el resultado descifrado.

### `limpiar()`
Esta función se ejecuta cuando se hace clic en el botón "Limpiar". Elimina el texto del campo de entrada de texto y establece el texto de la etiqueta de resultado en blanco.

### `salir()`
Esta función se ejecuta cuando se hace clic en el botón "Salir". Cierra la aplicación.

## Interfaz Gráfica

- **Campo de Entrada de Texto:** Permite al usuario ingresar el mensaje cifrado que desea descifrar.

- **Botón "Descifrar":** Al hacer clic en este botón, se ejecuta la función `actualizar_resultado`, descifrando el mensaje y actualizando la etiqueta de resultado.

- **Botón "Limpiar":** Al hacer clic en este botón, se ejecuta la función `limpiar`, eliminando el texto del campo de entrada y restableciendo la etiqueta de resultado.

- **Botón "Salir":** Cierra la aplicación cuando se hace clic en este botón.

- **Etiqueta de Resultado:** Muestra el mensaje descifrado resultante. Inicialmente, está en blanco.

## Ejecución

1. Asegúrate de tener Python instalado en tu sistema.
2. Ejecuta el script proporcionado.
3. Se abrirá una ventana con la interfaz gráfica.
4. Ingresa el mensaje cifrado en el campo de entrada de texto.
5. Haz clic en el botón "Descifrar" para obtener el resultado.
6. Puedes usar los botones "Limpiar" y "Salir" según sea necesario.

Este programa es una implementación básica para demostrar el cifrado y descifrado de mensajes a través de una interfaz gráfica simple.
