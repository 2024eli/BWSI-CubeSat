
def sector_area(location):
    sec = 0
    if 0 < location  < 60:
        sec = 2
    if 60 < location < 120:
        sec = 3
    if 120 < location < 180:
        sec = 4
    if 180 < location < 240:
        sec = 5
    if 240 < location < 300:
        sec = 6
    if 300 < location < 360:
        sec = 1
    return sec
