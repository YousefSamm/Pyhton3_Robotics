from robot_control_class import RobotControl
RC=RobotControl("summit")
RC.move_straight_time("forward", 0.3, 5)
RC.turn("clockwise", 0.3, 7)
