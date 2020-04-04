from Tile import Tile


class Game:
    def __init__(self):
        self.moves = 0
        self._gameArray = []
        self._activeTilePos = []
        self._size = 5

        count = 0
        for r in range(self._size):
            self._gameArray.append([])
            for k in range(self._size):
                count += 1
                if not(r == self._size - 1 and k == self._size - 1):
                    self._gameArray[r].append(Tile(count))
                else:
                    self._gameArray[r].append(Tile(0))
                    self._activeTilePos = [r, k]
        self._findNeighbours()

    def moveTile(self, tile, dir):
        print(tile)
        print(self._gameArray[self._activeTilePos[0]][self._activeTilePos[1]])
        moveTilePos = self.findTile(tile)

        self._gameArray[moveTilePos[0]][moveTilePos[1]
                                        ] = self._gameArray[self._activeTilePos[0]][self._activeTilePos[1]]
        self._gameArray[self._activeTilePos[0]][self._activeTilePos[1]] = tile
        self._activeTilePos = moveTilePos

        self._findNeighbours()

    def move(self, dir):
        if(dir == "w"):
            if(self._gameArray[self._activeTilePos[0]][self._activeTilePos[1]].getNorth() == None):
                print("North not found")
            else:
                self.moveTile(
                    self._gameArray[self._activeTilePos[0]][self._activeTilePos[1]].getNorth(), "north")
        elif(dir == "d"):
            if(self._gameArray[self._activeTilePos[0]][self._activeTilePos[1]].getEast() == None):
                print("East not found")
            else:
                self.moveTile(
                    self._gameArray[self._activeTilePos[0]][self._activeTilePos[1]].getEast(), "east")
        elif(dir == "s"):
            if(self._gameArray[self._activeTilePos[0]][self._activeTilePos[1]].getSouth() == None):
                print("South not found")
            else:
                self.moveTile(
                    self._gameArray[self._activeTilePos[0]][self._activeTilePos[1]].getSouth(), "south")
        elif(dir == "a"):
            if(self._gameArray[self._activeTilePos[0]][self._activeTilePos[1]].getWest() == None):
                print("West not found")
            else:
                self.moveTile(
                    self._gameArray[self._activeTilePos[0]][self._activeTilePos[1]].getWest(), "west")

    def printBoard(self):
        for r in range(self._size):
            print()
            for k in range(self._size):
                tegn = self._gameArray[r][k].getNum()
                print(tegn, end="\t")

    def _findNeighbours(self):
        for r in range(self._size):
            for k in range(self._size):
                if(r-1 >= 0):
                    self._gameArray[r][k].setNorth(self._gameArray[r-1][k])
                else:
                    self._gameArray[r][k].setNorth(None)
                if(k+1 < len(self._gameArray[r])):
                    self._gameArray[r][k].setEast(self._gameArray[r][k+1])
                else:
                    self._gameArray[r][k].setEast(None)
                if(r+1 < len(self._gameArray)):
                    self._gameArray[r][k].setSouth(self._gameArray[r+1][k])
                else:
                    self._gameArray[r][k].setSouth(None)
                if(k-1 >= 0):
                    self._gameArray[r][k].setWest(self._gameArray[r][k-1])
                else:
                    self._gameArray[r][k].setWest(None)

    def findTile(self, tile):
        for r in range(len(self._gameArray)):
            for k in range(len(self._gameArray[r])):
                if (self._gameArray[r][k] == tile):
                    return [r, k]
