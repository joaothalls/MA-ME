print "Programa faz convers�o de caracteres min�sculos para mai�sculos e vice-versa"

num = input("Aperte 1 para: min�sculo - Mai�sculo e 2 para: Mai�sculo - min�sculo ")
if (num == 1):
	print "min�sculo para Mai�sculo"
	texto = raw_input('Cole seu texto: ')
	print texto.upper()
	
 
elif (num == 2):
	print "Mai�sculo para min�sculo"
	texto = raw_input('Cole seu texto: ')
	print texto.lower()

else:
        print "Opc�o invalida!"
