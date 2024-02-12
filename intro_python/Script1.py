
rojo = "\033[91m"
verde = "\033[92m"
amarillo = "\033[93m"
azul = "\033[94m"
magenta = "\033[95m"
cyan = "\033[96m"
reset = "\033[0m"
fondo_amarillo= "\033[103m"

def main():

    j1 = input("Ingrese el nombre del jugador 1: ")
    j2 = input("Ingrese el nombre del jugador 2: ")

    print(cyan + j1 + " es el jugador 1" + reset)
    print(cyan + j2 + " es el jugador 2" + reset)

    mayoria = setsj1 = setsj2 = 0

    #entrada = True

    #while entrada:
        #try:
            #sets = int(input("Ingrese el número de sets a jugar: "))
    sets = 3
            #if sets > 0 and sets % 2 == 1:
                #entrada = False
    mayoria = (sets + 1) / 2

            #else:
                #print(rojo + "El número de sets debe ser impar" + reset)
       # except ValueError:
            #print(rojo + "La entrada debe ser un número" + reset)

    contador_sets = 0
    while setsj1 != mayoria and setsj2 != mayoria:
        contador_sets += 1

        if contador_sets == 1:
            print(verde + "\nPosicionarse en cancha")
        elif contador_sets % 2 == 0:
            print(verde + "Cambio de cancha")
        print(magenta + "\nSet " + str(contador_sets))
        print(magenta + "Sets: " + str(setsj1) + " - " + str(setsj2))
        if set(j1, j2) == 1:
            setsj1 += 1
        else:
            setsj2 += 1

    print(magenta + "Sets: " + str(setsj1) + " - " + str(setsj2))
    if setsj1 > setsj2:
        print(amarillo + "Ganador del partido: " + j1)
    else:
        print(amarillo + "Ganador del partido: " + j2)

def set(j1, j2):

    juegosj1 = juegosj2 = 0

    while (juegosj1 < 6 and juegosj2 < 6) or abs(juegosj1 - juegosj2) < 2 :
        print(azul + "\n** Nuevo juego **")
        print(azul + "Juegos: " + str(juegosj1) + " - " + str(juegosj2))

        if (juegosj1 + juegosj2) % 2 == 0 :
            print(verde + "Saca " + j1)
        else:
            print(verde + "Saca " + j2)

        if juego(j1, j2) == 1 :
            juegosj1 += 1
        else:
            juegosj2 += 1

    print(azul + "Juegos: " + str(juegosj1) + " - " + str(juegosj2))
    if juegosj1 > juegosj2:
        print(magenta + "\n### Ganador del set: " + j1 + " ###")
        return 1
    else:
        print(cyan + "\n### Ganador del set: " + j2 + " ###")
        return 2

def juego(j1, j2):

    puntaje = {0: 0, 1: 15, 2: 30, 3: 40, 4: "adv", 5: "gana"}
    deucej1 = deucej2 = puntosj1 = puntosj2 = 0

    entrada = seguir = True
    deuce = False
    contador_juego = 0

    while seguir:
        contador_juego += 1

        print(reset + "||||||| Partida" + str(contador_juego) + " |||||||")
        print(reset + "Marcador: " + str(puntaje[puntosj1]) + " - " + str(puntaje[puntosj2]))

        while(entrada):
            try:
                anotacion = int( input(reset + "Quién ganó el punto? (Ingresa 1 o 2): "))
                if anotacion == 1:
                    # punto a j1
                    puntosj1 += 1
                    entrada = False

                    if deuce:
                        if deucej2 == 1:
                            deucej1 = deucej2 =  0
                            puntosj1 = puntosj2 = 3
                        elif deucej1 == 0:
                            deucej1 += 1
                        else:  # Gana j1
                            msj_ganador(j1)
                            return 1

                elif anotacion == 2:  # punto a j2
                    puntosj2 += 1
                    entrada = False

                    if deuce:
                        if deucej1 == 1:
                            deucej1 = deucej2 = 0
                            puntosj1 = puntosj2 = 3
                        elif deucej2 == 0:
                            deucej2 += 1
                        else:  # Gana j2
                            msj_ganador(j2)
                            return 2
                else:
                    print(rojo + "La entrada debe ser 1 ó 2" + reset)
            except ValueError:
                print(rojo + "La entrada debe ser 1 ó 2" + reset)

        if puntosj1 == 3 and puntosj2 == 3:
            deuce = True

        if not deuce:
            if puntosj1 == 4:
                msj_ganador(j1)
                return 1
            elif puntosj2 == 4:
                msj_ganador(j2)
                return 2

        entrada = True


def msj_ganador(jugador):
    print(amarillo + "°°°°°°° Ganador del juego: " + jugador + " °°°°°°°")


if __name__ == "__main__":
    main()

