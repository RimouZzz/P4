import csv
import time

header = ['TestNr.', 'Age', 'Female', 'Hearing', 'Blindfold?', 'ReactionTime', 'SoundName', 'SoundMood', 'SpeakerNr', 'Precision']
timeString = time.strftime("%d%m%Y-%H%M%S")

testNum = int(input("Test nr:"))
age = int(input("Age: "))
gender = int(input("Gender (0 = F, 1 = M): "))
if gender == 0:
    female = True
else:
    female = False
hearing = int(input("Hearing Rate: "))
Blindfolded = int(input("Blindfold (0 = True, 1 = False): "))
if Blindfolded == 0:
    blind = True
else:
    blind = False

class csvWriter():
    def writeHeader(self):
        with open(f'CSV files/SoundReaction{timeString}.csv', mode='w', encoding='UTF8', newline='') as data_collection:
            data_collection = csv.writer(data_collection, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_collection.writerow(header)

    def writeData(self, testNo, age, Gender, Hearing, blind, ReactionTime, SoundName, SoundMood, speakerNr, Precision):
        with open(f'CSV files/SoundReaction{timeString}.csv', mode='a', encoding='UTF8', newline='') as data_collection:
            data_collection = csv.writer(data_collection, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            row = [testNo, age, Gender, Hearing, blind, ReactionTime, SoundName, SoundMood, speakerNr, Precision]
            data_collection.writerow(row)
