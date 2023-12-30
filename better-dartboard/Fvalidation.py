def toInt(x):
    try:
        x = int(x)
        return x
    except:
        return False
    


def validateAboveZero(x:int):
    if x >= 0:
        return x
    else: 
        return False
    