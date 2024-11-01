from robot_control_class import RobotControl
rc= RobotControl()
a=rc.get_laser_full()
print ('the 1st laser value is: ', a[0])
print ('the 2nd laser value is: ', a[360])
print ('the 3rd laser value is: ', a[719])
