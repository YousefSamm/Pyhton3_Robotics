from robot_control_class import RobotControl
control=RobotControl("summit")
control.move_straight_time("forward",2, 1 )
control.turn("counter_clockwise", 3.14/2.8, 1)
control.move_straight_time("forward",1, 1)
control.turn("counter_clockwise", 3.14/2.8, 1)
control.move_straight_time("forward",2, 2 )