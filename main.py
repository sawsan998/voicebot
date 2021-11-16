import pyttsx3

engine = pyttsx3.init()

def outro():
	print("Shutting Down, Thank You")
	print("Procces Finished\n")
	print("Created on November 16, 2021\nWritten By: Sawsan Niom\n")

def heading():
	print("✄╭━━━╮╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╭━━━━╮╱╱╱╱╭╮")
	print("✄┃╭━╮┃╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱┃╭╮╭╮┃╱╱╱╱┃┃")
	print("✄┃╰━━┳━━┳╮╭╮╭┫╰━━┳━━┳━╋╯┃┃┣┻━┳━━┫╰━╮")
	print("✄╰━━╮┃╭╮┃╰╯╰╯┣━━╮┃╭╮┃╭╮╮┃┃┃┃━┫╭━┫╭╮┃")
	print("✄┃╰━╯┃╭╮┣╮╭╮╭┫╰━╯┃╭╮┃┃┃┃┃┃┃┃━┫╰━┫┃┃┃")
	print("✄╰━━━┻╯╰╯╰╯╰╯╰━━━┻╯╰┻╯╰╯╰╯╰━━┻━━┻╯╰╯")
	print("-------------------------------------------------------------------------------")
	print("welcome to VoiceBot bV_1.1.3 (beta version)")
	print("Set the voice by go to 'Voice Settings' then 'Voice change' menu FIRST")
	print("If you dont setup the voice this program will crash")
	print("-------------------------------------------------------------------------------")
	print("1: Voice Settings")
	print("2: Play your text")
	print("exit: Quit the program")

def voiceSettings():
	print("1: voice Change")
	print("2: Listen Voice")
	print("0: Back")

def playFunc():
	print("Write your speech below")
	print("0: back")

def voiSetHeading():
	print("This voice setting page")
	print("this system has 48 different language")
	print("You can type in numbers like 1,2,3,4,5,.....,46,47,48")
	print("The number must be from 1 to 48")



def mew(voic):
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[voic-1].id)

def eng(promt):
	mew(settInput)
	engine.say(promt)
	engine.runAndWait()


while(True):
	heading()
	mainMenuInput = str(input("Select Option[Main Menu]: "))
	if(mainMenuInput == "1"):
		voiceSettings()
		while(True):
			settingIn = str(input("Select Option[VoiceSettings Menu]: "))
			if(settingIn == "0"):
				break
			elif(settingIn == "2"):
				eng("Hello This is Voice test, 1 2 3 4 Voice testing")
				voiceSettings()
				continue
			elif(settingIn == "1"):
				voiSetHeading()
				settInput = int(input("Select Number[VoiceOption Menu]: "))
				mew(settInput)
				voiceSettings()
				continue

			else:
				print("Wrong input, Try Again")
				voiceSettings()
				continue
		continue

	elif(mainMenuInput == "2"):
		playFunc()
		while(True):
			playIn = str(input("Select Option[Play Menu]: "))
			if(playIn == "0"):
				break
			else:
				eng(playIn)
				playFunc()
				continue
		continue

	elif(mainMenuInput == "exit"):
		outro()
		break
	else:
		print("Wrong Input, Try Again")
		continue

