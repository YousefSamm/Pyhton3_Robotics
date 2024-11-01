from robot_control_class import RobotControl
import time
RC=RobotControl()
def move_for(t):
      RC.move_straight()
      time.sleep(t)
      RC.stop_robot()

t=int(input ("enter the time: "))
move_for(t)
