class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.tareas_completadas = set()

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada.")

    def marcar_completada(self, tarea):
        if tarea in self.tareas:
            self.tareas_completadas.add(tarea)
            self.tareas.remove(tarea)
            print(f"Tarea '{tarea}' marcada como completada.")
        else:
            print(f"Tarea '{tarea}' no encontrada en la lista de tareas pendientes.")

    def proxima_tarea_pendiente(self):
        for tarea in self.tareas:
            if tarea not in self.tareas_completadas:
                return tarea
        return "No hay tareas pendientes."

# Inicializar el gestor de tareas
gestor_tareas = GestorTareas()

# Ejemplo de uso del sistema de gestión de tareas
gestor_tareas.agregar_tarea("Hacer la compra")
gestor_tareas.agregar_tarea("Preparar informe")
gestor_tareas.agregar_tarea("Llamar al cliente")

print("\nTareas pendientes:")
for tarea in gestor_tareas.tareas:
    print(tarea)

gestor_tareas.marcar_completada("Hacer la compra")
gestor_tareas.marcar_completada("Enviar correo")

print("\nTareas completadas:")
for tarea in gestor_tareas.tareas_completadas:
    print(tarea)

proxima_tarea = gestor_tareas.proxima_tarea_pendiente()
print("\nPróxima tarea pendiente:", proxima_tarea)
