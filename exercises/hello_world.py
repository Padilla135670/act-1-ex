# hello_world.py
# Actividad 1 (extra) - Trabajo colaborativo con Git y GitHub
# Estudiante 1: Juan Pablo Padilla

# Estas constantes guardan los datos que se van a mostrar en pantalla.
# Se escriben en MAYUSCULAS porque, por convencion en Python, indican
# valores que no deberian cambiar durante la ejecucion del programa.
NOMBRE = "Juan Pablo Padilla"
CURSO = "Algoritmos y Analisis de Datos"


def main():
    """Muestra un saludo personalizado en la consola."""
    print("Hello, World!")

    # Los f-string permiten insertar el valor de una variable dentro
    # del texto: lo que va entre llaves {} se reemplaza por su valor.
    print(f"Hola, mi nombre es {NOMBRE}.")
    print(f"Bienvenido al curso de {CURSO}.")

    # Mensaje personalizado adicional
    print("Este programa es mi aporte al trabajo en equipo de la actividad.")
    print("Con el aprendi a usar ramas, commits y Pull Requests en GitHub.")


# Este bloque hace que main() se ejecute unicamente cuando el archivo se
# corre de forma directa, y no cuando se importa desde otro modulo.
if __name__ == "__main__":
    main()
