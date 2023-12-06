# Definimos la estructura que va a tener nuestro juego 3 x 3
def crear_tablero():
 tablero = [[" " for iterador in range (3)] for iterador in range(3)]
 return tablero

# Imprimimos el tablero
def imprimir_tablero(tablero):
 print("-" * 9)
 for fila in tablero:
  print(" | ".join(fila))
  print("-" * 9)

# Creamos función en caso de empate
def empate(tablero):
 return all(all(casilla != " " for casilla in fila) for fila in tablero)

# Creamos función para el ganador
def ganador(tablero, jugador):
  for i in range(3):
   if all(tablero [i][j] == jugador for j in range(3)) or all(tablero [j][i] == jugador for j in range(3)):
    return True
  if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
   return True
  return False

# Función principal de nuestro Tres en Línea
def tres_en_linea():
 tablero = crear_tablero()
 jugador_actual = 'X'
 print('Bienvenid@ al juego de Tres en Línea! 👾')
 imprimir_tablero(tablero)

 while True:
  imprimir_tablero(tablero)
  print(f'Turno de jugador {jugador_actual}')
  fila = int(input('Elige Fila 0, 1, 2: '))
  columna = int(input('Elige Columna 0, 1, 2:'))
  if tablero[fila][columna] == " ":
   tablero[fila][columna] = jugador_actual
   if ganador(tablero, jugador_actual):
    print(f'El jugador {jugador_actual} ha ganado! 🏆')
    break
   if empate(tablero):
    print('Empate! 🤝')
    break
   jugador_actual = 'O' if jugador_actual == 'X' else 'X'
  else:
   print('Casilla ocupada')


if __name__ == "__main__":
 tres_en_linea()

