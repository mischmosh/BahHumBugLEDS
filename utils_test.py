from __future__ import print_function
import code
import utils

l11 = [0,1,2]
l12 = [3,4]
l13 = [5,6,7,8]

w1 = utils.Word(None, l11, l12, l13)

print('Word 1 Length 9 = %s' % (len(w1),) )

colors = ['R', 'G', 'B', 'Y', 'O']

p1 = utils.Pattern(colors, width=3)
print( list(p1.make(21)) )


code.interact(local=locals())
