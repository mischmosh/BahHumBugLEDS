# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import datetime

from neopixel import *


# LED strip configuration:
LED_COUNT      = 303     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 195     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.

def theaterChase(strip, color, wait_ms=60, iterations=5):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)


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

chaseB1a = [0,3,6, 9,12,15,18,21,   25,28,31,34,37,40,43,46,49,52,55,58,61,64,67,70,   92]
chaseB1b = [1,4,7,10,13,16,19,   23,26,29,32,35,38,41,44,47,50,53,56,59,62,65,68,71,90,93]
chaseB1c = [2,5,8,11,14,17,20,   24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,   91,94]

letterA2 = [100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,180,181,182,183,184]

chaseA2a = [100,103,106,109,112,115,118,121,124,127,130,133,136,139,    181,184,    143,146]
chaseA2b = [101,104,107,110,113,116,119,122,125,128,131,134,137,140,    182,    141,144]
chaseA2c = [102,105,108,111,114,117,120,123,126,129,132,135,138,    180,183,    142,145]

letterH3 = [185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,274,275,276,277,278,279,280,281,282,283,284,285] 

chaseH3a = [185,188,191,194,197,200,203,206,231,234,237,240,243,246,249,252,274,277,280,283]
chaseH3b = [186,189,192,195,198,201,204,207,232,235,238,241,244,247,250,253,275,278,281,284]
chaseH3c = [187,190,193,196,199,202,205,    233,236,239,242,245,248,251,    276,279,282,285]

letterH1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]

chaseH1a = [0,3,6, 9,12,15,18,21,64,67,70,73,76,   79,82,85,88,91,94,97]
chaseH1b = [1,4,7,10,13,16,19,   65,68,71,74,   77,80,83,86,89,92,95,98]
chaseH1c = [2,5,8,11,14,17,20,   66,69,72,75,   78,81,84,87,90,93,96,99]

letterU2 = [125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179]

chaseU2a = [    127,130,133,136,139,    181,184,147,150,153,156,159,162,165,168,171,174,177]
chaseU2b = [125,128,131,134,137,140,    182,    148,151,154,157,160,163,166,169,172,175,178]
chaseU2c = [126,129,132,135,138,    180,183,    149,152,155,158,161,164,167,170,173,176,179]

letterM3 = [185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253]

chaseM3a = [185,188,191,194,197,200,203,206,209,212,215,218,221,224,227,230,233,236,239,242,245,248,251]
chaseM3b = [186,189,192,195,198,201,204,207,210,213,216,219,222,225,228,231,234,237,240,243,246,249,252]
chaseM3c = [187,190,193,196,199,202,205,208,211,214,217,220,223,226,229,232,235,238,241,244,247,250,253]

letterG3 = [191,192,193,194,195,196,197,198,199,200,201,237,238,246,247,248,249,250,251,252,253,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303]

chaseG3a = [191,194,197,200,    237,287,290,293,296,299,302,  255,258,261,264,267,270,    248,251]
chaseG3b = [192,195,198,201,        286,289,292,295,298,301,  256,259,262,265,268,271,246,249,252]
chaseG3c = [193,196,199,    236,    288,291,294,297,300,303,  257,260,263,266,269,272,247,250,253]

#, wait_ms=60, iterations=5
def bah(strip, color):
	"""BAH"""
	for p in range(iterations):
	        for q in range(3):
        		for h in chaseB1a:
                		strip.setPixelColor(h,color)
           		for i in chaseA2a:
           			strip.setPixelColor(i,color)
			for j  in chaseH3a:
				strip.setPixelColor(j,color)
        	        strip.show()
                	time.sleep(wait_ms/60)
                	for k in range(strip.numPixels()):
                		strip.setPixelColor(k,0)
                	strip.show()

	                for h in chaseB1b:
				strip.setPixelColor(h,color)
                	for i in chaseA2b:
                		strip.setPixelColor(i,color)
                	for j  in chaseH3b:
                		strip.setPixelColor(j,color)
                	strip.show()
                	time.sleep(wait_ms/60)
                	for k in range(strip.numPixels()):
                		strip.setPixelColor(k,0)
                	strip.show()

	                for h in chaseB1c:
                		strip.setPixelColor(h,color)
                	for i in chaseA2c:
                		strip.setPixelColor(i,color)
                	for j  in chaseH3c:
                		strip.setPixelColor(j,color)
                	strip.show()
                	time.sleep(wait_ms/60)
                	for k in range(strip.numPixels()):
                		strip.setPixelColor(k,0)
                	strip.show()

def hum(strip, color):
	"""HUM"""
	for p in range(iterations):
	        for q in range(3):
        		for h in chaseH1a:
				strip.setPixelColor(h,color)
            		for i in chaseU2a:
                		strip.setPixelColor(i,color)
            		for j  in chaseM3a:
                		strip.setPixelColor(j,color)
            		strip.show()
            		time.sleep(wait_ms/60)
            		for k in range(strip.numPixels()):
            			strip.setPixelColor(k,0)
            		strip.show()

		        for h in chaseH1b:
                		strip.setPixelColor(h,color)
            		for i in chaseU2b:
                		strip.setPixelColor(i,color)
            		for j  in chaseM3b:
                		strip.setPixelColor(j,color)
            		strip.show()
            		time.sleep(wait_ms/60)
            		for k in range(strip.numPixels()):
            			strip.setPixelColor(k,0)
            		strip.show()

	    		for h in chaseH1c:
            			strip.setPixelColor(h,color)
            		for i in chaseU2c:
				strip.setPixelColor(i,color)
            		for j  in chaseM3c:
            			strip.setPixelColor(j,color)
            		strip.show()
            		time.sleep(wait_ms/60)
            		for k in range(strip.numPixels()):
            			strip.setPixelColor(k,0)
            		strip.show()

def bug(strip, color):
	"""BUG"""
	for p in range(iterations):
	        for q in range(3):
	        	for h in chaseB1a:
               			strip.setPixelColor(h,color)
            		for i in chaseU2a:
                		strip.setPixelColor(i,color)
            		for j  in chaseG3a:
                		strip.setPixelColor(j,color)
            		strip.show()
            		time.sleep(wait_ms/60)
            		for k in range(strip.numPixels()):
            			strip.setPixelColor(k,0)
            		strip.show()

			for h in chaseB1b:
		                strip.setPixelColor(h,color)
        		for i in chaseU2b:
                		strip.setPixelColor(i,color)
            		for j  in chaseG3b:
                		strip.setPixelColor(j,color)
            		strip.show()
            		time.sleep(wait_ms/60)
            		for k in range(strip.numPixels()):
                		strip.setPixelColor(k,0)
            		strip.show()

			for h in chaseB1c:
                		strip.setPixelColor(h,color)
            		for i in chaseU2c:
                		strip.setPixelColor(i,color)
            		for j  in chaseG3c:
                		strip.setPixelColor(j,color)
            		strip.show()
            		time.sleep(wait_ms/60)
            		for k in range(strip.numPixels()):
            			strip.setPixelColor(k,0)
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
#		strip._cleanup
		bah(strip, Color(255,0,0))
		time.sleep(1)
#		theaterChase(strip, Color(127,127,127))
#		lightWipe(strip)
		hum(strip, Color(0,0,255))
		time.sleep(1)

#		theaterChase(strip, Color(127,127,127))
#		lightWipe(strip)
		bug(strip, Color(0,255,0))
		time.sleep(1)

		theaterChase(strip, Color(127,127,127))
#		theaterChase(strip, Color(127,127,127))
#		theaterChase(strip, Color(0,255,0))  # Red theater chase
