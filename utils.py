from argparse import Namespace
import itertools as it
import math
import time

class Pattern(object):

    def __init__(self, colors, width=10):
        self.colors = colors
        self.width = width

    def get_patch_color(self, i, w=0):
        w = w if w != 0 else self.width
        color_idx = (i // w) % len(self)
        return self.colors[color_idx]

    def __len__(self):
        return len(self.colors)

    def __iter__(self):
        w = self.width
        for i in it.count():
            yield self.get_patch_color(i,w)

    def make(self, n=0, w=0):
        for i in xrange(n) if n != 0 else it.count():
            yield self.get_patch_color(i, w)

class Pixels(object):
    """
        Represents a set of pixels (by default all pixels). A pattern can
        be appied to all pixels.
    """

    def __init__(self, strip):
        self.strip = strip
        self.pixels = range(self.strip.numPixels())

    def __len__(self):
        return len(self.pixels)

    def __getitem__(self, n):
        return self.pixels[n]

    def __iter__(self):
        return xrange(len(self))

    def set_pattern(self, pattern, offset=0, ms=0):
        for c , i in zip(pattern, xrange(len(self))):
            idx = (i+offset) % len(self)
            self.strip.setPixelColor(self[idx], c)
            if ms > 0:
                time.sleep(ms/1000.0)
                strip.show()
        self.strip.show()

    def rotate(self, step=1):
        for idx , new_p in enumerate( self[step:] + self[:step] ):
            c = self.strip.getPixelColor(self[idx])
            self.strip.setPixelColor(new_p, c)
        self.strip.show()

    def clear(self):
        """ Clear all pixels on strip """
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, 0)


class Word(Pixels):

    def __init__(self, strip, l1, l2, l3):
        self.strip = strip
        self.letter1 = l1
        self.letter2 = l2
        self.letter3 = l3

    def __iter__(self):
        return it.chain(self.letter1, self.letter2, self.letter3)

    def __getitem__(self, n):
        if isinstance(n, slice):
            return [self[i] for i in xrange(*n.indices(len(self)))]

        if n < -len(self) or n >= len(self):
            raise IndexError("Index %s not found" % n)

        l1, l2, l3 = len(self.letter1) , len(self.letter2) , len(self.letter3)

        if  l1+l2 <= n and n < l1+l2+l3:
            return self.letter3[n-l1-l2]
        elif l1 <= n and n < l1+l2:
            return self.letter2[n-l1]
        elif 0 <= n and n < l1:
            return self.letter1[n]
        elif -l3 <= n and n < 0:
            return self.letter3[n]
        elif -l3-l2 <= n and n < -l3:
            return self.letter2[n+l3]
        elif -l3-l2-l1 <= n and n < -l3-l2:
            return self.letter1[n+l3+l2]

    def __len__(self):
            return len(self.letter1) + len(self.letter2) + len(self.letter3)

    def set_letters(self, pattern1, pattern2=None, pattern3=None, offset1=0, offset2=None, offset3=None, ms=0):
        self.set_letter(self.letter1, pattern1, offset1, ms)
        self.set_letter(self.letter2, 
                pattern2 if pattern2 is not None else pattern1,
                offset2  if offset2  is not None else offset1,
                ms)
        self.set_letter(self.letter3, 
                pattern3 if pattern3 is not None else pattern1,
                offset3  if offset3  is not None else offset1,
                ms)
        self.strip.show()

    def set_letter(self, letter, pattern, offset=0, ms=0):
        if isinstance(letter, int):
            letter = self.get_letter(letter)

        if isinstance(pattern, int):
            for i in letter:
                self.strip.setPixelColor(i, pattern)
                if ms > 0:
                    time.sleep(ms/1000.0)
                    self.strip.show()
            return

        for c , i in zip(pattern, range(len(letter))):
            idx = (i+offset) % len(letter)
            self.strip.setPixelColor(letter[idx], c)
            if ms > 0:
                time.sleep(ms/1000.0)
                self.strip.show()

    def get_letter(self, i):
        if i == 1:
            return self.letter1
        elif i == 2:
            return self.letter2
        else:
            return self.letter3

    def rotate_letters(self, step1=1, step2=None, step3=None):
        self.rotate_letter(self.letter1, step1)
        self.rotate_letter(self.letter2, step2 if step2 is not None else step1)
        self.rotate_letter(self.letter3, step3 if step3 is not None else step1)
        self.strip.show()

    def rotate_letter(self, letter, step=1):
        for idx , new_p in enumerate( letter[step:] + letter[:step] ):
            c = self.strip.getPixelColor(letter[idx])
            self.strip.setPixelColor(new_p, c)

