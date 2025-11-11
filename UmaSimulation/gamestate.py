# Main simulation

class GameState(uma):

    def __init__(self, uma):
        self.facilityLevels = [1,1,1,1,1]
        self.uma = uma

    def getFacilityLevel(self, facilityNum):
        return self.facilityLevels[facilityNum]

    def increaseFacilityLevel(self, facilityNum):
        self.facilityLevels[facilityNum] += 1

