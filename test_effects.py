from __future__ import print_function

from colors import Colors, Patterns
from setup_bah_hum_bug import *
from utils import Effects


if __name__ == '__main__':

    register_signals()
    strip = make_strip()
    bah , hum , bug = make_words(strip)
    set_color(strip) # start with empty strip

    rotate_letters = RotateLettersEffect()
    fade_effect = FadeEffect()
    chase_letter_effect = ChaseLetterEffect()


    print ('Press Ctrl-C to quit.')
    while True:

        print('BAH: CandyCane with A rotating backwards')
        rotate_letters.apply(bah, sec=3, s1=1, s2=-3,
                p1=Patterns.CandyCane.make(),
                p2=Patterns.CandyCane.make(w=20))

        print('HUM: Red/Green rotating')
        rotate_letters.apply(hum, sec=3, s1=-2, s2=2,
                p1=Patterns.Red4Green1.make(),
                p2=Patterns.Red1Green4.make())

        print('BUG: Christmas draw and rotate')
        rotate_letters.apply(bug, sec=3, s1=1, s2=2, s3=3, ms=10,
                p1=Patterns.Christmas.make(w=20),
                p2=Patterns.Christmas.make(),
                p3=Patterns.Christmas.make(w=5))

        print("BAH: Green Red Green fade 4se")
        bah.set_letter(1, Colors.Green)
        bah.set_letter(2, Colors.Red)
        bah.set_letter(3, Colors.Green)
        strip.show()
        fade_effect.apply(bah, sec=4) 

        print("HUM: Red Green Red fade 2.5sec")
        hum.set_letter(1, Colors.Red)
        hum.set_letter(2, Colors.Green)
        hum.set_letter(3, Colors.Red)
        strip.show()
        fade_effect.apply(hum, sec=2.5) 

        print("BUG: Red Red Red fasde 1.5sec")
        bug.set_letter(1, Colors.Red)
        bug.set_letter(2, Colors.Red)
        bug.set_letter(3, Colors.Red)
        strip.show()
        fade_effect.apply(bug, sec=1.5) 

        print("BAH: Red Geen Green Chase Loop")
        chase_letter_effect.apply(bah, sec=3, pattern=Patterns.Red1Green2)

        print("HUM: Christmas Chase Loop")
        chase_letter_effect.apply(hum, sec=3, pattern=Patterns.Christmas)

        print("BUG: Christmas Chase Chase Bounce")
        chase_letter_effect.apply(bug, sec=3, pattern=Patterns.Christmas, mode=ChaseLetterEffect.BOUNCE)

