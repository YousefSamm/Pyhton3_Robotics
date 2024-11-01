from robot_control_class import RobotControl
control=RobotControl()
distance=control.get_laser_full()
while(True): 
 while (distance[360]>=1.1):
  control.move_straight()
  distance=control.get_laser_full()
 control.stop_robot() 
 distance_left=distance[719]
 distance_right=distance[0]
 if distance_right>distance_left:
  control.rotate(-80)
 else:
  control.rotate(92)
 distance=control.get_laser_full()
