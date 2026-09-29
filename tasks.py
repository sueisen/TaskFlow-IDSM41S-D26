# ==============================
# CONSTANTES DE CLAVES (MEJORA DE LEGIBILIDAD)
# ==============================

KEY_ID = "id"
KEY_TITLE = "title"
KEY_COMPLETED = "completed"


def add_task(tasks, title):
    try:
        # Validar que el título no esté vacío
        if not title or not title.strip():
            print("❌ Error: El nombre de la tarea no puede estar vacío.")
            return

        title = title.strip()

        # Validar tareas duplicadas
        title_lower = title.lower()

        if any(task[KEY_TITLE].lower() == title_lower for task in tasks):
            print("❌ Error: Ya existe una tarea con ese título.")
            return

        new_task = {
            KEY_ID: len(tasks) + 1,
            KEY_TITLE: title,
            KEY_COMPLETED: False
        }

        tasks.append(new_task)

        print("✅ Tarea agregada correctamente.")

    except Exception as e:
        print("❌ Error inesperado al agregar la tarea:", e)


def list_tasks(tasks):
    """
    Muestra en consola todas las tareas registradas.

    Si la lista está vacía, informa al usuario que no hay tareas.
    En caso contrario, imprime cada tarea mostrando su ID, título
    y estado de completado.

    Args:
        tasks (list): Lista de tareas existentes.

    Returns:
        None
    """
    try:
        if not tasks:
            print("No hay tareas")
            return

        for task in tasks:
            task_id = task[KEY_ID]
            title = task[KEY_TITLE]
            completed = task[KEY_COMPLETED]

            status = "✔" if completed else "✘"
            print(f"{task_id}. {title} [{status}]")

    except Exception as e:
        print("❌ Error al mostrar las tareas:", e)


#  FUNCIÓN DE VALIDACIÓN DE ID
def validar_task_id(task_id):

    try:
        task_id = int(task_id)

    except (ValueError, TypeError):
        print("❌ Error: El ID debe ser un número.")
        return None

    if task_id <= 0:
        print("❌ Error: El ID debe ser mayor que cero.")
        return None

    return task_id


def complete_task(tasks, task_id):
    """
    Marca una tarea como completada.

    Valida el ID utilizando la función `validar_task_id`. Si el ID
    es inválido, la función termina sin interrumpir el flujo del
    programa. Si se encuentra la tarea correspondiente, cambia su
    estado a completado. Si no existe una tarea con ese ID, muestra
    un mensaje de error.

    Args:
        tasks (list): Lista de tareas existentes.
        task_id (int | str): Identificador de la tarea a completar.

    Returns:
        None
    """
    try:
        task_id = validar_task_id(task_id)
        if task_id is None:
            return  # 🔁 No se rompe el menú

        for task in tasks:
            if task[KEY_ID] == task_id:
                task[KEY_COMPLETED] = True
                print("✅ Tarea marcada como completada")
                return

        print("❌ Error: No se encontró una tarea con ese ID")

    except Exception as e:
        print("❌ Error inesperado al completar la tarea:", e)


def delete_task(tasks, task_id):

    try:

        task_id = validar_task_id(task_id)

        if task_id is None:
            return

        for task in tasks:

            if task[KEY_ID] == task_id:

                confirm = input(
                    f"¿Seguro que deseas eliminar '{task[KEY_TITLE]}'? (s/n): "
                )

                if confirm.lower() != "s":
                    print("Eliminación cancelada.")
                    return

                tasks.remove(task)

                # Reasignar IDs
                for i, task in enumerate(tasks):
                    task[KEY_ID] = i + 1

                print("✅ Tarea eliminada correctamente.")
                return

        print("❌ Error: No se encontró una tarea con ese ID.")

    except Exception as e:
        print("❌ Error inesperado al eliminar la tarea:", e)