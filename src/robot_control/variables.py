from robot_control_class import RobotControl
rc=RobotControl()
laser1= rc.get_laser(360)
print("the laser value receives is: ",laser1)
laser2= rc.get_laser(350)
print("the laser value receives is: ",laser2)
laser2 =rc.get_laser(370)
print("the laser value receives is: ",laser2)
