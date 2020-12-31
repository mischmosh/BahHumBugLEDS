from neopixel import Color
from utils import Pattern

def split_color(c):
    """ Split a 32 bit color in GRB into three ints """
    b , c = c % 256 , c >> 8
    g , c = c % 256 , c >> 8
    r = c % 256
    return g, r, b

def make_color(g, r, b):
    c = r
    c = c << 8
    c += g
    c = c << 8
    c += b

class Colors(object):
    Red = make_color(0,255,0)
    Green = make_color(255, 0, 0)
    White = make_color(180,180,180)
    Blank = make_color(0,0,0)

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

