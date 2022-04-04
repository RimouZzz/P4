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

    while i < 15:
        j = random.randint(0, 1)

        speakerAngleVals = [0, 45, 90, 135, 180, 225, 270, 315]
        currentSpeakerAngle = random.choice(speakerAngleVals)
        speakerNr1 = speakerAngleVals.index(currentSpeakerAngle)
        speakerNr2 = speakerNr1+1
        if speakerNr1 == 7:
            speakerNr2 = 0
        currentDegree = currentSpeakerAngle + sounds['orientation'][j]

        print(f"playing {sounds['mood'][j]} sound {sounds['name'][j]} "
              f"on speakers {speakerNr1} and {speakerNr2} at angle {currentDegree}°")
        playsound(sounds['file'][j], block=False)

        while True:
            guess = int(input("Type in the angle: "))
            if guess == currentDegree:
                i += 1
                break
            else:
                print("try again")

        print(" ")


AudioDirection()
