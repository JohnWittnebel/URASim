# desired stam
STAM_THRESHOLD = 1000

# stat values
SPEED_VAL = 2
STAM_VAL = 3
POWER_VAL = 1
GUTS_VAL = 0.5
WIT_VAL = 0.5

#This doesnt seem to be documented anywhere, but SUCCESS_CHANCE = 100 - 2(BASE_ENERGY) seems
#like a reasonable estimate for failure chance. You need to add a little bit for different facilities

# facility trainings

BASE_SPD_ENERGY = 20
BASE_SPD = [10,0,2,0,0,1]

BASE_STM_ENERGY = 20
BASE_STM = [0,9,0,0,2,1]

BASE_POW_ENERGY = 20
BASE_POW = [0,2,9,0,0,1]

BASE_GUT_ENERGY = 20
BASE_GUTS = [2,0,2,9,0,1]

BASE_WIT_ENERGY = -5
BASE_WIT = [2,0,0,0,9,2]

BASE_STATS = [BASE_SPD, BASE_STM, BASE_POW, BASE_GUTS, BASE_WIT]
BASE_ENERGY = [BASE_SPD_ENERGY, BASE_STM_ENERGY,BASE_POW_ENERGY, BASE_GUTS, BASE_WIT_ENERGY]

# dictates how much bond friends are given when training together
BASIC_BOND_UP = 5
CHARMING_BOND_UP = 7

# mood modifiers
TERRIBLE = 0
BAD = 1
NORMAL = 2
GOOD = 3
GREAT = 4
MOOD_ARR = [-0.2, -0.1, 0, 0.1, 0.2]

DEFAULT_HINT_RATE = 0.075