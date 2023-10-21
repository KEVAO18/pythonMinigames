import random
def save(numJugadores:int, ganadorUnint:int, ganadorDosInt:int, ganadorTresInt:int, noGanador:int, rand:int):
    
    porcentGanUna = ganadorUnint * ( 100 / numJugadores )
    
    porcentGanDos = ganadorDosInt * ( 100 / numJugadores )

    porcentGanTres = ganadorTresInt * ( 100 / numJugadores )
    
    porcentNoGan = noGanador * ( 100 / numJugadores )
    
    listFinished = {
        "jugadores": numJugadores,
        "uno": porcentGanUna,
        "dos": porcentGanDos,
        "tres": porcentGanTres,
        "no": porcentNoGan,
        "numero": rand
        }
    
    return listFinished

def juego(num:int, rand:int):

    if(num == rand):
        return "Ganador"
    elif((num > (rand-3)) and (num < (rand+3))):
        return "Caliente"
    elif((num > (rand-5)) and (num < (rand+5))):
        return "tibio"
    else:
        return "frio"

def jugador(rand:int):
    nom = input("\ningrese el nombre del jugador: ")
    
    turno = {
        "int":0,
        "nombre": nom
    }
    
    while(turno["int"] < 3):
        pregunta = int(input("\ningrese un numero: "))
        print(juego(pregunta, rand))
        if(juego(pregunta, rand) != "Ganador"):
            turno["int"] +=1
        else:
            break
        
    return turno

def gameplay(n:int, rand:int):
    
    listGame = {
        "jugadores": "",
        "uno": 0,
        "dos": 0,
        "tres": 0,
        "noGan": 0
        }
    
    i = 0
    
    while(i < n):
        
        player = jugador(rand)
        
        if(player["int"] == 0):
            listGame["jugadores"] += player["nombre"]+","
            listGame["uno"] += 1
        elif(player["int"] == 1):
            listGame["jugadores"] += player["nombre"]+","
            listGame["dos"] += 1
        elif(player["int"] == 2):
            listGame["jugadores"] += player["nombre"]+","
            listGame["tres"] += 1
        elif(player["int"] == 3):
            listGame["noGan"] += 1
            
        i += 1
    
    listFinished = save(n, listGame["uno"], listGame["dos"], listGame["tres"], listGame["noGan"], rand)
    
    print("\nGanadores: "+listGame["jugadores"])
    
    print("porcentaje de respuestas a la primera: "+str(listFinished["uno"]))

    print("porcentaje de respuestas a la segunda: "+str(listFinished["dos"]))

    print("porcentaje de respuestas a la tercera: "+str(listFinished["tres"]))
    
    print("porcentaje de no ganadores: "+str(listFinished["no"]))

    print("el numero era: "+str(listFinished["numero"]))

r = round(random.randint(1, 20))
gameplay(int(input("\nnumero de jugadores: ")), r)
