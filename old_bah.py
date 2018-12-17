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
	for b in range(303):
		strip.setPixelColor(b, 0)
		strip.show()
#		time.sleep(wait_ms/100000)

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

letterB1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,90,91,92,93,94]
letterA2 = [100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,180,181,182,183,184]
letterH3 = [185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,274,275,276,277,278,279,280,281,282,283,284,285] 

letterH1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
letterU2 = [125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179]
letterM3 = [185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253]

letterG3 = [191,192,193,194,195,196,197,198,199,200,201,237,238,246,247,248,249,250,251,252,253,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303]

def bah(strip, wait_ms=5):
	"""BAH"""
	for h in letterB1:
		strip.setPixelColorRGB(h, 0, 255, 0)
	for i in letterA2:
		strip.setPixelColorRGB(i, 0, 255, 0)
	for j in letterH3:
		strip.setPixelColorRGB(j, 0, 255, 0)
		strip.show()
#		time.sleep (wait_ms/100.0)

def hum(strip, wait_ms=5):
	"""HUM"""
	for h in letterH1:
		strip.setPixelColorRGB(h, 0,255,0)
	for i in letterU2:
		strip.setPixelColorRGB(i, 0,255,0)
	for j in letterM3:
		strip.setPixelColorRGB(j, 0,255,0)
		strip.show()

def bug(strip, wait_ms=5):
	"""BUG"""
	for h in letterB1:
		strip.setPixelColorRGB(h, 0, 255, 0)
	for i in letterU2:
		strip.setPixelColorRGB(i, 0, 255, 0)
	for j in letterG3:
		strip.setPixelColorRGB(j, 0, 255, 0)
		strip.show()

# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		# Theater chase animations.
		theaterChase(strip, Color(127, 127, 127))  # White theater chase

#		lightWipe(strip)  # lights out
		strip._cleanup
		bah(strip)
		time.sleep(2)

		theaterChase(strip, Color(127,127,127))
#		lightWipe(strip)
		hum(strip)
		time.sleep(2)

		theaterChase(strip, Color(127,127,127))
#		lightWipe(strip)
		bug(strip)
		time.sleep(2)

		theaterChase(strip, Color(127,127,127))
