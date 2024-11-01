from robot_control_class import RobotControl
rc=RobotControl()
a=rc.get_laser_full()
b={'Postion 0':a[0], 'Poistion 100': a[100],'Poistion 200': a[200],'Poistion 300': a[300], 'Poistion 400': a[400], 'Poistion 500': a[500], 'Poistion 600': a[600], 'Poistion 719': a[719] }
print (b)
