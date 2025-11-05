from constants import NORMAL

class Uma:
    def __init__(self, baseSpd, baseStm, basePow, baseGuts, baseWit, bonusSpd, bonusStm, bonusPow, bonusGuts, bonusWit):
        self.baseSpd = baseSpd
        self.baseStm = baseStm
        self.basePow = basePow
        self.baseGuts = baseGuts
        self.baseWit = baseWit
        self.bonusSpd = bonusSpd
        self.bonusStm = bonusStm
        self.bonusPow = bonusPow
        self.bonusGuts = bonusGuts
        self.bonusWit = bonusWit

        self.charming = False
        self.mood = NORMAL
        self.spd = baseSpd
        self.stm = baseStm
        self.pow = basePow
        self.guts = baseGuts
        self.wit = baseWit