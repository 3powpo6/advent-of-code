input = open("input", "r")
strat1 = {'BX':1,'CY':2,'AZ':3,'AX':4,'BY':5,'CZ':6,'CX':7,'AY':8,'BZ':9}
strat2 = {'BX':1,'CX':2,'AX':3,'AY':4,'BY':5,'CY':6,'CZ':7,'AZ':8,'BZ':9}
score1 = 0
score2 = 0
for x in input:
    line = x.strip().replace(" ","")
    score1 += strat1[line]
    score2 += strat2[line]
print("Total score using strategy 1:", score1)
print("Total score using strategy 2:", score2)