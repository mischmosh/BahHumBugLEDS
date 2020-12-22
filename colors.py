from neopixel import Color
from utils import Pattern

class Colors(object):
    Red = Color(0,255,0)
    Green = Color(255, 0, 0)
    White = Color(180,180,180)
    Blank = Color(0,0,0)

class Patterns(object):

    RedBlank =     Pattern([Colors.Red, Colors.Blank])
    Red1Blank3 =   Pattern([Colors.Red, Colors.Blank, Colors.Blank, Colors.Blank])
    GreenBlank =   Pattern([Colors.Green, Colors.Blank])
    Green1Blank3 = Pattern([Colors.Green, Colors.Blank, Colors.Blank, Colors.Blank])
    WhiteBlank =   Pattern([Colors.White, Colors.Blank])
    White1Blank3 = Pattern([Colors.White, Colors.Blank, Colors.Blank, Colors.Blank])

    RedGreen =   Pattern([Colors.Red, Colors.Green])
    Red1Green2 = Pattern([Colors.Red, Colors.Green, Colors.Green])
    Red2Green1 = Pattern([Colors.Red, Colors.Red, Colors.Green])
    Red4Green1 = Pattern([Colors.Red, Colors.Red, Colors.Red, Colors.Red, Colors.Green])
    Red1Green4 = Pattern([Colors.Red, Colors.Green, Colors.Green, Colors.Green, Colors.Green])

    CandyCane = Pattern([Colors.Red, Colors.White])
    CandyCaneRed = Pattern([Colors.Red, Colors.Red, Colors.White])
    CandyCaneWhite = Pattern([Colors.Red, Colors.White, Colors.White])

    Christmas = Pattern([Colors.Red, Colors.Green, Colors.White])
    ChristmasBlank = Pattern([Colors.Red, Colors.Green, Colors.White, Colors.Blank])
