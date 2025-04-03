
# 📌 Procesador de Transacciones Bancarias

## 📝 Introducción

Este proyecto es una aplicación que procesa transacciones bancarias desde un archivo CSV. Permite calcular el balance final, identificar la transacción de mayor monto y contar la cantidad de transacciones de tipo "Crédito" y "Débito". Cuenta con una interfaz gráfica intuitiva para facilitar su uso.

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
3. Accede a la carpeta `cli` y ejecuta el script principal:
   ```sh
   cd cli
   python main.py
   ```
4. Se abrirá una interfaz gráfica donde podrás seleccionar un archivo CSV para procesar.

## 🏗️ Enfoque y Solución

El proyecto sigue una arquitectura en capas para mantener una estructura modular y escalable:

- **Capa de Procesamiento** 📊: Encargada de leer el archivo CSV, calcular el balance final, contar las transacciones y encontrar la transacción con el mayor monto.
- **Capa de Interfaz** 🎨: Implementa una GUI con `Tkinter` para permitir una interacción amigable con el usuario.

Este enfoque modular facilita la expansión y el mantenimiento del código.

## 📂 Estructura del Proyecto

```
retotecnico-cobol/
│── cli/
│   │── main.py                   # Código principal con GUI y lógica de negocio
│── input/
│   │── transacciones.csv          # Archivo de ejemplo con transacciones
│── README.md                     # Documentación del proyecto
```

🚀
