# hello_cheetah
Minimal "Hello World" example of a quadruped robot in a bybullet simulation.

The simulation is very minimal.  First, the Mini-Cheetah will appear in the air with its feet slightly above the floor.  The robot falls to the floor.  This shows how the simulation detects and handles collisions between solid objects.  (The floor and the robot’s feet are both solid.) Next, the robot lowers its body by bending at the knees.  This provides two things (1) example code to move a robot's joints and (2) that gravity continues to influence the robot, as the feet stay in contact with the floor and the body lowers.

How to install and run this:
- Optionally, set up a Python virtual environment using the "virtualenv" command.  Nothing really bad happens if you don't do this but it is best practice.
- Clone this repository onto your computer
- Install the Python package "pybullet" using the command "pip install pybullet"
- Run the demo by using the command "python3 hello_cheetah.py"       

Note:  The simulation will run in ultra-slow motion.  This is intentional because running in real-time requires more code than I want in a Hello World example.

Author:  Chris Albertson, albertson.chris@gmail.com

One more thing — Free free to use this repository as a GitHub exercise space.  Report problems and send pull requests.  The goal is to make this a better minimal example and allow more people to get into running quadruped simulations.  Eventually, there will be a series of graduated examples.
