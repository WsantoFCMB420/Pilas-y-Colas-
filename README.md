Documentacion Activda Pials Y colas 
_________________________________________________________________________________________________________________________________________________________________________________________
1 Ejemplo Pilas
Simulación del historial de jugadas en ajedrez usando una pila

Este programa simula el almacenamiento del historial de jugadas en una partida de ajedrez usando una estructura de pila . Cada jugada se registra con la operación push, y si un jugador decide deshacer su última jugada, se utiliza la operación pop.

Funciones implementadas:
push: agrega una jugada al historial.

pop: elimina la última jugada.

isFull: verifica si la pila ha alcanzado su límite.

isEmpty: verifica si no hay jugadas registradas.

mostrar_historial: imprime las jugadas desde la más reciente a la más antigua.

Aplicación práctica:
En muchos videojuegos (como los de ajedrez), se usa una pila para implementar la función de "deshacer", ya que permite retirar la última acción realizada fácilmente.
_________________________________________________________________________________________________________________________________________________________________________________________
2 Ejemplo Pilas 
Simulación de apilado de cajas en una bodega usando una pila

Este programa simula el proceso de apilar cajas en una bodega utilizando una pila, donde solo se puede acceder a la caja superior. Las cajas se agregan con push y se retiran con pop, respetando la lógica LIFO (Last In, First Out).

Funciones implementadas:
push: coloca una nueva caja en la pila.

pop: retira la última caja apilada.

isFull: comprueba si la bodega está llena.

isEmpty: verifica si no hay cajas en la bodega.

mostrar_bodega: muestra el estado actual del apilado.

ste ejemplo se aplica en almacenes o centros de distribución donde las cajas se apilan verticalmente. Para acceder a las primeras, es necesario quitar las últimas primero, lo cual justifica el uso de una pila.
_________________________________________________________________________________________________________________________________________________________________________________________1 Ejemplo Colas
Simulación de cola de aviones esperando permiso para despegar

Este programa representa una cola de despegue en un aeropuerto. Cada avión entra en la cola con enqueue cuando está listo para despegar y sale de ella con dequeue cuando recibe autorización. El orden se mantiene estrictamente FIFO.

Funciones implementadas:
enqueue: agrega un nuevo avión al final de la cola.

dequeue: retira el primer avión (el más antiguo).

isFull: verifica si se alcanzó la capacidad máxima de espera.

isEmpty: indica si no hay aviones esperando.

mostrar_cola: muestra el orden actual de los vuelos.

Aplicación práctica:
Este modelo se utiliza en sistemas de gestión de tráfico aéreo para garantizar que los aviones despeguen en el orden correcto, evitando colisiones o retrasos por mal manejo de turnos.
_________________________________________________________________________________________________________________________________________________________________________________________2 Ejemplo Colas
Simulación de pacientes esperando resultados médicos usando una cola

Este programa modela una fila de pacientes que esperan la entrega de sus resultados médicos. Cada persona entra a la cola con enqueue, y cuando su turno llega, se le notifica usando dequeue.

Funciones implementadas:
enqueue: registra un nuevo paciente en la fila.

dequeue: entrega resultados al primer paciente.

isFull: determina si el laboratorio ha llegado a su máxima capacidad.

isEmpty: indica si no hay nadie esperando.

mostrar_cola: imprime la lista de pacientes en espera.

Aplicación práctica:
En sistemas hospitalarios o de laboratorio, las colas garantizan el orden de atención y evitan conflictos o saltos de turno. Es ideal para mantener la equidad y eficiencia en el servicio
____________________________________________________________________________________________________________________________________________________________Ejeplo PyC
Simulación de juego de cartas con pila y cola

Este programa simula un mini juego de cartas con dos estructuras de datos:

Una cola para representar el mazo (orden de robo).

Una pila para representar el montón de descarte (última carta jugada).

Los jugadores roban cartas del mazo (FIFO) y las descartan al montón (LIFO), reflejando cómo funcionan estas estructuras en contextos lúdicos y reales.

Funciones usadas:
Pila:

push: agrega carta al montón de descarte.

pop: retira la carta superior.

isEmpty, mostrar: para revisar estado.

Cola:

enqueue: agrega carta al mazo.

dequeue: jugador roba carta.

mezclar: mezcla las cartas del mazo.

Este ejemplo es ideal para demostrar cómo las pilas y colas pueden coexistir en sistemas reales, especialmente en videojuegos, simuladores, o cualquier sistema que requiera control sobre el orden de acciones.
____________________________________________________________________________________________________________________________________________________________