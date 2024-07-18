import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from interface.feetech.robot import Robot as RobotFT

leader = RobotFT(device_name="/dev/ttyUSB1", servo_ids=[1,2,3,4,5,6])
follower = RobotFT(device_name="/dev/ttyUSB0", servo_ids=[1,2,3,4,5,6])

leader._disable_torque()
follower._disable_torque()