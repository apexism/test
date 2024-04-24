from pymycobot.mycobot import MyCobot
import time

mc = MyCobot('/dev/ttyACM0', 115200)
mc.set_gripper_mode(0)
mc.init_eletric_gripper()
time.sleep(1)

while True:
    mc.set_eletric_gripper(0)
    mc.set_gripper_value(10,1)
    print("open gripper")
    time.sleep(5)

    mc.set_eletric_gripper(1)
    mc.set_gripper_value(0,1)
    print("close gripper")
    time.sleep(5)


# mc.set_eletric_gripper(0)
# mc.set_gripper_value(100,20)
# time.sleep(2)