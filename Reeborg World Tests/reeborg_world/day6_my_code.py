
while not at_goal():
    while not wall_on_right() and front_is_clear():
        turn_right()
        move()
    while wall_on_right():
        if front_is_clear():
            move()
        elif wall_in_front():
            turn_left()
            if wall_in_front():
                turn_left()     
    while right_is_clear() and not at_goal():
        turn_right()
        move()
