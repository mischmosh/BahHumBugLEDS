# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import os
import random
import signal 
import sys
import time

from neopixel import *

# Custom library imports
from letters import *

# LED strip configuration:
LED_COUNT      = 303     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 195     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.

def theaterChase(strip, color, wait_ms=60, iterations=5, interval_size=3):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(interval_size):
			for i in range(0, strip.numPixels(), interval_size):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(),interval_size):
				strip.setPixelColor(i+q, 10)
	set_grb(strip) # clear pixels

def sparkleRandom(strip, pixels=None, sec=2, cps=20, frac=0.2):
	if pixels is None:
		pixels = range(strip.numPixels())

	set_grb(strip, pixels) # clear pixels

	cycles = int(sec * cps)
	cycle_length = 1.0 / cps
	for i in range(cycles):
		lit = random.sample(pixels, int(frac*len(pixels)))
		for p in lit:
			strip.setPixelColor(p, Color(200,200,200))
		strip.show()
		time.sleep(cycle_length)
	

def sparklePopRandom(strip, pixels=None, sec=2, cps=100):
	if pixels is None:
		pixels = range(strip.numPixels())

	set_grb(strip, pixels) # clear pixels

	pool = [ p for p in pixels]
	lit = []

	cycles = int(sec * cps)
	cycle_length = 1.0 / cps

	for i in range(cycles):
		# pop from pool
		lit.append( (pool.pop(random.randrange(len(pool))), 255) )
		still_lit = []
		for p , v in lit:
			if v > 0:
				strip.setPixelColor(p, Color(v,v,v))
				still_lit.append( (p, v-5))
			else:
				pool.append(p)
		lit = still_lit
		strip.show()
		time.sleep(cycle_length)
		

def sparkleChristmas(strip, pixels=None, sec=2, cps=10, w=4):
	if pixels is None:
		pixels = range(strip.numPixels())

	colors = [Color(255,0,0), Color(0,255,0), Color(200,200,200)]

	cycles = int(sec * cps)
	cycle_length = 1.0 / cps

	for i in range(cycles):
		for p_start in range(0, len(pixels), w):
			c = random.choice(colors)
			for p in range(p_start,p_start+w):
				if p < len(pixels):
					strip.setPixelColor(pixels[p],c)
			strip.show()
	time.sleep(cycle_length)
	

def paintCandyCane(strip, pixels=None, n=10):
	# n: number of pixels in batch
	if pixels is None:
		pixels = range(strip.numPixels())

	for idx , p in enumerate(pixels):
		color = Color(0, 255, 0) if (idx/n) % 2 == 0 else Color(200,200,200)
		strip.setPixelColor(p,color) 

def wave(strip, pixels=None, initPaint=None, sec=2, cps=60):
	""" Move the pixels along at fps for sec
	    initPaint: initial paint function (none keeps pixels as is)
	    sec: number of seconds to wave for.
	    cps: cycles per second (speed of wave)
	"""
	if pixels is None:
		pixels = range(strip.numPixels())

	if initPaint is not None:
		initPaint(strip, pixels)

	cycles = int(sec * cps)
	cycle_length = 1.0 / cps
	for i in range(cycles):
		rotateOnePixel(strip, pixels)
		time.sleep(cycle_length)
	
def rotateOnePixel(strip, pixels):
	prev_color = strip.getPixelColor(pixels[-1])	
	for idx in range(len(pixels)):
		tmp_color = strip.getPixelColor(pixels[idx])
		strip.setPixelColor(pixels[idx], prev_color)
		prev_color = tmp_color
	strip.show()

def rotateBUG(strip, sec=2, cps=10):

	cycles = int(sec * cps)
	cycle_length = 1.0 / cps
	for i in range(cycles):
		if i % 4 == 0:
			set_grb(strip, letterB1, r=255)
			set_grb(strip, letterA2, g=255)
			set_grb(strip, letterH3, g=255)
		elif i % 4 == 2:
			set_grb(strip, letterB1, g=255)
			set_grb(strip, letterA2, g=255)
			set_grb(strip, letterH3, r=255)
		else:
			set_grb(strip, letterB1, g=255)
			set_grb(strip, letterA2, r=255)
			set_grb(strip, letterH3, g=255)
		strip.show()
		time.sleep(cycle_length)

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


def sleep_ms(ms=0):
	if ms > 0:
		time.sleep(ms/1000.0)

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
			sleep_ms(ms)
			strip.show()
	strip.show()


# Define a function for SIGTERM
def lights_off(signal, fram):
	 print 'Lights Off Time To Go TO Bed BahHumBug'
	 set_grb(strip)
	 sys.exit(0)

# Main program logic follows:
if __name__ == '__main__':
	
	# Set SIGTERM handler to lights_off
	signal.signal(signal.SIGTERM, lights_off)
	signal.signal(signal.SIGINT, lights_off)

	# write current pid to file
	pid = os.getpid()
	pid_f = open('/home/pi/bahhumbugleds/bah_pid.txt','w')
	pid_f.write(str(pid))
	pid_f.close()


	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:

		# set_grb(strip, letterB1, g=255)
		# set_grb(strip, letterA2, r=255)
		# set_grb(strip, letterH3, g=255)
		# wave(strip, bah_pixels, sec=2, cps=200)
		rotateBUG(strip)
		set_grb(strip)

		wave(strip, hum_pixels, paintCandyCane, sec=2)
		set_grb(strip)

		sparkleChristmas(strip, bug_pixels, sec=2)
		set_grb(strip)

		sparklePopRandom(strip, sec=2)
		set_grb(strip)
