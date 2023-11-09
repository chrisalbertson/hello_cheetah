"""
Minimal "hello world" style example of a quadruped robot running in a simulation.

How to install and run this:
    1)  optionally, setup a Python virtual environment using the "virtualenv" command.
        Nothing really bad happens if you don't do this but it is best practice.
    2)  Install the Python package "pybullet" using the command
        "pip install pybullet"
    3)  Run the demo by using the command
        "python3 hello_cheetah.py"
        You should see some output at the terminal and a window will open showing
        a tiny robot on a blue and white checkerboard floor.  You can zoom and
        rotate the view with your mouse if you hold the control key and mouse button
        at the same time.
        Note:  The simulation is in ultra-slow motion.  This is intentional because
        running in real-time requires more code than is desired in a hello word demo.
"""
import pybullet as p
import pybullet_data
import time

# Below is some "boiler plate" to create the simulation, add the floor and the
# robot and then define the strength and direction of the Earth's gravity.
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
plane = p.loadURDF("plane.urdf")
robot = p.loadURDF("mini_cheetah.urdf", [0., 0., 0.5])
p.setGravity(0,0,-10)


""" 
Print information about each of the 16 joints that are defined in the URDF file.
You have to lookup getJointInfo() to know what the output means.  Each joint has
a "joint index" and you just have to know which index number refers to which 
URDF joint.  The information printed by this loop should help make this clear.
"""
for i in range(p.getNumJoints(robot)):
    print(p.getJointInfo(robot, i))


"""
These constants are somewhat arbitrary.  They were determined by eye to create
a "neutral stand" look.  Change them to any value you like and see what happens.
(It is very easy to select values that move the feet such that the robot falls down.)
They are angles with units of radians.  The angles are applied to all four legs.  
"""
thigh_neutral =  0.5
knee_neutral  = -1.9 * thigh_neutral


"""
The simulation advances in increments of "tick_increment" seconds per cycle.
The default is 1/240 second.
"""
tick_increment = 1. / 50.
tick_count = 0
p.setTimeStep(tick_increment)


"""
This is the simulation loop.  Time is advanced by tick_increment seconds each
time the loop cycles.  In this "hello world" example we do nothing for the first
simulated two seconds (100 ticks.)  
This allows time for the simulated gravity to pull the robot's feet to the floor
and for any bouncing to stop.
"""
while True:
    p.stepSimulation()
    time.sleep(tick_increment)
    tick_count += 1
    sim_time = tick_count * tick_increment

    # wait for two simulated seconds
    if sim_time == 2.0:
        print("bending joints...")

        """
        The URDF file defines 16 joints, four for each leg.  Of these only 12
        joints can move.  The "toe" joint connects the rubber-ball foot to the lower
        leg and this joint can not move.
        
        Notice that we are setting the target rotation angle it one giant step.
        The simulator will start the bending motion right away but because the joints
        can only move so fast, they will continue bending in future cycles until
        they reach the target angles.  Tis is not the best way to program robot motion
        but it is the simplest way so is suitable for a "hello world" demo.
        """

        # Set the angles for all 4 knee joints.  
        # set the max joint velocity to be proportional the amount of rotation
        for j in [2, 6, 10, 14]:
            p.setJointMotorControl2(robot, j,
                                    p.POSITION_CONTROL,
                                    targetPosition=knee_neutral,
                                    maxVelocity=2.0*knee_neutral)

        # Set the angles for all 4 hip joints.
        # set the max joint velocity to be proportional the amount of rotation
        for j in [1, 5, 9, 13]:
            p.setJointMotorControl2(robot, j,
                                    p.POSITION_CONTROL,
                                    targetPosition=thigh_neutral,
                                    maxVelocity=2.0*thigh_neutral)

