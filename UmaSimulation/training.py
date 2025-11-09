#This is the function called assuming that we do not fail training
from constants import BASE_STATS, MOOD_ARR, BASE_ENERGY


def trainFacilitySucc(supports, fakeFaces, uma, facilityNum, facilityLevel):

    baseSpdIncrease = BASE_STATS[facilityNum][0][facilityLevel-1]
    baseStmIncrease = BASE_STATS[facilityNum][1][facilityLevel-1]
    basePowIncrease = BASE_STATS[facilityNum][2][facilityLevel-1]
    baseGutsIncrease = BASE_STATS[facilityNum][3][facilityLevel-1]
    baseWitIncrease = BASE_STATS[facilityNum][4][facilityLevel-1]
    baseSPIncrease = BASE_STATS[facilityNum][5][facilityLevel-1]

    numSupports = len(supports)
    moodEffect = MOOD_ARR[uma.mood]
    moodModifier = 0
    trainingEffect = 1.0
    baseBonus = uma.bonusSpd

    total_friend_multiplier = 1.0
    energy_recovery = 0
    energy_cost_reduction = 1.0

    for support in supports:
        trainingEffect += support.trainingBonus
        moodModifier += support.moodEffect

        if support.bond >= 80 and support.defaultFacility == facilityNum:
            total_friend_multiplier *= support.friendshipBonus
            energy_recovery += support.energyBoost
            energy_cost_reduction *= support.energyCostReduction

        # manages bond of supports only, does not influence stat calc
        support.trainWith(uma)

    total_mood_modifier = 1 + float(moodEffect * (100.0 + moodModifier) / 100)

    total_multiplier = baseBonus * (1 + float(0.5 * (numSupports + fakeFaces))) * trainingEffect * total_friend_multiplier * total_mood_modifier

    uma.spd += baseSpdIncrease * total_multiplier
    uma.stm += baseStmIncrease * total_multiplier
    uma.pow += basePowIncrease * total_multiplier
    uma.guts += baseGutsIncrease * total_multiplier
    uma.wit += baseWitIncrease * total_multiplier
    uma.sp += baseSPIncrease * total_multiplier

    if facilityNum < 4:
        uma.energy = max(0, uma.energy - ((BASE_ENERGY[facilityNum] + (facilityLevel - 1)) * energy_cost_reduction))
    else:
        uma.energy = min(100, uma.energy + energy_recovery - BASE_ENERGY[facilityNum])