Effects = Namespace() # Object to hold custom effects
class Effect(object):

    def __init__(self, cps=0):
        self.cps = cps

    def __call__(self, word, sec=2, **kwargs):
        self.apply(word, sec, **kwargs)

    def apply(self, word, sec=2, **kwargs):
        cps = kwargs.get('cps', self.cps)
        
        num_cycles = int(sec * cps)
        cycle_wait = 1.0 / cps
        kwargs['num_cycles'] = num_cycles

        self.setup_vars(**kwargs)
        self.setup(word)

        if cps <= 0:
            # no animation pause for full duraction
            time.sleep(sec)
            return

        for i in range(num_cycles):
            self.cycle(word, i)
            time.sleep(cycle_wait)

        self.finish(word)

    def setup(self, word):
        pass

    def finish(self, word):
        pass

    def setup_vars(self, **kwargs):
        pass

    def cycle(self, word, i):
        pass

class RotateLettersEffect(Effect):
    
    def __init__(self, cps=20):
        self.cps = cps

        self.s1 , self.s2 , self.s3 = None , None , None
        self.p1 , self.p2 , self.p3 = None , None , None
        self.ms = 0

    def setup_vars(self, **kwargs):
        self.s1 = kwargs.get('s1', 1)
        self.s2 = kwargs.get('s2', self.s1)
        self.s3 = kwargs.get('s3', self.s1)

        self.p1 = kwargs.get('p1', self.p1)
        self.p2 = kwargs.get('p2', self.p1)
        self.p3 = kwargs.get('p3', self.p1)

        self.ms = kwargs.get('ms', self.ms)

    def setup(self, word):
        if self.p1 is not None:
            word.set_letters(self.p1, self.p2, self.p3, self.ms)

    def cycle(self, word, i):
        if self.p1 is not None:
            word.set_letters(self.p1, self.p2, self.p3, self.s1*i, self.s2*i, self.s3*i)
        else:
            word.rotate_letters(self.s1, self.s2, self.s3)

Effects.roatate_letters = RotateLettersEffect()

class FadeEffect(Effect):
    """ Fades Green, Red and White pixels. From start_bright (>=1) to end_bright (default: 255) """

    def __init__(self, cps=30, start_bright=1, end_bright=255, ms=0):
        self.cps = cps if cps > 0 else 0
        self.start_bright = start_bright if start_bright >=1 else 1
        self.end_bright = end_bright if end_bright <= 255 else 255
        self.ms = ms if ms > 0 else 0

    def setup_vars(self, **kwargs):
        self.cps = kwargs.get('cps', self.cps)
        if self.cps < 0: self.cps = 0

        self.start_bright = kwargs.get('start_bright', self.start_bright)
        if self.start_bright < 1: self.start_bright = 1

        self.end_bright = kwargs.get('end_bright', self.end_bright)
        if self.end_bright > 255: self.end_bright = 255

        self.delta  = (self.end_bright - self.start_bright) / (1.0 * kwargs.get('num_cycles',1))
        self.sign = 1 if self.delta >= 0 else -1
        self.delta = math.abs(self.delta)
        self.ms = kwargs.get('ms', self.ms)

    def setup(self, word):
        """ Set all colors to start_bright """
        for p in word:
            c = word.strip.getColor(p)
            word.strip.setColor(p, get_color(c, 0))
            if self.ms > 0:
                time.sleep(ms/1000.0)
            word.strip.show()

    def get_brightness(self, c, i):
        import colors # import here to avoid cyclical import
        v = int(self.start_bright + self.delta * i)
        g, r, b = colors.split_color(c)
        if g > r: # assume green
            g, r, b = v, 0, 0
        elif r > g: # assume red
            g, r, b = 0, v, 0
        else: # assume white
            g, r, b = v, v, v
        return colors.make_color(g, r, b)

    def cycle(self, word, i):
        for p in word:
            c = word.strip.getPixelColor(p)
            word.strip.setPixelColr(p,self.get_brightness(c,i))
            if self.ms > 0:
                    time.sleep(ms/1000.0)
            word.strip.show()
        word.strip.show()

Effects.fade = FadeEffect()

class ChaseLetterEffect(Effect):

    LOOP = 1
    BOUNCE = 2

    MODES = {
        LOOP: [ [0, 1, 2],
                [1, 2, 0],
                [2, 0, 1]],
        BOUNCE:[[0, 1, 2],
                [1, 2, 0],
                [2, 0, 1],
                [1, 2, 0]]
        }

    def __init__(self, pattern=None, cps=5, mode=LOOP):
        self.cps = cps
        self.pattern = pattern
        self.mode = mode

    def color_word(self, word, i=0):
        offsets = ChaseLetterEffect.MODES[self.mode]
        o = offsets[i % len(offsets)]
        word.set_letter(1, self.pattern.get_patch_color(o[0], 1))
        word.set_letter(2, self.pattern.get_patch_color(o[1], 1))
        word.set_letter(3, self.pattern.get_patch_color(o[2], 1))
        word.strip.show()

    def setup_vars(self, **kwargs):
        self.pattern = kwargs.get('pattern', self.pattern)
        self.mode = kwargs.get('mode', self.mode)

    def setup(self, word):
        self.color_word(word)

    def cycle(self, word, i):
        self.color_word(word, i)

Effects.chase_letter = ChaseLetterEffect()

if __name__ == '__main__':
    
    print 'Effect names and values'

    for name , value in Effects.__dict__.items():
        print '\t', name , value
