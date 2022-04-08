import sounddevice as sd
import soundfile as sf
import csv

def soundMood():
    sounds = ['lydfiler/Announcement.wav','lydfiler/applaus.wav','lydfiler/bane gennemført type beat.wav',
              'lydfiler/EM.wav','lydfiler/FamilyStore.wav','lydfiler/fuglesang.wav','lydfiler/GirlScream.wav',
              'lydfiler/GlassBreaking.wav','lydfiler/goblin agtig.wav','lydfiler/HalloweenImpact.wav',
              'lydfiler/HarpFlourish.wav','lydfiler/HipHopBeat.wav','lydfiler/horror sweep.wav',
              'lydfiler/hundehvalp.wav','lydfiler/kuglepen.wav','lydfiler/magisk fe.wav','lydfiler/ManScream.wav',
              'lydfiler/monster growl.wav','lydfiler/skrivemaskine.wav','lydfiler/Sky.wav','lydfiler/splatter.wav',
              'lydfiler/stikkontakt.wav','lydfiler/Tearing.wav','lydfiler/TuborgClassic.wav','lydfiler/Uprise.wav',
              'lydfiler/WeirdoScream.wav']
    currentSound = 0
    print("Sound mood determiner: ")
    print("1: Positive\n"
          "2: Neutral\n"
          "3: Negative")

    soundname = sounds[0][12:-4]


    filename = sounds[currentSound]
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    print(" ")
    currentMood = input("Type in 1 for positive, 2 for neutral or 3 for negative: ")
    if currentMood == 1:
        mood = 'Positive'
    if currentMood == 2:
        mood = 'Neutral'
    if currentMood == 3:
        mood = 'Negative'
    else:
        input("Type in 1 for positive, 2 for neutral or 3 for negative: ")

    header = ['Sound name', 'Mood']
    with open('CSV files/soundMoods.csv', mode='w', encoding='UTF8', newline='') as data_collection:
        data_collection = csv.writer(data_collection, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_collection.writerow(header)

    with open('CSV files/soundMoods.csv', mode='a', encoding='UTF8', newline='') as data_collection:
        data_collection = csv.writer(data_collection, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        row = [soundname, mood]
        data_collection.writerow(row)
    currentSound+1

soundMood()