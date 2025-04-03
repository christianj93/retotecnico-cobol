
# 📌 Procesador de Transacciones Bancarias

## 📝 Introducción

Este proyecto es una aplicación que procesa transacciones bancarias desde un archivo CSV. Permite calcular el balance final, identificar la transacción de mayor monto y contar la cantidad de transacciones de tipo "Crédito" y "Débito". La aplicación cuenta con una interfaz gráfica intuitiva que muestra los resultados en un área de texto.

## 🚀 Instrucciones de Ejecución

### 🔧 Requisitos

- Python 3.7 o superior
- Tkinter (incluido en la instalación estándar de Python)

### 📦 Instalación de Dependencias

Asegúrate de que `tkinter` esté disponible y ejecuta el siguiente comando para instalar cualquier dependencia necesaria:

```sh
pip install tk
```

### ▶️ Ejecución de la Aplicación

Sigue estos pasos para ejecutar la aplicación:

1. Clona el repositorio:
   ```sh
   git clone https://github.com/christianj93/retotecnico-cobol.git
   ```
2. Accede al directorio del proyecto:
   ```sh
   cd retotecnico-cobol
   ```
3. Ejecuta el script principal:
   ```sh
   python main.py
   ```
4. Se abrirá una ventana donde podrás seleccionar un archivo CSV para procesar.

## 🏗️ Enfoque y Solución

El proyecto sigue una arquitectura en capas para mantener una estructura modular y escalable:

- **Capa de Procesamiento** 📊: Encargada de leer el archivo CSV, calcular el balance final, contar las transacciones y encontrar la transacción con el mayor monto.
- **Capa de Interfaz** 🎨: Implementa una GUI con `Tkinter` para permitir una interacción amigable con el usuario.

Este enfoque modular facilita la expansión y el mantenimiento del código.

## 📂 Estructura del Proyecto

```
retotecnico-cobol/
│── src/
│   │── gui/
│   │   │── interfaz.py        # Código para la interfaz gráfica con Tkinter
│   │   │── __init__.py        # Conviente la carpeta en un módulo
│   │── logic/
│   │   │── logica.py          # Lógica de negocio para procesar las transacciones
│   │   │── __init__.py        # Conviente la carpeta en un módulo
│   │── __init__.py            # Conviente la carpeta en un módulo
│── input/
│   │── transacciones.csv      # Archivo de ejemplo con transacciones
│── README.md                  # Documentación del proyecto
│── main.py                    # Archivo principal que invoca la interfaz
```

El código está bien documentado y diseñado para ser fácil de entender y modificar. ¡Esperamos que sea de utilidad! 🚀
