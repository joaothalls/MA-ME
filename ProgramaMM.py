print "Programa faz conversão de caracteres minúsculos para maiúsculos e vice-versa"

num = input("Aperte 1 para: minúsculo - Maiúsculo e 2 para: Maiúsculo - minúsculo ")
if (num == 1):
	print "minúsculo para Maiúsculo"
	texto = raw_input('Cole seu texto: ')
	print texto.upper()
	
 
elif (num == 2):
	print "Maiúsculo para minúsculo"
	texto = raw_input('Cole seu texto: ')
	print texto.lower()

else:
        print "Opcão invalida!"
