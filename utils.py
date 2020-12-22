import itertools as it
import time

class Pixels(object):

    def __init__(self, strip):
        self.strip = strip

    def __len__(self):
        return self.strip.numPixels()

    def __getitem__(self, n):
        return list(range(len(self)))[n]

    def __iter__(self):
        return xrange(self.strip.numPixels())

    def set_pattern(self, pattern, offset=0, ms=0):
        for c , i in zip(pattern, range(len(self))):
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


class Effect(object):

    # Flags for clearing strip before and after effect
    BOTH   = 0b11
    BEFORE = 0b10
    AFTER  = 0b01
    NONE   = 0b00

    def __init__(self, cps=0, clear=BOTH):
        self.cps = cps
        self.clear = clear

    def apply(self, word, sec=2, **kwargs):
        clear = kwargs.get('clear', self.clear)
        cps = kwargs.get('cps', self.cps)
        

        num_cycles = int(sec * cps)
        cycle_wait = 1.0 / cps
        kwargs['num_cycles'] = num_cycles

        self.setup_vars(**kwargs)

        if clear & Effect.BEFORE:
            word.clear()

        self.setup(word)

        if cps <= 0:
            # no animation pause for full duraction
            time.sleep(sec)
            return

        for i in range(num_cycles):
            self.cycle(word, i)
            time.sleep(cycle_wait)

        self.finish(word)

        if clear & Effect.AFTER:
            word.clear()

    def setup(self, word):
        pass

    def finish(self, word):
        pass

    def setup_vars(self, **kwargs):
        pass

    def cycle(self, word, i):
        pass

class RotateLettersEffect(Effect):
    
    def __init__(self, cps=50, clear=None):
        self.cps = cps
        self.clear = clear if clear is not None else Effect.BOTH 

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

class FadeEffect(Effect):

    def __init__(self, cps=60, start_bright=10, end_bright=255, clear=Effect.AFTER):
        self.cps = cps
        self.clear = clear
        self.start_bright = start_bright
        self.end_bright = end_bright

    def setup_vars(self, **kwargs):
        self.cps = kwargs.get('cps', self.cps)
        self.start_bright = kwargs.get('start_bright', self.start_bright)
        self.end_bright = kwargs.get('end_bright', self.end_bright)
        self.num_cycles = kwargs['num_cycles']

    def setup(self, word):
        self.initial_bright = word.strip.getBrightness()
        word.strip.setBrightness(self.start_bright)

    def get_brightness(self, i):
        delta = (self.end_bright - self.start_bright) * ( 1.0 * i / self.num_cycles )
        return int(self.start_bright + delta)

    def cycle(self, word, i):
        word.strip.setBrightness(self.get_brightness(i))

    def finish(self, word):
        word.strip.setBrightness(self.initial_bright)

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

    def __init__(self, pattern=None, cps=5, clear=Effect.BOTH, mode=LOOP):
        self.cps = cps
        self.pattern = pattern
        self.clear = clear
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


