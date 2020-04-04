class Tile:
    def __init__(self, paramNum):
        self.num = paramNum
        self.width = 40
        self.height = self.width

        self.north = None
        self.east = None
        self.south = None
        self.west = None

    # Get-functions

    def getNum(self):
        return self.num

    def getNorth(self):
        return self.north

    def getEast(self):
        return self.east

    def getSouth(self):
        return self.south

    def getWest(self):
        return self.west

    # Set-functions

    def setNorth(self, tile):
        self.north = tile

    def setEast(self, tile):
        self.east = tile

    def setSouth(self, tile):
        self.south = tile

    def setWest(self, tile):
        self.west = tile

    def __str__(self):
        return str(self.num)
