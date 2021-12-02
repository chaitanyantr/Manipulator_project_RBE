# Project-2

> please use catkin_scara.zip package to build on your PC.
> catkin_make
> Start the controllers using roslaunch

Test the Scara controlled by ros_control by running the following:

# Start the scara simulation:

> roslaunch scara_gazebo scara_world.launch

# Load the controllers for the three joints by running the second launch file:

> roslaunch scara_control scara_control.launch

# Using service calls manually

If you first load the scara_control.yaml files to the parameter server, you could load the controllers manually through service requests. We'll include them here for reference though we usually prefer roslaunch:

# Load the controllers:

rosservice call /scara/controller_manager/load_controller "name: 'joint1_position_controller'"
rosservice call /scara/controller_manager/load_controller "name: 'joint2_position_controller'"

# Start the controllers:

rosservice call /scara/controller_manager/switch_controller "{start_controllers: ['joint1_position_controller','joint2_position_controller'], stop_controllers: [], strictness: 2}"

# Stop the controllers:

rosservice call /scara/controller_manager/switch_controller "{start_controllers: [], stop_controllers: ['joint1_position_controller','joint2_position_controller'], strictness: 2}"

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

