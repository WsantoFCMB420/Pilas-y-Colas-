# Simulación de pacientes esperando para recibir sus resultados médicos usando una cola

class Cola:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pacientes = []

    def isFull(self):
        """Retorna True si el laboratorio está al tope de pacientes en espera."""
        return len(self.pacientes) == self.capacidad

    def isEmpty(self):
        """Retorna True si no hay pacientes en la cola."""
        return len(self.pacientes) == 0

    def enqueue(self, paciente):
        """Agrega un paciente a la cola de espera."""
        if self.isFull():
            print(f" Laboratorio lleno. No puede ingresar: {paciente}")
        else:
            self.pacientes.append(paciente)
            print(f" Paciente registrado: {paciente}")

    def dequeue(self):
        """Atiende al primer paciente en la cola."""
        if self.isEmpty():
            print("⚠️No hay pacientes en espera.")
            return None
        else:
            paciente = self.pacientes.pop(0)
            print(f" Resultados listos para: {paciente}")
            return paciente

    def mostrar_cola(self):
        """Muestra los pacientes en espera."""
        if self.isEmpty():
            print(" No hay pacientes esperando.")
        else:
            print(" Pacientes en espera de resultados:")
            for i, paciente in enumerate(self.pacientes, 1):
                print(f" {i}. {paciente}")

# --------------------------
# Simulación de laboratorio
# --------------------------

if __name__ == "__main__":
    laboratorio = Cola(5)

    laboratorio.enqueue("Paciente: Diego Sanchez")
    laboratorio.enqueue("Paciente: Michael Suarez")
    laboratorio.enqueue("Paciente: Felipe Molina")
    laboratorio.mostrar_cola()

    laboratorio.dequeue()
    laboratorio.mostrar_cola()