def recept(antal):
    print( round( antal * 0.75), "st ägg")
    print( antal * 0.75,  "dl ströbröd")
    print( antal * 0.5,   "tsk vaniljsocker")
    print( antal * 0.5,   "tsk bakpulver")
    print( antal * 0.75,  "dl vetemjöl")
    print( antal * 18.75, "g smör")
    print( antal * 0.25,  "dl vatten")


def tidblanda(antal):
    return 10 + antal


def tidgradda(antal):
    return 30 + 3 * antal

def sockerkaka(antal):
    print("tid:", tidblanda(antal) + tidgradda(antal), "min")
    recept(antal)


#SCRIPT

sockerkaka(4)
print("") #blankrad, gör det lättare å läsa
sockerkaka(7)
