import json
import os

# Nombre del archivo donde se guardarán las tareas
FILE_NAME = "tareas.json"

def load_tasks():
    """Carga las tareas desde el archivo JSON."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

#Guardar en JSON
def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

#Mostrar
def show_tasks(tasks):
    if not tasks:
        print("\nNo hay tareas pendientes.")
    else:
        print("\nLista de tareas:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

#Añadir
def add_task(tasks):
    task = input("Ingrese la nueva tarea: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Tarea añadida correctamente.")

#Eliminar
def remove_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Tarea eliminada: {removed_task}")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

#Menú
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        choice = input("Seleccione una opción: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
