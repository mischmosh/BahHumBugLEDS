# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)

from setup_bah_hum_bug import *

def clear_strip():
    strip = make_strip()
    set_color(strip)

# Main program logic follows: Trun off all LEDs
if __name__ == '__main__':
    clear_strip()
