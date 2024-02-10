
def main():

    j1 = input("Ingrese el nombre del jugador 1: ")
    j2 = input("Ingrese el nombre del jugador 2: ")

    sets = 0
    juegos = 6
    puntosj1 = 0
    puntosj2 = 0
    setsj1 = 0
    setsj2 = 0

    entrada = True
    puntaje = {0:0, 1:15, 2:30, 3:40, 4:"adv", 5:"gana"}
    deucej1 = 0
    deucej2 = 0

    while entrada:
        try:
            sets = int(input("Ingrese el número de sets a jugar: "))
            if sets > 0:
                entrada = False
            else:
                print("La entrada no es valida")
        except ValueError:
            print("La entrada no es valida")

    entrada = True
    deuce = False
    seguir = True

    #juegos
    for i in range(1, juegos+1):
        print("Juego " + str(i))
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
                            deucej1 = 0
                            deucej2 = 0
                        elif deucej1 == 0:
                            deucej1 += 1
                        else: # Gana j1
                            setsj1 += 1
                            #reiniciar contadores
                            puntosj1 = puntosj2 = deucej1 = deucej2 = 0
                            deuce = False

                elif anotacion == 2: #punto a j2
                    puntosj2 += 1
                    entrada = False

                    if deuce:
                        if deucej1 == 1:
                            deucej1 = 0
                            deucej2 = 0
                        elif deucej2 == 0:
                            deucej2+= 1
                        else: # Gana j2
                            setsj2 += 1
                            #reiniciar contadores
                            puntosj1 = puntosj2 = deucej1 = deucej2 = 0
                            deuce = False
                else:
                    print("La entrada no es válida")
            except ValueError:
                print("La entrada no es valida")



        if puntosj1 == 3 and puntosj2 == 3 :
            deuce = True

        if puntosj1 == 4 and deuce == False:
            msj_ganador(j1)
        elif puntosj2 == 4 and deuce == False:
            msj_ganador(j2)

        entrada = True


def msj_ganador(jugador):
    print("Ganador del juego: " + jugador)








if __name__ == "__main__":
    main()

