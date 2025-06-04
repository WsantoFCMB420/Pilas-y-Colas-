# Ejemplo de uso de una cola para gestionar el orden de despegue de aviones en un aeropuerto

class Cola:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.aviones = []
    def isFull(self):
        """Retorna True si la pista ya tiene la cola de despegue llena."""
        return len(self.aviones) == self.capacidad
    def isEmpty(self):
        """Retorna True si no hay aviones esperando."""
        return len(self.aviones) == 0
    def enqueue(self, avion):
        """Agrega un avion al final de la cola de espera."""
        if self.isFull():
            print(f" La cola de despegue esta llena. No puede agregarse: {avion}")
        else:
            self.aviones.append(avion)
            print(f" Avion en espera: {avion}")
    def dequeue(self):
        """Despega el primer avion en la cola."""
        if self.isEmpty():
            print(" No hay aviones en cola para despegar.")
            return None
        else:
            avion = self.aviones.pop(0)
            print(f" Avion autorizado para despegar: {avion}")
            return avion
    def mostrar_cola(self):
        """Muestra el estado actual de la cola de aviones."""
        if self.isEmpty():
            print(" No hay aviones esperando.")
        else:
            print(" Cola actual de despegue:")
            for i, avion in enumerate(self.aviones, 1):
                print(f" {i}. {avion}")

# --------------------------
# Simulación de cola de despegue
# --------------------------

if __name__ == "__main__":
    pista = Cola(5)

    pista.enqueue("Vuelo AV123")
    pista.enqueue("Vuelo LA234")
    pista.enqueue("Vuelo AA345")
    pista.mostrar_cola()

    pista.dequeue()
    pista.mostrar_cola()

