# Code for Reeborg's World; Hurdles 4 Challenge
# URL: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# This is a "basic introduction to functions" challenge, with the functions already defined in the site's backend, so it won't do anything here in an IDE. This is just to log it.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def above_hurdle_rotation():
    turn_right()
    move()
    turn_right()
    move()
    
def cross_hurdle():
    if wall_in_front():
        turn_left()
    while wall_on_right():
        move()
    above_hurdle_rotation()
    while wall_on_right() and front_is_clear():
        move()
    if front_is_clear() == False:
        turn_left()

def traverse_empty_space():
    while front_is_clear():
        if not at_goal():
            move()
        elif at_goal():
            done()
            
while not at_goal():
    traverse_empty_space()
    cross_hurdle()