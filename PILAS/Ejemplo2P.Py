# Ejemplo de uso de una pila para simular el apilado de cajas en una bodega

class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cajas = []
    def isFull(self):
        """Retorna True si la bodega esta llena."""
        return len(self.cajas) == self.capacidad
    def isEmpty(self):
        """Retorna True si la bodega esta vacia."""
        return len(self.cajas) == 0
    def push(self, caja):
        """Agrega una caja a la pila de la bodega."""
        if self.isFull():
            print(f" Bodega llena. No se puede agregar la caja: {caja}")
        else:
            self.cajas.append(caja)
            print(f" Caja agregada: {caja}")
    def pop(self):
        """Retira la última caja agregada."""
        if self.isEmpty():
            print(" La bodega esta vacia. No hay cajas para retirar.")
            return None
        else:
            caja = self.cajas.pop()
            print(f" Caja retirada: {caja}")
            return caja
    def mostrar_bodega(self):
        """Muestra el estado actual de la pila de cajas."""
        if self.isEmpty():
            print(" La bodega esta vacia.")
        else:
            print(" Estado actual de la bodega:")
            for i, caja in enumerate(reversed(self.cajas), 1):
                print(f" {i}. {caja}")

# --------------------------
# Simulación de bodega
# --------------------------

if __name__ == "__main__":
    bodega = Pila(5)

    bodega.push("Caja de herramientas")
    bodega.push("Caja de documentos")
    bodega.push("Caja de repuestos")
    bodega.push("Caja fragil")
    
    bodega.mostrar_bodega()

    bodega.pop()  # Retira la última caja
    bodega.mostrar_bodega()