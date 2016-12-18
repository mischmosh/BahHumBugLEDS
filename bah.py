# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *

# LED strip configuration:
LED_COUNT      = 303     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 195     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=20):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()): 
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def lightWipe(strip, wait_ms=2):
	for b in range(300):
		strip.setPixelColor(b, 0)
		strip.show()
		time.sleep(wait_ms/100000)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def numb(strip, wait_ms=20):
	for H in range(46):
		if H < 4:
			strip.setPixelColorRGB(H, 0, 255, 0) 
		elif H > 8:
	
			strip.setPixelColorRGB(H, 240, 128, 0)
#		elif H -= 16
		#	H -= 17
#			strip.setPixelColorRGB(H, 210, 12, 100)	
	for H in range(100):
		if H > 47:
			strip.setPixelColorRGB(H, 10, 123, 123)	
	strip.show()
	time.sleep (wait_ms/10.0)
	
#def flicker(color,
			
#		strip.show()
#		time.sleep(wait_ms/10

#def BAHHUMBUG(strip, wait_ms=200, iterations=3):
#	"""Sequence BAH-HUM-BUG"""
#		if
#		strip.show()
#		time.sleep (wait_ms/1000.0)
letterH = [0,5,10,15,20,25,30,35,40,45,55,60,65,70,75,80,85,90,95]
letterB = [100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195]
letterA = [200,205,210,215,220,225,230,235,240,245,250,255,260,265,270,275,280,285,290,295,300]

def bah(strip, wait_ms=20):
	"""BAH"""
	for h in letterH:
		strip.setPixelColorRGB(h, 123, 125, 198)
	for i in letterB:
		strip.setPixelColorRGB(i, 200, 120, 20)
	for j in letterA:
		strip.setPixelColorRGB(j, 240, 128, 0)
		strip.show()
#		time.sleep (wait_ms/100.0)

#def HUM(strip, wait_ms=100):



#def BUG(strip, wait_ms=100):

# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		# Color wipe animations.
#		colorWipe(strip, Color(0, 255, 0))  # Red wipe
#		colorWipe(strip, Color(63, 255, 0)) # Orange wipe
#		colorWipe(strip, Color(127, 255, 0)) # Yellow wipe
#		colorWipe(strip, Color(255, 0, 0))  # Green wipe
#		colorWipe(strip, Color(0, 0, 255))  # Blue wipe
#		colorWipe(strip, Color(0, 63, 255)) # Purple?
		# Theater chase animations.
#		theaterChase(strip, Color(127, 127, 127))  # White theater chase
#		theaterChase(strip, Color(127,   0,   0))  # Green theater chase
#		theaterChase(strip, Color(127, 255,   0))  # Yellow?
#		theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
#		theaterChase(strip, Color(  0, 127,   0))  # Red
		# Rainbow animations.
#		rainbow(strip)
#		rainbowCycle(strip)
#		theaterChaseRainbow(strip)
		lightWipe(strip)
		bah(strip)
		time.sleep(wait_ms/10000)
#		lightWipe(strip)
#		numb(strip)

#		colorWipe(strip, Color(0, 0, 0)) # turn off
