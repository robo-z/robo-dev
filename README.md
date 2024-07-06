# robo-dev
Code Resources for Robo-X development 


# 操作步骤
1. 确认主动臂和从动臂的端口号，一般使用舵机供应商的debug软件可以确定
2. 使用preperation/alignment.py 确定主从臂的偏置
3. 使用preperation/teleoperation.py 测试偏置以及遥操作是否正常
4. 确任相机是否正常，最好使用操作系统自带的相机功能确定一个角度，然后使用preperation/debug_cam.ipynb测试截图是否正常