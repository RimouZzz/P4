import random
i = 0
prevSpeaker = 10
while i < 15:
    speakerAngleVals = [0, 45, 90, 135, 180, 225, 270, 315]
    currentSpeakerAngle = random.choice(speakerAngleVals)
    speakerNr1 = speakerAngleVals.index(currentSpeakerAngle) + 1
    speakerNr2 = speakerNr1 + 1
    if speakerNr1 == 8:
        speakerNr2 = 1
    while prevSpeaker == speakerNr1:
        currentSpeakerAngle = random.choice(speakerAngleVals)
        speakerNr1 = speakerAngleVals.index(currentSpeakerAngle) + 1
        print("reroll")
    prevSpeaker = speakerNr1
    print(f"speaker nr: {speakerNr1}")
    i += 1