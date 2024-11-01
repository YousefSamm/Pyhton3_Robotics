from robot_control_class import RobotControl
rc = RobotControl()
parameter = int(input ("enter a number between 0 and 719: "))
laser = rc.get_laser(parameter)
print ( '\n the laser value is: ', float(laser))
