# Project-2

> please use catkin_scara.zip package to build on your PC.
> catkin_make

> Followed the gazebo tutorials
> added motor plugins for 3 joints in scara.xacro
> added gazebo pluggins in launch file and added joint3

> rostopic pub -1 /scara/joint1_position_controller/command std_msgs/Float64 "data: 1.5"
> 
> rostopic pub -1 /scara/joint2_position_controller/command std_msgs/Float64 "data: 1.5"
> 
> rostopic pub -1 /scara/joint3_position_controller/command std_msgs/Float64 "data: 1.0"




# Manipulator_project_RBE

# -----------------------------------------------------------------------------------------#
# Project-1

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

