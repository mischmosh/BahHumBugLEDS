import signal
import sys
import time

from neopixel import *

# Custom library imports
from letters import *
from utils import *

# LED strip configuration:
LED_COUNT      = 303     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 195     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


def set_grb(strip, pixels=None, g=0, r=0, b=0, ms=0):
	""" 
	The strip uses a GRB varient so swap red and green.
	If no color value set for chanel use 0.
	If no pixels set use whole strip.
	"""
	set_color(strip, pixels, Color(g, r, b), ms)

def set_color(strip, pixels=None, color=0, ms=0):

	if pixels is None:
		pixels = range(strip.numPixels())

	for p in pixels:
		strip.setPixelColor(p, color)
		if ms > 0:
			time.sleep(ms/1000.0)
			strip.show()
	strip.show()

# Define a function for SIGTERM
def catch_signal(signal, fram):
	 print 'Lights Off Time To Go TO Bed BahHumBug'
         strip = make_strip()
         set_color(strip)
	 sys.exit(0)

def make_strip():
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

    # Intialize the library (must be called once before other functions).
    strip.begin()

    return strip

def make_words(strip):
    bah = Word(strip, letterB1, letterA2, letterH3)
    hum = Word(strip, letterH1, letterU2, letterM3)
    bug = Word(strip, letterB1, letterU2, letterG3)
    return bah , hum , bug
            
def register_signals():
    signal.signal(signal.SIGTERM, catch_signal)
    signal.signal(signal.SIGINT, catch_signal)
