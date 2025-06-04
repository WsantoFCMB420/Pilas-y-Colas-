# Implementación modificada de una pila para almacenar jugadas de ajedrez
class Pila:
    def __init__(self, cap_max):
        self.capacidad = cap_max  # Capacidad máxima permitida
        self.elementos = []  # Lista que actúa como la pila

    def esta_llena(self):
        """Devuelve True si la pila está completa."""
        return len(self.elementos) == self.capacidad

    def esta_vacia(self):
        """Devuelve True si no hay jugadas en la pila."""
        return len(self.elementos) == 0

    def apilar(self, movimiento):
        """Agrega una jugada en la cima de la pila."""
        if self.esta_llena():
            print("La pila está llena. No se puede insertar la jugada.")
        else:
            self.elementos.append(movimiento)
            print(f"Jugada guardada: {movimiento}")

    def desapilar(self):
        """Quita y devuelve la jugada más reciente."""
        if self.esta_vacia():
            print("La pila está vacía. No hay jugadas para deshacer.")
            return None
        else:
            jugada = self.elementos.pop()
            print(f"Jugada removida: {jugada}")
            return jugada

    def ver_historial(self):
        """Muestra todas las jugadas almacenadas hasta ahora."""
        if self.esta_vacia():
            print("No se han registrado jugadas.")
        else:
            print("Historial actual de jugadas:")
            for jugada in reversed(self.elementos):
                print(" ->", jugada)

# ------------------------------
# Ejemplo práctico del programa
# ------------------------------
if __name__ == "__main__":
    historial = Pila(10)  # Crear una pila con capacidad de 10 jugadas

    # Insertar jugadas simuladas
    historial.apilar("Peon E2 a E4")
    historial.apilar("Caballo G8 a F6")
    historial.apilar("Peon D2 a D4")
    historial.apilar("Alfil F8 a B4")

    historial.ver_historial()  # Mostrar jugadas

    # Deshacer la última jugada
    historial.desapilar()
    historial.ver_historial()
