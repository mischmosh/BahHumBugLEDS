# Define letters to spell BAH - HUM - BUG

# Old painfully entered led sets
#letterB1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,90,91,92,93,94]
#letterA2 = [100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,180,181,182,183,184]
#letterH3 = [185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,274,275,276,277,278,279,280,281,282,283,284,285] 

#letterH1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
#letterU2 = [125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179]
#letterM3 = [185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253]

#letterG3 = [191,192,193,194,195,196,197,198,199,200,201,237,238,246,247,248,249,250,251,252,253,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303]

# New Letters

w1_left_straight = range(0,22)
w1_right_arcs = range(23,65) + range(90,96)
w1_right_straight = range(77,99)
w1_middle_bar_left = range(65,72)
w1_middle_bar_full = w1_middle_bar_left + range(72,77)

w2_left_swoop = range(147,180)
w2_diagnol = range(100,125)
w2_middle_bar = range(141,147)
w2_right_upper_straight = range(125, 141)
w2_right_lower_straight = range(180,185)

w3_lower_left_straight = range(185,191)
w3_left_straight = range(191,202)
w3_upper_left_straight = range(202,208)

w3_lower_right_straight = range(248,254)
w3_lower_right_straightG = range(246,254)
w3_right_straight = range(237,248)
w3_upper_right_straight = range(231,237)

w3_lower_arc = range(255,273)
w3_upper_arc = range(286,304)
w3_upper_valley = range(208,231)
w3_middle_bar = range(274,286) 

letterB1 = w1_left_straight + w1_right_arcs + w1_middle_bar_left
letterH1 = w1_left_straight + w1_middle_bar_full + w1_right_straight

letterA2 = w2_diagnol + w2_middle_bar + w2_right_lower_straight + w2_right_upper_straight
letterU2 = w2_left_swoop + w2_right_upper_straight

letterH3 = w3_lower_right_straight + w3_lower_left_straight + w3_right_straight + w3_left_straight + w3_upper_right_straight + w3_upper_left_straight + w3_middle_bar
letterM3 = w3_lower_right_straight + w3_lower_left_straight + w3_right_straight + w3_left_straight + w3_upper_right_straight + w3_upper_left_straight + w3_upper_valley
letterG3 = w3_upper_arc + w3_left_straight + w3_lower_arc + w3_lower_right_straightG


bah_pixels = letterB1 + letterA2 + letterH3
hum_pixels = letterH1 + letterU2 + letterM3
bug_pixels = letterB1 + letterU2 + letterG3
