from robot_control_class import RobotControl
rc =  RobotControl()
lasers=rc.get_laser_full()
High=0
for x in lasers:
 if x > High:
   High=x

print("Highest Value is: ", High)

  
