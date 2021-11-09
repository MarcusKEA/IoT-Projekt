import haversine

class Player:
    """Class for hver enkelte GPS enhed"""

    def __init__(self, nwBorder:tuple, seBorder:tuple):
        self.nwBorder = nwBorder
        self.seBorder = seBorder
        self.borders = []

    #Udregner zonens 4 hjørner, ved hjælp af 2 modsatte hjørner.
    def calculate_borders(self, nwBorder:list, seBorder:list):
        borders = [nwBorder,
                    [seBorder[0],nwBorder[1]],
                    seBorder,
                    [nwBorder[0],seBorder[1]]]
        self.borders = borders
        print(borders)
        return borders

player1 = Player((1,9), (7,3))
player1Pos = [55.64266121248321, 12.612958544710214]

nextBorderCal = haversine.makeZone(player1Pos,5,10)

#Længde og breddegrader for zone
Player.calculate_borders(Player, nextBorderCal[0],nextBorderCal[1])

