print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bienvenido a Treasure Island.")
print("Tu misión es encontrar el tesoro y no morir.")

choice1 = input('Estás en una encrucijada. ¿Hacia dónde quieres ir? Escribe "izquierda" o "derecha" \n').lower()
if choice1 == "izquierda":
  choice2 = input('Has llegado a un bosque oscuro. Puedes escuchar el sonido de un río cercano. ¿Quieres "explorar" el bosque o "seguir" el sonido del río? \n').lower()
  if choice2 == "explorar":
    choice3 = input("Te encuentras con una cueva misteriosa. ¿Quieres entrar en la cueva o seguir explorando el bosque? \n").lower()
    if choice3 == "entrar":
      print("Dentro de la cueva encuentras un tesoro escondido. ¡Felicidades, has ganado!")
    elif choice3 == "seguir explorando" or choice3 == "seguir":
      print("Sigues explorando el bosque y descubres una antigua ruina. ¡Es un hallazgo fascinante!")
    else:
      print("Te quedas parado sin tomar una decisión clara. Una sombra oscura te envuelve. Game Over.")
  elif choice2 == "seguir":
    print("Sigues el sonido del río y encuentras un puente colgante. Cruzas con cuidado y llegas a un hermoso prado. ¡Qué experiencia tan tranquila!")
  else:
    print("Te quedas indeciso en medio del bosque. La oscuridad te rodea. Game Over.")
else:
  print("Caminas hacia la derecha y te encuentras con un precipicio. No puedes seguir adelante. Game Over.")
