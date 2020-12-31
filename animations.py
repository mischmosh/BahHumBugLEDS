from __future__ import print_function
from collections import OrderedDict

import functools

import random
import time

# Local imports
from colors import *
from utils import *

class Animation(object):

    def __init__(self, sec=2):
        self.sec = sec

    def __call__(self, word, **kwargs):
        self.start(word, **kwargs)

    def start(self, word, sec=0, **kwargs):
        # clear pixels
        word.clear()
        self.sec = sec if sec > 0 else self.sec
        self.setup(word, **kwargs)
        word.strip.show()
        self.animate(word, **kwargs)
        self.finish(word, **kwargs)

    def setup(self, word, **kwargs):
        pass

    def animate(self, word, **kwargs):
        pass

    def finish(self, word, **kwargs):
        pass

    @property
    def is_animation(self):
        return True

    def wrap(self, **kwargs):
        f = functools.partial(self.start, **kwargs)
        f.is_animation = True
        return f

class AnimationHolder(OrderedDict):

    def __getattr__(self, name):
        if name in self:
            return self[name]
        if hasattr(self, name):
            return super(OrderedDict).__getattr__(name)
        raise AttributeError(name + ' not in holder')

    def __setattr__(self, name, value):
        """ Assign annimation types to main dict not as an attribute """
        if hasattr(value,'is_animation'):
            self[name] = value
        else:
            self.__dict__[name] = value # assigning to the dict of names in the class

    def get_random(self, blocked=None):
        blocked = set(blocked) if blocked else set()
        animations = list(self.values())

        a = random.choice(animations)
        if not set(self.values()) - blocked:
            # No items not blocked so return a random one
            return a

        # Return a random animation that is not blocked
        while a not in blocked:
            a = random.choice(animations)
        return a

Animations = AnimationHolder()


class CandyCaneRotating(Animation):
    """ Rotating candy cane letters.  L1 and L3 slow clockwise, L2 faster anticlockwise """

    def animate(self, word):
        Effects.rotate_letters.apply(word, sec=3, s1=-1, s2=3,
            p1=Patterns.CandyCane.make(),
            p2=Patterns.CandyCane.make(w=20))
Animations.candy_cane_rotating  = CandyCaneRotating()

class RedGreenRotating(Animation):
    """ Rotating red (L1, L3) and green (L2) letters """

    def animate(self, word):
        Effects.rotate_letters.apply(word, sec=3, s1=-1, s2=1,
            p1=Patterns.Red4Green1.make(),
            p2=Patterns.Red1Green4.make())
Animations.red_green_rotating  = RedGreenRotating()

class GreenRedRotating(Animation):
    """ Rotating green (L1, L3) and red (L2) letters """
 
    def animate(self, word):
        Effects.rotate_letters.apply(word, sec=3, s1=1, s2=-1,
            p1=Patterns.Red1Green4.make(),
            p2=Patterns.Red4Green1.make())
Animations.green_red_rotating = GreenRedRotating()

class ChristmasRotating(Animation):
    """ Christmas (Red, Gree, White) rotating letters """

    def animate(self, word):
        Effects.rotate_letters.apply(bug, sec=3, s1=2, s2=-2, ms=10,
            p1=Patterns.Christmas.make(w=20),
            p2=Patterns.Christmas.make(w=5),
            p3=Patterns.Christmas.make(w=10))
Animations.christmas_rotating = ChristmasRotating()

class SetupLetters(Animation):

    def __init__(self, sec=2):
        self.sec = 2
        self.p1 = Patterns.Christmas.make()
        self.p2 , self.p3 = None , None

    def setup(self, word, **kwargs):
        p1 = kwargs('p1', self.p1)
        p2 = kwargs('p2', self.p2)
        p3 = kwargs('p3', self.p3)
        ms = kwargs('ms', 0)
        word.set_letters(p1,p2,p3,ms=ms)

class FadeBase(SetupLetters):
    """ Base fade animation """

    def animate(self, word):
        Effects.fade.apply(word, self.sec)
Animations.fade_christmas = FadeBase()
Animations.fade_green  = FadeBase().wrap(p1=Colors.Green)
Animations.fade_red  = FadeBase().wrap(p1=Colors.Red)
Animations.fade_candy_cane  = FadeBase().wrap(p1=Patterns.CandyCane)
Animations.fade_red_green  = FadeBase().wrap(p1=Colors.Red, p2=Colors.Green)
Animations.fade_green_red  = FadeBase().wrap(p1=Colors.Green, p2=Colors.Red)

class FlashBase(SetupLetters):
    """ Base fade animation dark -> bright -> dark """

    def animate(self, word):
        Effects.fade.apply(word, self.sec/2)
        Effects.fade.apply(word, self.sec/2, start_bright=255, end_bright=1)
Animations.flash_christmas = FlashBase()
Animations.flash_green  = FlashBase().wrap(p1=Colors.Green)
Animations.flash_red  = FlashBase().wrap(p1=Colors.Red)
Animations.flash_candy_cane  = FlashBase().wrap(p1=Patterns.CandyCane)
Animations.flash_red_green  = FlashBase().wrap(p1=Colors.Red, p2=Colors.Green)
Animations.flash_green_red  = FlashBase().wrap(p1=Colors.Green, p2=Colors.Red)


if __name__ == '__main__':

    print('Animation names and values')

    for name , value in Animations.items():
        print(' - %s: %s' % (name, value.__class__.__doc__))
