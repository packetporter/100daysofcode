def wall_on_left():
    turn_left()
    if wall_in_front():
        turn_right()
        return True
    else:
        turn_right()
        return False
   
while not at_goal():
    if right_is_clear():
        turn_right()
    elif front_is_clear():
        move()
    else:
        turn_left()


