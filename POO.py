import os
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system ("cls")  
	print ("Selecciona tu animal favorito")
	print ("\t1 - Perrito""\U0001F436" )
	print ("\t2 - Caballito""\U0001F434")
	print ("\t3 - Murcielago""\U0001F987")
	print ("\t4 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
 	# solicitamos al usuario que elija una opción 
	opcionMenu = input("Inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("""
\n	   _=,_
\n	o_/6 /#\
\n	\__ |##/
\n	='|--\
\n	/   #'-.
\n	\#|_   _'-. /
\n	|/ \_( # |"
\n	C/ ,--___/""")
		input("Has pulsado la opción Perrito...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		print ("""
\n           ,--,
\n     _ ___/ /\|
\n ,;'( )__, )  ~
\n//  //   '--; 
\n'   \     | ^
\n     ^    ^ 
		""")
		input("Has pulsado la opción Caballito...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("""
\n		(_    ,_,    _) 
\n      / `'--) (--'` \
\n     /  _,-'\_/'-,_  \
\n    /.-'     "     '-.\	
		""")
		input("Has pulsado la opción Murcielago...\npulsa una tecla para continuar")
	elif opcionMenu=="4":
		break
	else:
		print ("")
		input("No has pulsado una opción correcta...\npulsa una tecla para continuar")