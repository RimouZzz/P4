import sounddevice as sd
import soundfile as sf
import random
import serial
import time


def AudioDirection():
    i = 0
    sounds = {
        'orientation': [32, 45],
        'file': ['Sound Files/clean.wav', 'Sound Files/test.wav'],
        'name': ["CLEAN GUITAR", "CLEAN GUITAR (RIGHT)"],
        'mood': ["Neutral", "Neutral"]
    }

    arduino = serial.Serial('COM7', 9600)

    while i < 15:
        j = random.randint(0, 1)
        soundsQue = []

        speakerAngleVals = [0, 45, 90, 135, 180, 225, 270, 315]
        currentSpeakerAngle = random.choice(speakerAngleVals)
        speakerNr1 = speakerAngleVals.index(currentSpeakerAngle)
        speakerNr2 = speakerNr1+1
        if speakerNr1 == 7:
            speakerNr2 = 0
        currentDegree = currentSpeakerAngle + sounds['orientation'][j]

        filename = sounds['file'][j]
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data, fs)
        start = time.time()
        print(f"playing {sounds['mood'][j]} sound {sounds['name'][j]} "
              f"on speakers {speakerNr1} and {speakerNr2} at angle {currentDegree}°")


        while True:
            arduinoRead = arduino.readline()
            arduinoToString = arduinoRead.decode()
            guess = int(arduinoToString)
            if guess == currentDegree:
                end = time.time()
                finalTime = str(end - start)
                print(f"elapsed time: {finalTime[:5]}")
                arduinoResponse = 'c'
                arduino.write(arduinoResponse.encode())
                i += 1
                break


AudioDirection()
