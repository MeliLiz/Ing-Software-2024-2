
def main():

    j1 = input("Ingrese el nombre del jugador 1: ")
    j2 = input("Ingrese el nombre del jugador 2: ")

    sets = setsj1 = setsj2 = 0

    entrada = True

    while entrada:
        try:
            sets = int(input("Ingrese el número de sets a jugar: "))
            if sets > 0 and sets % 2 == 1:
                entrada = False
                mayoria = (sets + 1) / 2
            else:
                print("La entrada no es valida")
        except ValueError:
            print("La entrada no es valida")

    contadorSets = 0
    while(setsj1 != mayoria and setsj2 != mayoria):
        contadorSets += 1

        if contadorSets == 1:
            print("Posicionarse en cancha")
        elif contadorSets % 2 == 0:
            print("Cambio de cancha")
        print("\nSet " + str(contadorSets))
        print("Sets: " + str(setsj1) + " - " + str(setsj2))
        if set(j1, j2) == 1:
            setsj1 += 1
        else:
            setsj2 += 1

    print("Sets: " + str(setsj1) + " - " + str(setsj2))
    if setsj1 > setsj2:
        print("Ganador del partido: " + j1)
    else:
        print("Ganador del partido" + j2)

def set(j1, j2):
    juegosj1 = juegosj2 = 0

    while (juegosj1 < 6 and juegosj2 < 6) or abs(juegosj1 - juegosj2) < 2 :
        print("** Nuevo juego **")
        print("Juegos: " + str(juegosj1) + " - " + str(juegosj2))

        if (juegosj1 + juegosj2) % 2 == 0 :
            print("Saca " + j1)
        else:
            print("Saca " + j2)

        if juego(j1, j2) == 1 :
            juegosj1 += 1
        else:
            juegosj2 += 1

    print("Juegos: " + str(juegosj1) + " - " + str(juegosj2))
    if juegosj1 > juegosj2 :
        print("\n### Ganador del set: " + j1 + " ###")
        return 1
    else:
        print("\n### Ganador del set: " + j2 + " ###")
        return 2

def juego(j1, j2):

    puntaje = {0: 0, 1: 15, 2: 30, 3: 40, 4: "adv", 5: "gana"}
    deucej1 = deucej2 = puntosj1 = puntosj2 = 0

    entrada = seguir = True
    deuce = False
    contador_juego = 0

    while seguir:
        contador_juego += 1

        print("||||||| Partida" + str(contador_juego) + " |||||||")
        print("Marcador: " + str(puntaje[puntosj1]) + " - " + str(puntaje[puntosj2]))

        while(entrada):
            try:
                anotacion = int( input("Quién ganó el punto? (Ingresa 1 o 2): "))
                if anotacion == 1:
                    #punto a j1
                    puntosj1 += 1
                    entrada = False

                    if deuce:
                        if deucej2 == 1:
                            deucej1 = deucej2 =  0
                            puntosj1 = puntosj2 = 3
                        elif deucej1 == 0:
                            deucej1 += 1
                        else: # Gana j1
                            msj_ganador(j1)
                            return 1

                elif anotacion == 2: #punto a j2
                    puntosj2 += 1
                    entrada = False

                    if deuce:
                        if deucej1 == 1:
                            deucej1 = deucej2 = 0
                            puntosj1 = puntosj2 = 3
                        elif deucej2 == 0:
                            deucej2+= 1
                        else: # Gana j2
                            msj_ganador(j2)
                            return 2
                else:
                    print("La entrada no es válida")
            except ValueError:
                print("La entrada no es valida")

        if puntosj1 == 3 and puntosj2 == 3 :
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
    print("°°°°°°° Ganador del juego: " + jugador + " °°°°°°°")








if __name__ == "__main__":
    main()

