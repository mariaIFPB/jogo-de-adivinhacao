import random
x = random.randint(1,100)
print("bem vindo! tente acertar o número!")
while (x > 0):
	parar = str(input("deseja continuar?"))
	if (parar == "sim"):
		for i in range (0,3):
			num = int(input("qual é o número?"))
			if (num < x):
				print ("o numero sorteado é MAIOR")
			elif (num == x):
				print("você acertou!")
				x = random.randint(1,100)
				break
			elif(num > x):
				print("o numero sorteado é menor")
			if (num != x):
				print ("você errou!")
	else:
		print("jogo finalisado!")
		print("obrigado por jogar!")
		break 
