import random


print("\nwesebi: \n"
+"qva vs furceli -> furceli moigebs \n"
+"qva vs makrateli -> qva moigebs \n"
+"furceli vs makrateli -> makrateli moigebs \n")



while True:
	print("\nmiutitet archevani \n 1. qva \n 2. furceli \n 3. makrateli \n")

	archevani = int(input("tqveni jeri: "))
	
	while archevani > 3 or archevani < 1:
		archevani = int(input("miutitet mocemuli archevnidan ert-erti: "))
        

	if archevani == 1:
		materialuri_archevani = '**qva**'
	elif archevani == 2:
		materialuri_archevani = '**furceli**'
	else:
		materialuri_archevani = '**makrateli**'


	print("tqveni archevania: " + materialuri_archevani)

	print("\naxla boti irchevs.....")
    


	botis_archevani = random.randint(1, 3)
	

	while botis_archevani == archevani:
		botis_archevani = random.randint(1, 3)


	if botis_archevani == 1:
		botis_materialuri_archevani = '**qva**'
	elif botis_archevani == 2:
		botis_materialuri_archevani = '**furceli**'
	else:
		botis_materialuri_archevani = '**makrateli**'
		
	print("botis archevania: " + botis_materialuri_archevani + "\n")
	print("////" + materialuri_archevani + " vs " + botis_materialuri_archevani + "\\\\\\" + "\n")

	if((archevani == 1 and botis_archevani == 2) or
	(archevani == 2 and botis_archevani ==1 )):
		print("furcelma moigo!\n")
		shedegi = "furceli"
		
	elif((archevani == 1 and botis_archevani == 3) or
		(archevani == 3 and botis_archevani == 1)):
		print("qvam moigo!\n")
		shedegi = "qva"
	else:
		print("makratelma moigo!\n")
		shedegi = "makrateli"


	if shedegi == materialuri_archevani:
		print("<== TQVEN MOIGET ==>\n")
	else:
		print("<== BOTMA MOGIGOT ==>\n")
		
	print("GINDAT KIDEV TAMASHI? (ara/Enter)")
	sss = input()


	if sss == 'ara':
		break
	

print("\nDIDI MADLOBA TAMASHISTVIS <3")
