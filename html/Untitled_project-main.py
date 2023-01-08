# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image(
                '00900:'
                '00500:'
                '05550:'
                '50505:'
                '05050:'
                        ))
    sleep(10000)
    display.show(Image(
        '50005:'
        '05050:'
        '00500:'
        '05050:'
        '50005:'
    ))
    sleep(1000)
    
