import sounddevice as sd
import soundfile as sf
import random
import serial
import time


def AudioDirection():
    i = 0
    sounds = {
        'orientation': [22, 30, 40, 0, 22, 10, 15, 35, 40, 20, 10, 30, 45, 22, 0], #Currently random numbers, need to be updated
        'file': ['lydfiler/Negative-Med-Vinkel/lydfiler_Negative_GirlScream+22.wav',
                 'lydfiler/Negative-Med-Vinkel/lydfiler_Negative_GlassBreaking+30.wav',
                 'lydfiler/Negative-Med-Vinkel/lydfiler_Negative_ManScream+40.wav',
                 'lydfiler/Negative-Med-Vinkel/lydfiler_Negative_Monster_Growl+0.wav',
                 'lydfiler/Negative-Med-Vinkel/lydfiler_Negative_WeirdoScream+22.wav',
                 'lydfiler/Neutrale-Med-Vinkel/lydfiler_Neutral_Chatter+10.wav',
                 'lydfiler/Neutrale-Med-Vinkel/lydfiler_Neutral_HipHopBeat+15.wav',
                 'lydfiler/Neutrale-Med-Vinkel/lydfiler_Neutral_Kuglepen+35.wav',
                 'lydfiler/Neutrale-Med-Vinkel/lydfiler_Neutral_Skrivemaskine+40.wav',
                 'lydfiler/Neutrale-Med-Vinkel/lydfiler_Neutral_Stikkontakt+20.wav',
                 'lydfiler/Positive_Med_Vinkel/lydfiler_Positive_Announcement+10.wav',
                 'lydfiler/Positive_Med_Vinkel/lydfiler_Positive_Applaus+30.wav',
                 'lydfiler/Positive_Med_Vinkel/lydfiler_Positive_harpFlourish+45.wav',
                 'lydfiler/Positive_Med_Vinkel/lydfiler_Positive_LevelComplete+22.wav',
                 'lydfiler/Positive_Med_Vinkel/lydfiler_Positive_Uprise+0.wav'],
        'name': ["Girl Scream", "Glass Breaking", "Man scream", "Monster growl", "Weirdo scream", "Chatter",
                 "HipHop beat", "Kuglepen", "Skrivemaskine", "Stikkontakt", "Announcement", "applaus", "Harp floursih",
                 "Level complete", "Uprise"],
        'mood': ["Negative", "Negative", "Negative", "Negative", "Negative", "Neutral", "Neutral",
                 "Neutral", "Neutral", "Neutral", "Positive", "Positive", "Positive", "Positive", "Positive"]
    }

    arduino = serial.Serial('COM9', 9600) #Check portnummer i Arduino før start

    negativeSounds = [0, 1, 2, 3, 4]
    neutralSounds = [5, 6, 7, 8, 9]
    positiveSounds = [10, 11, 12, 13, 14]

    random.shuffle(negativeSounds)
    random.shuffle(neutralSounds)
    random.shuffle(positiveSounds)

    currentSounds = []
    for x, y, z in zip(negativeSounds, neutralSounds, positiveSounds):
        currentSounds += [x, y, z]

    while i < 15:
        print(f"current sound list: {currentSounds}")
        speakerAngleVals = [0, 45, 90, 135, 180, 225, 270, 315]
        currentSpeakerAngle = random.choice(speakerAngleVals)
        speakerNr1 = speakerAngleVals.index(currentSpeakerAngle)+1
        speakerNr2 = speakerNr1+1
        if speakerNr1 == 8:
            speakerNr2 = 1
        output_mapping = [speakerNr1, speakerNr2]
        currentDegree = currentSpeakerAngle + sounds['orientation'][currentSounds[0]]

        filename = sounds['file'][currentSounds[0]]
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data, fs, mapping=output_mapping, loop=True)
        start = time.time()
        print(f"playing {sounds['mood'][currentSounds[0]]} sound {sounds['name'][currentSounds[0]]} "
              f"on speakers {speakerNr1} and {speakerNr2} at angle {currentDegree}°")


        while True:
            arduinoRead = arduino.readline()
            arduinoToString = arduinoRead.decode()
            guess = int(arduinoToString)
            print(guess)
            guessSpectrum = [guess, guess-1, guess-2, guess-3, guess-4, guess-5, guess+1, guess+2, guess+3, guess+4, guess+5]
            if currentDegree in guessSpectrum:
                correctInputTimerStart = time.time()
                correctInputTimerStop = time.time()
                finalCorrectInputTime = int(correctInputTimerStop - correctInputTimerStart)
                if finalCorrectInputTime > 2:
                    print("2 seconds")

                currentSounds.pop(0)
                end = time.time()
                finalTime = str(end - start)
                print(f"elapsed time: {finalTime[:5]}")
                arduinoResponse = 'c'
                arduino.write(arduinoResponse.encode())
                i += 1
                break


AudioDirection()
