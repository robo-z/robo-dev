import numpy as np
from interface.dynamixel.robot import Robot
from interface.feetech.robot import Robot as RobotFT


# init robots
leader = RobotFT(device_name="COM7", servo_ids=[1,2,3,4,5,6])
follower = RobotFT(device_name="COM6", servo_ids=[1,2,3,4,5,6])

# leader = Robot(device_name="/dev/ttyACM0", servo_ids=[1,2,3,4,5,6])
# follower = RobotFT(device_name="/dev/ttyUSB0", servo_ids=[1,2,3,4,5,6])

# activate the leader gripper torque

# leader._disable_torque()

leader.set_trigger_torque(value=500)
# leader._disable_torque()
bias = np.array([-8, 93, 198, 431, 66, 1009])

while True:
    # print(leader.read_position()-bias)
    action = leader.read_position()-bias
    print(action)
    follower.set_goal_pos(action)

leader._disable_torque()
#follower._disable_torque()



