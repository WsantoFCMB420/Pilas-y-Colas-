# Versión modificada: Uso de una pila para simular el almacenamiento de cajas en una bodega

class Pila:
    def __init__(self, limite):
        self.capacidad = limite
        self.lista_cajas = []

    def esta_llena(self):
        """Devuelve True si la bodega está completa."""
        return len(self.lista_cajas) == self.capacidad

    def esta_vacia(self):
        """Devuelve True si la bodega no tiene cajas."""
        return len(self.lista_cajas) == 0

    def apilar(self, nueva_caja):
        """Añade una nueva caja en la cima de la pila."""
        if self.esta_llena():
            print(f"No se puede ingresar la caja (bodega llena): {nueva_caja}")
        else:
            self.lista_cajas.append(nueva_caja)
            print(f"Se agregó una caja: {nueva_caja}")

    def desapilar(self):
        """Saca la caja más reciente de la pila."""
        if self.esta_vacia():
            print("No hay cajas para retirar (bodega vacía).")
            return None
        else:
            caja_retirada = self.lista_cajas.pop()
            print(f"Caja retirada de la bodega: {caja_retirada}")
            return caja_retirada

    def ver_bodega(self):
        """Imprime el contenido actual de la pila de cajas."""
        if self.esta_vacia():
            print("No hay contenido en la bodega.")
        else:
            print("Contenido de la bodega (última caja al principio):")
            for idx, caja in enumerate(reversed(self.lista_cajas), start=1):
                print(f"{idx}) {caja}")
if __name__ == "__main__":
    bodega = Pila(5)  # Bodega con espacio para 5 cajas
    bodega.apilar("Caja con herramientas")
    bodega.apilar("Caja con papeles")
    bodega.apilar("Caja con repuestos")
    bodega.apilar("Caja frágil")
    bodega.ver_bodega()
    bodega.desapilar()  # Elimina la última caja
    bodega.ver_bodega()
