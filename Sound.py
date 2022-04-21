import sounddevice as sd
import soundfile as sf
import random
import serial
import time


def AudioDirection():
    i = 0
    sounds = {
        'orientation': [16, 5, 12, 12, -16, -3, 3, -16, 1, -8, -14, -4, -12, 7, 17], #Currently random numbers, need to be updated
        'file': ['lydfiler/Negative/GirlScream.wav', 'lydfiler/Negative/GlassBreaking.wav',
                 'lydfiler/Negative/ManScream.wav', 'lydfiler/Negative/monster growl.wav',
                 'lydfiler/Negative/WeirdoScream.wav', 'lydfiler/Neutral/Chatter.wav',
                 'lydfiler/Neutral/HipHopBeat.wav', 'lydfiler/Neutral/kuglepen.wav',
                 'lydfiler/Neutral/skrivemaskine.wav', 'lydfiler/Neutral/stikkontakt.wav',
                 'lydfiler/Positive/Announcement.wav', 'lydfiler/Positive/applaus.wav',
                 'lydfiler/Positive/HarpFlourish.wav', 'lydfiler/Positive/Level complete.wav',
                 'lydfiler/Positive/Uprise.wav'],
        'name': ["Girl Scream", "Glass Breaking", "Man scream", "Monster growl", "Weirdo scream", "Chatter",
                 "HipHop beat", "Kuglepen", "Skrivemaskine", "Stikkontakt", "Announcement", "applaus", "Harp floursih",
                 "Level complete", "Uprise"],
        'mood': ["Negative", "Negative", "Negative", "Negative", "Negative", "Neutral", "Neutral",
                 "Neutral", "Neutral", "Neutral", "Positive", "Positive", "Positive", "Positive", "Positive"]
    }

    arduino = serial.Serial('COM9', 9600) #Check portnummer i Arduino før start

    while i < 15:
        currentSound = random.randint(0, 14)
        lastSound = currentSound
        if sounds['mood'][currentSound] == sounds['mood'][lastSound]:



        speakerAngleVals = [0, 45, 90, 135, 180, 225, 270, 315]
        currentSpeakerAngle = random.choice(speakerAngleVals)
        speakerNr1 = speakerAngleVals.index(currentSpeakerAngle)
        speakerNr2 = speakerNr1+1
        if speakerNr1 == 7:
            speakerNr2 = 0
        currentDegree = currentSpeakerAngle + sounds['orientation'][currentSound]

        filename = sounds['file'][currentSound]
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data, fs)
        start = time.time()
        print(f"playing {sounds['mood'][currentSound]} sound {sounds['name'][currentSound]} "
              f"on speakers {speakerNr1} and {speakerNr2} at angle {currentDegree}°")


        while True:
            arduinoRead = arduino.readline()
            arduinoToString = arduinoRead.decode()
            guess = int(arduinoToString)
            print(guess)
            if guess == currentDegree:
                end = time.time()
                finalTime = str(end - start)
                print(f"elapsed time: {finalTime[:5]}")
                arduinoResponse = 'c'
                arduino.write(arduinoResponse.encode())
                i += 1
                break


AudioDirection()
