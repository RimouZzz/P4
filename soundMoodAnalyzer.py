import sounddevice as sd
import soundfile as sf
import soundMoodCSV

logToCSV = soundMoodCSV.csvWriter()


def soundMood():
    sounds = ['lydfiler/Announcement.wav', 'lydfiler/applaus.wav', 'lydfiler/bane gennemført type beat.wav',
              'lydfiler/EM.wav', 'lydfiler/FamilyStore.wav', 'lydfiler/fuglesang.wav', 'lydfiler/GirlScream.wav',
              'lydfiler/GlassBreaking.wav', 'lydfiler/goblin agtig.wav', 'lydfiler/HalloweenImpact.wav',
              'lydfiler/HarpFlourish.wav', 'lydfiler/HipHopBeat.wav', 'lydfiler/horror sweep.wav',
              'lydfiler/hundehvalp.wav', 'lydfiler/kuglepen.wav', 'lydfiler/magisk fe.wav', 'lydfiler/ManScream.wav',
              'lydfiler/monster growl.wav', 'lydfiler/skrivemaskine.wav', 'lydfiler/Sky.wav', 'lydfiler/splatter.wav',
              'lydfiler/stikkontakt.wav', 'lydfiler/Tearing.wav', 'lydfiler/TuborgClassic.wav', 'lydfiler/Uprise.wav',
              'lydfiler/WeirdoScream.wav']
    currentSound = 0
    mood = ''
    logToCSV.writeHeader()
    print("Sound mood determiner: ")
    print("1: Positive\n"
          "2: Neutral\n"
          "3: Negative")

    while currentSound < len(sounds):
        soundname = sounds[currentSound][9:-4]
        filename = sounds[currentSound]
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data, fs)
        print(" ")
        print(f"playing sound nr: {currentSound+1} out of {len(sounds)}")
        currentMood = int(input("Type in 1 for positive, 2 for neutral or 3 for negative: "))
        if currentMood == 1:
            mood = 'Positive'
        elif currentMood == 2:
            mood = 'Neutral'
        elif currentMood == 3:
            mood = 'Negative'
        else:
            input("Type in 1 for positive, 2 for neutral or 3 for negative: ")

        currentSound += 1
        print(" ")
        logToCSV.writeData(soundname, mood)

soundMood()
