from robot_control_class import RobotControl
RC=RobotControl(robot_name="summit")
def exercice4(a):
   d = RC.get_laser_summit(int(a[0]))
   e = RC.get_laser_summit(int(a[1]))
   f = RC.get_laser_summit(int(a[2]))
   return [d, e, f]
a=[0, 0, 0]
for i in range(3): 
    a[i] = input ("enter a number between 0 and 719: ")  
    while (True):
     if (int(a[i])>=0 and int(a[i])<=719)==0:
       a[i] = input ("Wrong input, please enter a number between 0 and 719: ") 
     if (int(a[i])>=0 and int(a[i])<=719)==1:
      break

list = exercice4(a)
print (list)
