import random
from playsound import playsound #Version 1.2.2

def AudioDirection():
    i = 0
    sounds = {
        'orientation': [32, 45],
        'file': ['clean.wav', 'test.wav'],
        'name': ["CLEAN GUITAR", "CLEAN GUITAR (RIGHT)"],
        'mood': ["Neutral", "Neutral"]
    }

    while(i < 15):
        #First number = which sound 2nd = direction of sound between two speakers
        j = random.randint(0,1)

        chosenSpeaker = random.randint(0,7) #Pick random speaker
        speaker2 = chosenSpeaker +1
        if chosenSpeaker == 7:
            speaker2 = 0

        print(f"playing sound {sounds['name'][j]} on speakers {chosenSpeaker} and {speaker2} at angle {sounds['orientation'][j]}")
        playsound(sounds['file'][j])

        while True:
            answer = sounds['orientation'][j]
            guess = int(input("Type in the angle: "))
            if guess == answer:
                i += 1
                break
            else:
                print("try again")

        print(" ")

AudioDirection()