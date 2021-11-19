# Manipulator_project_RBE

if you want to run in your pc

 > take 'gazebo_ros_demo' folder in to your src

 > catkin_make

# launch file

> roslaunch rrbot_gazebo world.launch

# Test FK

> rosrun rrbot_control fk.py

# Output of fk 
> rostopic echo /arm_pose 

# Test IK

>rosrun rrbot_control ik.py

# Output for ik

> rosservice call /inver_server 

# Make sure you do
> source devel/setup.bash

> python files as executing files(right click the file and go to permission and allow it as executing file)

