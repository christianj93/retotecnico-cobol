Introducción

Este proyecto es una aplicación para procesar transacciones bancarias desde un archivo CSV. La herramienta calcula el balance final, identifica la transacción de mayor monto y cuenta el número de transacciones de tipo "Crédito" y "Débito". Además, cuenta con una interfaz gráfica para facilitar su uso.

Instrucciones de Ejecución

Requisitos

Python 3.7 o superior

Tkinter (incluido en Python estándar)

Instalación de Dependencias

Para mejorar la presentación, se recomienda instalar la librería tkinter (si no está incluida en la instalación de Python) y asegurarse de tener acceso a las funcionalidades necesarias ejecutando:

pip install tk

Ejecución de la Aplicación

Para ejecutar la aplicación, sigue estos pasos:

Clona el repositorio:

git clone https://github.com/tu-usuario/retotecnico-cobol.git

Navega al directorio del proyecto:

cd retotecnico-cobol

Ejecuta el script principal:

python cli/main.py

Se abrirá una interfaz gráfica donde puedes seleccionar un archivo CSV para procesar.

Enfoque y Solución

El proyecto está desarrollado en Python y sigue una arquitectura en capas:

Capa de Procesamiento: Se encarga de leer el archivo CSV, calcular el balance, contar las transacciones y determinar la transacción de mayor monto.

Capa de Interfaz: Implementa una GUI con Tkinter para una interacción más intuitiva con el usuario.

El diseño modular permite ampliar y mejorar la funcionalidad fácilmente.

Estructura del Proyecto

retotecnico-cobol/
│── cli/
│   │── main.py                   # Código principal con GUI y lógica de negocio
│── README.md                     # Documentación del proyecto
│── input/
│   │── transacciones.csv              # Archivo de ejemplo con transacciones

El código está bien documentado y estructurado para facilitar su mantenimiento y extensión. ¡Esperamos que te sea útil!

