import numpy as np

import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from interface.dynamixel.robot import Robot
from interface.feetech.robot import Robot as RobotFT


# init robots
# leader = RobotFT(device_name="COM7", servo_ids=[1,2,3,4,5,6])
# follower = RobotFT(device_name="COM6", servo_ids=[1,2,3,4,5,6])

leader = RobotFT(device_name="/dev/ttyUSB1", servo_ids=[1,2,3,4,5,6])
follower = RobotFT(device_name="/dev/ttyUSB0", servo_ids=[1,2,3,4,5,6])

# activate the leader gripper torque

# leader._disable_torque()

leader.set_trigger_torque(value=500)
# leader._disable_torque()
bias = np.array([131, 157, -82, 35, 123, 750])

while 0:
    # print(leader.read_position()-bias)
    try:
        raw_posistion = leader.read_position()
    except:
        continue
    
    print(f"RAW: {raw_posistion}")
    action = raw_posistion-bias
    print(f"After Bias: {action}")
    follower.set_goal_pos(action)





