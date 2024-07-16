
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from interface.feetech.robot import Robot as RobotFT



# init robots
leader = RobotFT(device_name="COM7", servo_ids=[1,2,3,4,5,6])
follower = RobotFT(device_name="COM10", servo_ids=[1,2,3,4,5,6])


def get_bias():
    length = len(leader.read_position())
    leader_pos = leader.read_position()
    print(f"leader_pos: {leader_pos}")
    follower_pos = follower.read_position()
    print(f"follower_pos: {follower_pos}")
    bias = [leader_pos[i] - follower_pos[i] for i in range(length)]
    print(bias)
    return bias


get_bias()
