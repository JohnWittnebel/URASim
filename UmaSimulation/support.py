from constants import BASIC_BOND_UP, CHARMING_BOND_UP

class Support:
    def __init__(self, defaultFacility, friendshipBonus, moodEffect, trainingBonus, bonusStats, initialStats, initialBond, raceBonus, hintFreq, prio):
        self.defaultFacility = defaultFacility
        self.friendshipBonus = friendshipBonus
        self.moodEffect = moodEffect
        self.trainingBonus = trainingBonus
        self.bonusStats = bonusStats
        self.initialStats = initialStats
        self.initialBond = initialBond
        self.raceBonus = raceBonus
        self.hintFreq = hintFreq
        self.prio = prio
        self.currBond = initialBond

    def trainWith(self, uma):
        if uma.charming:
            self.currBond += CHARMING_BOND_UP
        else:
            self.currBond += BASIC_BOND_UP