import json
import os

FILE_NAME = "tasks.json"

# Campos obligatorios que debe tener cada tarea
REQUIRED_FIELDS = {"id", "title", "completed"}


def load_tasks():
    """
    Carga las tareas desde el archivo JSON.
    Valida estructura, campos obligatorios y tipos de datos.
    Retorna una lista de tareas válida.
    """

    # Si el archivo no existe
    if not os.path.exists(FILE_NAME):
        print("Archivo no encontrado. Se iniciará con una lista vacía.")
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Validar que el contenido sea una lista
        if not isinstance(data, list):
            print("Error: El archivo JSON no contiene una lista de tareas.")
            return []

        valid_tasks = []

        for index, task in enumerate(data):

            # Validar que cada tarea sea un diccionario
            if not isinstance(task, dict):
                print(
                    f"Tarea en posición {index} ignorada: "
                    "estructura inválida."
                )
                continue

            # Validar campos obligatorios
            if not REQUIRED_FIELDS.issubset(task.keys()):
                print(
                    f"Tarea en posición {index} ignorada: "
                    f"faltan campos obligatorios {REQUIRED_FIELDS}."
                )
                continue

            # Validar ID
            if not isinstance(task["id"], int) or isinstance(task["id"], bool):
                print(
                    f"Tarea en posición {index} ignorada: "
                    "el ID debe ser un número entero."
                )
                continue

            if task["id"] < 0:
                print(
                    f"Tarea en posición {index} ignorada: "
                    "el ID no puede ser negativo."
                )
                continue

            # Validar título
            if not isinstance(task["title"], str) or not task["title"].strip():
                print(
                    f"Tarea en posición {index} ignorada: "
                    "el título debe ser texto y no estar vacío."
                )
                continue

            # Validar completed
            if not isinstance(task["completed"], bool):
                print(
                    f"Tarea en posición {index} ignorada: "
                    "el campo 'completed' debe ser verdadero o falso."
                )
                continue

            valid_tasks.append(task)

        return valid_tasks

    except json.JSONDecodeError as error:
        print("Error: El archivo JSON está mal formado o corrupto.")
        print("Detalle técnico:", error)
        return []

    except OSError as error:
        print("Error: No se pudo acceder al archivo de tareas.")
        print("Detalle técnico:", error)
        return []

    except Exception as error:
        print("Error inesperado al cargar las tareas.")
        print("Detalle técnico:", error)
        return []


def save_tasks(tasks):
    """
    Guarda las tareas en el archivo JSON.
    """

    try:
        # Validar que se esté guardando una lista
        if not isinstance(tasks, list):
            print("Error: Las tareas deben almacenarse en una lista.")
            return False

        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(
                tasks,
                file,
                indent=4,
                ensure_ascii=False
            )

        return True

    except OSError as error:
        print("Error: No se pudo guardar el archivo de tareas.")
        print("Detalle técnico:", error)
        return False

    except (TypeError, ValueError) as error:
        print("Error: Los datos de las tareas no son válidos.")
        print("Detalle técnico:", error)
        return False

    except Exception as error:
        print("Error inesperado al guardar las tareas.")
        print("Detalle técnico:", error)
        return False