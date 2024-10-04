# Jalayan Vikram Robot



## Overview

**Jalayan Vikram Robot** is an autonomous amphibious robot designed for post-flood relief operations. This project leverages ROS2, Gazebo, OpenCV, and the Raspberry Pi 4 to create a powerful system capable of navigating land and water environments for disaster recovery. The robot's core feature is its ability to geo-tag locations, which helps optimize resource allocation and significantly reduces response time in flood-affected areas.

## Features

- **Amphibious Design:** Designed to operate both on land and in water, suitable for flood rescue missions.
- **Autonomous Navigation:** ROS2-based control for real-time movement and decision-making.
- **Geo-tagging System:** Optimizes resource allocation by tagging locations during the rescue operation.
- **Obstacle Detection:** Uses sensors and OpenCV for object detection and obstacle avoidance.
- **Simulated Testing:** Developed and tested in Gazebo before real-world implementation.
- **Raspberry Pi 4:** Low-cost, high-performance computing for real-time operations.

## Technologies Used

- **ROS2 (Robot Operating System 2)**
- **Gazebo Simulator**
- **OpenCV (Computer Vision Library)**
- **Raspberry Pi 4**
- **Fusion 360 (3D Modeling and Design)**

## Development Process

1. **Design:** 3D design using Fusion 360 for an amphibious chassis.
2. **Simulation:** Testing in a virtual flood environment using Gazebo.
3. **Autonomous Navigation:** ROS2 nodes for movement and obstacle detection.
4. **Object Detection:** Integrated OpenCV for real-time object detection.
5. **Geo-tagging:** Implemented location-based tagging to enhance disaster relief coordination.

---

## How to Build and Run the Package

### Prerequisites

- **ROS2** installed on your system. You can find instructions to install ROS2 [here](https://docs.ros.org/en/foxy/Installation.html).
- **Gazebo** installed for simulation.
- A basic understanding of ROS2 nodes and packages.

### 1. Create a ROS2 Workspace

To begin, create a workspace and initialize your project package.

```bash
mkdir -p ~/jalayan_ws/src
cd ~/jalayan_ws/src
ros2 pkg create --build-type ament_python flood_robot
```

### 2. Clone the Project Repository

Clone the repository into your workspace:

```bash
git clone https://github.com/jaswanth-coder/Flood_robo.git
```

### 3. Implement the Movement and Obstacle Detection

In the `flood_robot` directory, create two Python files: `move_robot.py` and `obstacle_detection.py`. These files will handle the robot’s movement and obstacle detection, respectively.

#### `move_robot.py`



#### `obstacle_detection.py`



### 4. Create a Launch File

In the `launch` directory, create a launch file `flood_robot_launch.py` to launch both the movement and obstacle detection nodes.



### 5. Build the Package

After writing the code, build the ROS2 package:

```bash
cd ~/jalayan_ws
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

### 6. Run the Launch File

Finally, launch the package:

```bash
ros2 launch flood_robot flood_robot_launch.py
```

This will start the robot movement and obstacle detection system.

---

## Simulation in Gazebo

You can test the robot’s behavior in a simulated environment using **Gazebo**. Modify the package to include a simulation world and robot model, and test the movement and obstacle avoidance in a virtual flood scenario.

---

## Conclusion

**Jalayan Vikram Robot** is an ideal beginner project that introduces you to core robotics concepts such as autonomous navigation, obstacle detection, and sensor integration using **ROS2**. Its application in post-flood relief scenarios demonstrates the real-world utility of robotics in disaster management. As you continue to develop the project, consider incorporating more advanced AI algorithms for better performance.


Special Thanks to https://www.pcbway.com/project/shareproject/3D_Printed_Screw_propelled_Robot_With_Video_Feed_8bf6a5c6.html
Contributions are welcome. Check out the [CONTRIBUTING.md](./CONTRIBUTING.md) for more details.

---

For further inquiries or support, please contact the project maintainers.

