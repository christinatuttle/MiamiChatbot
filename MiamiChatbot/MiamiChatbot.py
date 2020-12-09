# MiamiChatbot.py - chat bot that asks and records responses based on language of trigger


# check if trigger is valid, set language for prompts
def set_language(trigger, prompts):
	if trigger == "Love Miami":
		prompts.extend(["What is your zipcode? ", 
					"How long have you lived in Miami? ", 
					"What is your favorite thing about Miami? ", 
					"If you could change one thing about Miami what would it be? ", 
					"How do you feel about the current leadership? ", 
					"Do you see yourself staying in Miami? "])
		return True
	elif trigger == "Amor Miami":
		prompts.extend(["¿Cuál es su código postal? ",
					"¿Cuánto tiempo has vivido en Miami? ",
					"¿Qué es lo que más te gusta de Miami? ",
					"Si pudieras cambiar una cosa de Miami, ¿cuál sería? ",
					"¿Cómo te sientes acerca del liderazgo actual? ",
					"¿Te ves en Miami? "])
		return True
	elif trigger == "Renmen Miami":
		prompts.extend(["Ki sa ki postal postal ou a? ", 
						"Depi konbyen tan ou rete nan Miami? ",
						"Ki bagay ou pi renmen sou Miami? ",
						"Si ou ta ka chanje yon sèl bagay sou Miami ki sa li ta dwe? ",
						"Kijan ou santi ou sou lidèchip aktyèl la? ",
						"Èske ou wè tèt ou rete nan Miami? "])
		return True
	else:
		return False



def main():
	prompts = []
	responses = []

	print("Welcome to the Miami Chatbot")
	while True:
		trigger = input("")
		if set_language(trigger, prompts):
			break
		elif trigger == "exit":
			exit()
	
	# ask questions + store user input
	for prompt in prompts:
		answer = input(prompt + '\n')
		responses.append(answer)

	# print questions + responses
	print("")
	for i in range(6):
		print(str(i+1) + ". " + prompts[i] + responses[i])

if __name__ == "__main__":
    main()


