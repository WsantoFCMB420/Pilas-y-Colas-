# Ejemplo de uso de una pila para almacenar el historial de jugadas en un juego de ajedrez
class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.items = []
    def isFull(self):
        """Retorna True si la pila está llena."""
        return len(self.items) == self.capacidad
    def isEmpty(self):
        """Retorna True si la pila esta vacia."""
        return len(self.items) == 0
    def push(self, elemento):
        """Inserta un elemento en la cima de la pila."""
        if self.isFull():
            print(" La pila esta llena. No se puede agregar la jugada.")
        else:
            self.items.append(elemento)
            print(f"Jugada agregada: {elemento}")
    def pop(self):
        """Elimina y retorna el elemento en la cima de la pila."""
        if self.isEmpty():
            print("La pila esta vacia. No hay jugadas para deshacer.")
            return None
        else:
            jugada = self.items.pop()
            print(f"Jugada deshecha: {jugada}")
            return jugada

    def mostrar_historial(self):
        """Muestra todas las jugadas registradas hasta ahora."""
        if self.isEmpty():
            print("No hay jugadas registradas.")
        else:
            print("Historial de jugadas:")
            for jugada in reversed(self.items):
                print(f" - {jugada}")

# --------------
# Ejemplo de uso
# --------------
if __name__ == "__main__":
    historial = Pila(10)

    # Simulación de jugadas
    historial.push("Peon E2 a E4")
    historial.push("Caballo G8 a F6")
    historial.push("Peon D2 a D4")
    historial.push("Alfil F8 a B4")

    historial.mostrar_historial()

    # Deshacer última jugada
    historial.pop()
    historial.mostrar_historial()