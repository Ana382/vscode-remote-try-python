#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")
# write 'hello world' to the console
print("hello world")

if __name__ == "__main__":
    #menu con tres opciones
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    #seleccion de opcion y cambiar la entrada de elección a minúsculas
    opcion = int(input("Select your option: "))
    #validacion de opcion y cambiar la opcio
    if opcion == 1:
        print("You selected Rock")
    elif opcion == 2:
        print("You selected Paper")
    elif opcion == 3:
        print("You selected Scissors")
    else:
        print("Invalid option")
    #importar random
    import random
    #generar numero random
    num = random.randint(1,3)
    #validar numero random
    if num == 1:
        print("Computer selected Rock")
    elif num == 2:
        print("Computer selected Paper")
    elif num == 3:
        print("Computer selected Scissors")
    else:
        print("Invalid option")
    #Si gana se agrega uno al contador de ganadas
    win = 0
    #validar opciones
    if opcion == 1 and num == 1:
        print("Tie")
    elif opcion == 1 and num == 2:
        print("You lose")
    elif opcion == 1 and num == 3:
        print("You win")
        win = win + 1
    elif opcion == 2 and num == 1:
        print("You win")
        win = win + 1
    elif opcion == 2 and num == 2:
        print("Tie")
    elif opcion == 2 and num == 3:
        print("You lose")
    elif opcion == 3 and num == 1:
        print("You lose")
    elif opcion == 3 and num == 2:
        print("You win")
        win = win + 1
    elif opcion == 3 and num == 3:
        print("Tie")
    else:
        print("Invalid option")
    #mensaje final
    print("Thanks for playing")
    #se muestra menu para volver a jugar o para salir
    print("1. Play again")
    print("2. Exit")
    #seleccion de opcion
    opcion = int(input("Select your option: "))
    #validacion de opcion, si elige volver a jugar vuelve al menu principal con un ciclo while
    #Se agrega uno al contador cada avez que juega
    play = 1
    while opcion == 1:
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        opcion = int(input("Select your option: "))
        if opcion == 1:
            print("You selected Rock")
        elif opcion == 2:
            print("You selected Paper")
        elif opcion == 3:
            print("You selected Scissors")
        else:
            print("Invalid option")
        import random
        num = random.randint(1,3)
        if num == 1:
            print("Computer selected Rock")
        elif num == 2:
            print("Computer selected Paper")
        elif num == 3:
            print("Computer selected Scissors")
        else:
            print("Invalid option")
        if opcion == 1 and num == 1:
            print("Tie")
        elif opcion == 1 and num == 2:
            print("You lose")
        elif opcion == 1 and num == 3:
            print("You win")
            win = win + 1
        elif opcion == 2 and num == 1:
            print("You win")
            win = win + 1
        elif opcion == 2 and num == 2:
            print("Tie")
        elif opcion == 2 and num == 3:
            print("You lose")
        elif opcion == 3 and num == 1:
            print("You lose")
        elif opcion == 3 and num == 2:
            print("You win")
            win = win + 1
        elif opcion == 3 and num == 3:
            print("Tie")
        else:
            print("Invalid option")
        play = play + 1
        print("Thanks for playing")
        print("1. Play again")
        print("2. Exit")
        opcion = int(input("Select your option: "))
        #si elige salir se cierra el programa
        if opcion == 2:
            break
    #si elige salir se cierra el programa
    if opcion == 2:
        print("Thanks for playing")
        #se muestra un contador de las veces que el jugador ganó y cuantas veces jugó
        print("You won", win, "times")
        print("You played", play, "times")
        exit()
    #si elige salir se cierra el programa
    else:
        print("Invalid option")
        exit()

