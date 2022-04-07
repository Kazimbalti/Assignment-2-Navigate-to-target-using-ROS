# Assignment-2-Navigate-to-target-using-ROS

## This is the repository about ROS: Zero to ROS course on Udamy.
https://www.udemy.com/course/school-of-ros-zero-to-ros/

## This is the second assignment (Navigate to target) of Zero to ROS course
#### Here is the attached video of this assignment 02 (Navigate to target).
### Task is: 
Use Rosparam to change the location of your target (a parameter for each coordinate: x and y) and to define the radius that defines the threshold within which the target is considered reached. Create a node called "turtle_guide_to_xy" that guides the turtle to the target location. 
https://youtu.be/1fjvXMGLQGg

To run this repository first create a catkin workspace
1. mkdir -p ~/catkin-ws/src
2. cd ~/catkin_ws/src
3. catkin_init_workspace
4. cd ~/catkin_ws
5. catkin_make 


## To clone this repository 
2. cd catkin_ws/src
2. git clone https://github.com/Kazimbalti/Assignment-2-Navigate-to-target-using-ROS.git
3. cd catkin_ws
4. catkin_make

## Open 4 terminals
### In first terminal
 roscore

### second terminal
 rosrun turtlesim turtlesim_node

### 3rd ternial

