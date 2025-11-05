#This is the function called assuming that we do not fail training
from constants import BASE_SPD_SPD, BASE_SPD_POW, MOOD_ARR


def trainSpeedSucc(supports, uma):

    baseSpdIncrease = BASE_SPD_SPD
    basePowIncrease = BASE_SPD_POW

    numSupports = len(supports)
    moodEffect = MOOD_ARR[uma.mood]
    moodModifier = 0
    trainingEffect = 0
    baseBonus = uma.bonusSpd

    for support in supports:
        trainingEffect += support.trainingBonus
        moodModifier += support.moodEffect

    totalMoodModifier = 1 + float(moodEffect * (100 + moodModifier) / 100)

    uma.spd += baseSpdIncrease * baseBonus * float(1 + 0.5 * numSupports)

