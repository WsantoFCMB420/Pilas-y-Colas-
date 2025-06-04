# Simulación de un juego de cartas con pila y cola

import random

class Pila:
    def __init__(self):
        self.cartas = []

    def push(self, carta):
        """Agrega una carta al montón de descarte."""
        self.cartas.append(carta)

    def pop(self):
        """Retira la ultima carta jugada del monton de descarte."""
        return self.cartas.pop() if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.cartas) == 0

    def mostrar(self):
        """Muestra la carta en la parte superior del monton de descarte."""
        return self.cartas[-1] if not self.isEmpty() else "Ninguna"

class Cola:
    def __init__(self):
        self.cartas = []

    def enqueue(self, carta):
        """Agrega una carta al final del mazo."""
        self.cartas.append(carta)

    def dequeue(self):
        """Roba la carta mas antigua del mazo."""
        return self.cartas.pop(0) if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.cartas) == 0

    def mezclar(self):
        """Mezcla las cartas del mazo."""
        random.shuffle(self.cartas)

# --------------------------
# Simulación del juego
# --------------------------

if __name__ == "__main__":
    mazo = Cola()
    descarte = Pila()

    # Crear mazo de cartas
    cartas = [f"{valor} de {palo}" for palo in ["corazones", "diamantes", "tréboles", "picas"]
              for valor in ["A", "2", "3", "4", "5"]]
    
    for carta in cartas:
        mazo.enqueue(carta)
    
    mazo.mezclar()
    print("Mazo mezclado.")

    # Jugadores roban 3 cartas y las descartan
    for turno in range(3):
        carta = mazo.dequeue()
        if carta:
            print(f"Jugador roba: {carta}")
            descarte.push(carta)
            print(f"Descartada: {carta}")
    
    print(f"Carta en la cima del monton de descarte: {descarte.mostrar()}")