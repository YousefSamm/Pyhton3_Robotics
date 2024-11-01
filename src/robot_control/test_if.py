from robot_control_class import RobotControl
rc=RobotControl()
distance = rc.get_laser(360)
if distance > 1: 
  rc.move_straight()

else:
  rc.stop_robot()

print("the wall is ", distance, " meters Away \n")

