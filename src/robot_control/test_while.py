from robot_control_class import RobotControl
rc = RobotControl()
distance = rc.get_laser(360)
while distance > 1:
 rc.move_straight()
  
 distance = rc.get_laser(360)
 print ("the wall is ", distance, " meters away")

rc.stop_robot()
print ("the wall is ", distance, " meters away as we stopped")