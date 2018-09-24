left_motor = "47258416584374622758504"
right_motor = "47248007641358630233090"

rsticky = -Gamepad.get_value("joystick_right_y")
rstickx = Gamepad.get_value("joystick_right_x")
lsticky = -Gamepad.get_value("joystick_left_y")
lstickx = Gamepad.get_value("joystick_left_x")

def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(autonomous_actions)

def autonomous_main():
    pass

async def autonomous_actions():
    print("Autonomous action sequence started")
    await Actions.sleep(1.0)
    print("1 second has passed in autonomous mode")

def teleop_setup():
    print("Tele-operated mode has started!")

def teleop_main():
    if lsticky > 0.25:
        Robot.set_value(left_motor,"duty_cycle", lsticky)
        